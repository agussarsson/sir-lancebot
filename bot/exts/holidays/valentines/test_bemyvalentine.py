import pytest
import discord
from unittest.mock import AsyncMock, MagicMock
from discord.ext import commands

from bot.constants import Roles
from bot.exts.holidays.valentines.be_my_valentine import BeMyValentine


@pytest.mark.asyncio
async def test_anonymous_user_without_lovefest_role():
    """Test that sending a valentine to a user without the lovefest role raises UserInputError."""
    bot = MagicMock()
    cog = BeMyValentine(bot)

    ctx = MagicMock()
    ctx.message.delete = AsyncMock()
    ctx.author = MagicMock()
    user = MagicMock()
    user.roles = []  # User does not have the lovefest role

    with pytest.raises(commands.UserInputError, match="You cannot send a valentine to .* as they do not have the lovefest role!"):
        await cog.anonymous(cog, ctx, user)  

    ctx.message.delete.assert_awaited()


@pytest.mark.asyncio
async def test_anonymous_self_valentine():
    """Test that a user cannot send a valentine to themselves."""
    bot = MagicMock()
    cog = BeMyValentine(bot)

    ctx = MagicMock()
    ctx.author = MagicMock()
    ctx.message.delete = AsyncMock()
    user = ctx.author  # Self-send

    # Ensure the user has the lovefest role
    user.roles = [MagicMock(id=Roles.lovefest)]

    with pytest.raises(commands.UserInputError, match="Come on, you can't send a valentine to yourself"):
        await cog.anonymous(cog, ctx, user)  
    ctx.message.delete.assert_not_awaited()  # No need to delete the message in this case

@pytest.mark.asyncio
async def test_anonymous_successful_message():
    """Test that an anonymous valentine is successfully sent via DM."""
    bot = MagicMock()
    cog = BeMyValentine(bot)

    ctx = MagicMock()
    ctx.author = MagicMock()
    ctx.message.delete = AsyncMock()
    ctx.author.send = AsyncMock()

    user = MagicMock()
    user.roles = [MagicMock(id=Roles.lovefest)] 
    user.display_name = "Recipient"
    user.send = AsyncMock()

    cog.random_emoji = MagicMock(return_value=("💖", "💕"))
    cog.valentine_check = MagicMock(return_value=("A lovely poem", "A poem dedicated to"))

    await cog.anonymous(cog, ctx, user, valentine_type="p")  

    user.send.assert_awaited()  # DM should be sent
    ctx.author.send.assert_awaited_with(f"Your message has been sent to {user}")  # Notify sender
    ctx.message.delete.assert_awaited()  # Original command message should be deleted


@pytest.mark.asyncio
async def test_anonymous_recipient_dm_disabled():
    """Test that an error is raised when the recipient has DMs disabled."""
    bot = MagicMock()
    cog = BeMyValentine(bot)

    ctx = MagicMock()
    ctx.author = MagicMock()
    ctx.message.delete = AsyncMock()
    ctx.author.send = AsyncMock()

    user = MagicMock()
    user.roles = [MagicMock(id=Roles.lovefest)]  
    user.display_name = "Recipient"

    # Properly mock the discord.Forbidden exception
    forbidden_exception = discord.Forbidden(response=MagicMock(), message="Forbidden")
    user.send = AsyncMock(side_effect=forbidden_exception)  # Simulate DMs being disabled

    cog.random_emoji = MagicMock(return_value=("💖", "💕"))
    cog.valentine_check = MagicMock(return_value=("A lovely poem", "A poem dedicated to"))

    with pytest.raises(commands.UserInputError, match=".* has DMs disabled, so I couldn't send the message. Sorry!"):
        await cog.anonymous(cog, ctx, user, valentine_type="p")  

    ctx.message.delete.assert_awaited()