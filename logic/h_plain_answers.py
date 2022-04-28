from aiogram import types
from aiogram.dispatcher import filters

import log
from init_bot import bot, dp
from lang import phrase
import conf



logger = log.get_logger(__file__)


@dp.message_handler(filters.CommandStart())
async def start(message: types.Message):
    await message.answer(phrase('/start', message.from_user.language_code))


@dp.message_handler(filters.CommandHelp())
async def get_help(message: types.Message):
    await message.answer(phrase('/help', message.from_user.language_code))


@dp.message_handler(filters.Command(['ft_example']))
async def get_help(message: types.Message):
    with open(conf.FT_EXAMPLE, 'rb') as ft:
        await bot.send_document(
            message.from_user.id,
            document=ft,
            caption=phrase('/ft_example',
            message.from_user.language_code))


@dp.message_handler(filters.Command(['blank']))
async def get_help(message: types.Message):
    with open(conf.BLANK_OF_TEMPLATE, 'rb') as ft:
        await bot.send_document(
            message.from_user.id,
            document=ft,
            caption=phrase('/blank',
            message.from_user.language_code))
