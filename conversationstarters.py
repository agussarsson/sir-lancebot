import logging
import random
from pathlib import Path

from discord.ext import commands

log = logging.getLogger(__name__)

starters = [
    'What is your favourite Easter candy or treat?',
    'What is your earliest memory of Easter?',
    'What is the title of the last book you read?',
    'What is better: Milk, Dark or White chocolate?',
    'What is your favourite holiday?',
    'If you could have any superpower, what would it be?',
    'Name one thing you like about a person to your right.',
    'If you could be anyone else for one day, who would it be?',
    'What Easter tradition do you enjoy most?',
    "What is the best gift you've been given?",
    'Name one famous person you would like to have at your easter dinner.',
    'What was the last movie you saw in a cinema?',
    'What is your favourite food?',
    'If you could travel anywhere in the world, where would you go?',
    'Tell us 5 things you do well.',
    'What is your favourite place that you have visited?',
    'What is your favourite color?',
    'If you had $100 bill in your Easter Basket, what would you do with it?',
    'What would you do if you know you could succeed at anything you chose to do?',
    'If you could take only three things from your house, what would they be?'
]


class ConvoStarters(commands.Cog):
    """A cog which posts easter conversation starters"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=('conversation_starters', 'convo_starters'))
    async def convo_starter(self, ctx):
        """Responds with a random conversation starter"""

        await ctx.send(f"{random.choice(starters)}")


def setup(bot):
    """ConversationStarters Cog load."""

    bot.add_cog(ConvoStarters(bot))
    log.info("ConversationStarters cog loaded")
