from aiogram.filters import Filter
from aiogram.types import Message

import config


class AllowedIdFilter(Filter):
    """
    Filter for Telegram bot to check whether user
    is able to interact with bot
    """

    def __init__(self):
        self.allowed_ids = config.ALLOWED_IDS

    async def __call__(self, message: Message) -> bool:
        """
        Filter checks whether the incoming message from user
        allowed to interact with the bot
        :param message: incoming message
        :return: true if user allowed to interact with bot, false otherwise
        """
        return message.from_user.id in self.allowed_ids
