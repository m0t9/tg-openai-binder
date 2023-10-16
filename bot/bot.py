import typing

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

import config
import openai_api
from bot.filters import AllowedIdFilter

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher()

user_contexts: typing.Dict[int, openai_api.Model]
user_contexts = dict()


@dp.message(CommandStart(), AllowedIdFilter())
async def start_respond(message: Message) -> None:
    """
    Handler for '/start' commands
    :param message: message object
    :return: None
    """
    await message.answer(config.START_PLACEHOLDER)


@dp.message(Command('delete_context'))
async def clear_context(message: Message) -> None:
    await message.answer(config.CLEAR_CONTEXT_ANSWER)
    if message.from_user.id in user_contexts:
        user_contexts.pop(message.from_user.id)


@dp.message(AllowedIdFilter())
async def query_respond(message: Message) -> None:
    """
    Handler for ordinary user request
    Takes model with dialogue context, extends it and generates the answer.
    :param message: new incoming query to add to context
    :return: None
    """
    response = await message.answer(config.PLACEHOLDER)
    user_id = message.from_user.id

    if user_id not in user_contexts:
        user_contexts[user_id] = openai_api.Model()

    query = message.text
    answer = user_contexts[user_id].generate_answer(query)

    await bot.edit_message_text(answer, response.chat.id, response.message_id)


async def main() -> None:
    """
    Run the polling
    :return: None
    """
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
