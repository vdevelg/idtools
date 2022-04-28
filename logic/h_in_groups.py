from aiogram import types
from aiogram.dispatcher import filters

import log
from init_bot import dp
from lang import phrase
# import conf



logger = log.get_logger(__file__)


@dp.message_handler(filters.ChatTypeFilter(types.ChatType.SUPERGROUP))
async def skip_groups(message: types.Message):
    await message.reply(
        phrase('f-err_skip_groups', message.from_user.language_code))
