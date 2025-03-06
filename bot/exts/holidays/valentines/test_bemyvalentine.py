import pytest
import discord
from unittest.mock import AsyncMock, MagicMock
from discord.ext import commands

from bot.constants import Roles, Channels, Colours
from .be_my_valentine import BeMyValentine


@pytest.mark.asyncio
async def test_send_valentine_user_without_lovefest_role():
    """Test that sending a valentine to a user without the lovefest role raises UserInputError."""
    bot = MagicMock()
    cog = BeMyValentine(bot)

    # Create a context with a valid guild so that the guild check passes.
    ctx = MagicMock()
    ctx.guild = MagicMock()
    ctx.author = MagicMock()
    ctx.message = MagicMock()
    ctx.message.delete = AsyncMock()
    ctx.send = AsyncMock()

    user = MagicMock()
    user.roles = []  # User does not have the lovefest role
    user.mention = "@UserWithoutRole"

    with pytest.raises(commands.UserInputError, match="You cannot send a valentine to .* as they do not have the lovefest role!"):
        await cog.send_valentine.callback(cog, ctx, user, valentine_type="p")


@pytest.mark.asyncio
async def test_send_valentine_self_valentine():
    """Test that a user cannot send a valentine to themselves."""
    bot = MagicMock()
    cog = BeMyValentine(bot)

    ctx = MagicMock()
    ctx.guild = MagicMock()  # valid guild
    ctx.author = MagicMock()
    ctx.author.mention = "@Sender"
    ctx.message = MagicMock()
    ctx.message.delete = AsyncMock()

    user = ctx.author  # Self-send
    # Ensure the author has the lovefest role
    user.roles = [MagicMock(id=Roles.lovefest)]
    user.mention = "@Sender"

    with pytest.raises(commands.UserInputError, match="Come on, you can't send a valentine to yourself"):
        await cog.send_valentine.callback(cog, ctx, user, valentine_type="p")


@pytest.mark.asyncio
async def test_send_valentine_successful_message():
    """Test that a public, signed valentine is sent successfully."""
    bot = MagicMock()
    cog = BeMyValentine(bot)

    # Prepare a mock channel and have bot.get_channel return it.
    channel_mock = MagicMock()
    channel_mock.send = AsyncMock()
    bot.get_channel.return_value = channel_mock

    ctx = MagicMock()
    ctx.guild = MagicMock()  # valid guild
    ctx.author = MagicMock()
    ctx.author.mention = "@Sender"
    ctx.message = MagicMock()
    ctx.message.delete = AsyncMock()

    user = MagicMock()
    # User has the lovefest role
    user.roles = [MagicMock(id=Roles.lovefest)]
    user.display_name = "Recipient"
    user.mention = "@Recipient"

    # Set up mocks for random_emoji and valentine_check.
    cog.random_emoji = MagicMock(return_value=("💖", "💕"))
    cog.valentine_check = MagicMock(return_value=("A lovely poem", "A poem dedicated to"))

    await cog.send_valentine.callback(cog, ctx, user, valentine_type="p")

    # Verify that the channel's send was called (the command sends the embed to the channel).
    channel_mock.send.assert_awaited()


@pytest.mark.asyncio
async def test_send_valentine_guild_none():
    """Test that using the command outside a guild raises an error."""
    bot = MagicMock()
    cog = BeMyValentine(bot)

    ctx = MagicMock()
    ctx.guild = None  # Not in a guild
    ctx.author = MagicMock()
    ctx.message = MagicMock()
    ctx.message.delete = AsyncMock()

    user = MagicMock()
    user.roles = [MagicMock(id=Roles.lovefest)]
    user.mention = "@User"

    with pytest.raises(commands.UserInputError, match="You are supposed to use this command in the server."):
        await cog.send_valentine.callback(cog, ctx, user, valentine_type="p")
