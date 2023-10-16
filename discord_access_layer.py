"""
    A layer to encapsulate the interactions with the discord API
"""

import discord
from logger import Logger


class DiscordAccessLayer:

    def __init__(self, token, verbose):

        # intents
        intents = discord.Intents.default()
        intents.typing = False
        intents.presences = False

        # set the fields up
        self._bot = discord.Client(intents)  # maybe use commands.Bot as Alan?
        self._token = token
        self.prefix = "!"
        self.roles = []  # TODO
        self.commands = {}
        self.logger = Logger(verbose=verbose)

        # events handling
        @self._bot.event
        async def on_ready():
            self.logger.info(f"The bot is connected and ready to run")

        @self._bot.event
        async def on_message(message):
            if message.author == self._bot.user:
                return  # Ignore messages from the bot itself
            if message.content.startswith(self.prefix):
                await self.handle_command(message)

    def enter(self):
        self.logger.info(f"Running the bot. username: {self._bot.user.name}")
        self._bot.run(self._token)

    def send_message(self, message, channel_id):
        channel = self._bot.get_channel(channel_id)
        if channel:
            self._bot.loop.create_task(channel.send(message))
        else:
            self.logger.error(f"There is no channel with ID {channel_id}")

    def exit(self):
        self.logger.info("Closing the bot.")
        self._bot.close()

    async def handle_command(message):
        raise NotImplementedError()  # TODO


def discord_ctx(token, verbose):
    bot = DiscordAccessLayer(token, verbose)
    bot.enter()
    yield bot
    bot.exit()
