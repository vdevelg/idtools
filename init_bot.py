from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from lang import phrase
import conf



bot = Bot(token=conf.TG_API_TOKEN, parse_mode=types.ParseMode.HTML)

ram_storage = MemoryStorage()
dp = Dispatcher(bot, storage=ram_storage)


async def set_default_commands(dp: Dispatcher):
    commands = phrase('commands', lang_code=conf.DEFAULT_LANGUAGE)
    default_commands = []
    for command_name, command_description in commands:
        default_commands.append(
            types.BotCommand(command_name, command_description))
    await dp.bot.set_my_commands(default_commands)
