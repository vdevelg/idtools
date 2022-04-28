from aiogram import Dispatcher, executor

import log
from init_bot import bot, dp, set_default_commands
from lang import phrase
import conf
import logic



logger = log.init_log(__file__)


async def on_startup(dp: Dispatcher):
    await set_default_commands(dp)
    message_text = phrase('f-run')
    logger.info(message_text)
    await bot.send_message(conf.ADMIN_TG_ID, message_text)


async def on_shutdown(dp: Dispatcher):
    message_text = phrase('f-stop')
    logger.info(message_text)
    await bot.send_message(conf.ADMIN_TG_ID, message_text)



if __name__ == '__main__':
    executor.start_polling(
        dp,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown)
