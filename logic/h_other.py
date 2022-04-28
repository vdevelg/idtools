from aiogram import types
from aiogram.dispatcher import filters

import log
from init_bot import dp
from lang import phrase
import conf



logger = log.get_logger(__file__)


@dp.message_handler(filters.Text(startswith=conf.TG_COMM_PREFIX))
async def get_answer_to_unknown_commands(message: types.Message):
    await message.reply(
        phrase('f-unknown_command', message.from_user.language_code))


@dp.message_handler()
async def get_answer_to_unknown_text(message: types.Message):
    await message.reply(
        phrase('f-unknown_text', message.from_user.language_code))
