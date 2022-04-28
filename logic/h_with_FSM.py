import io

from aiogram import types
from aiogram.dispatcher import filters, FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

import log
from init_bot import bot, dp
from lang import phrase
# import conf
from logic.class_Subs import Subs



logger = log.get_logger(__file__)


class File(StatesGroup):
    sending = State()  # состояние ожидания отправки файла


@dp.message_handler(filters.Command(['send']))
async def send(message: types.Message):
    await message.answer(phrase('/send',
        lang_code=message.from_user.language_code))
    await File.sending.set()


@dp.message_handler(filters.Command(['cancel', 'отмена'], ignore_case=True),
                    state='*')
@dp.message_handler(filters.Text(['cancel', 'отмена'], ignore_case=True),
                    state='*')
async def cancel_sending(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state:
        # Сброс конечного автомата
        await state.finish()
        # Сообщение пользователю об отмене и
        # удаление клавиатуры (на всякий случай)
        await message.answer(phrase('/cancel',
            lang_code=message.from_user.language_code),
            reply_markup=types.ReplyKeyboardRemove())
    else:
        await message.reply(phrase('f-err_not_in_state',
            lang_code=message.from_user.language_code))


@dp.message_handler(content_types=[types.ContentType.DOCUMENT],
                    state=File.sending)
async def convert_and_send_srt(message: types.Message, state: FSMContext):
    final_translation = io.BytesIO()
    await message.document.download(destination_file=final_translation)
    
    subs = Subs()
    try:
        subs.parse_ft_file(final_translation)
        final_translation.close()
    except Exception as exception_instance:
        main_part = phrase(*exception_instance.args,
                           lang_code=message.from_user.language_code)
        addendum = phrase('f-err_cnv_add',
                          lang_code=message.from_user.language_code)
        await message.answer('\n'.join([main_part, addendum]))
        return
    
    subtitles_translation = subs.compose_srt_file()
    
    await bot.send_document(message.from_user.id,
        document=subtitles_translation,
        caption=phrase('f-send_srt',
            lang_code=message.from_user.language_code))
    subtitles_translation.close()
    await state.finish()


@dp.message_handler(state=File.sending)
async def in_send_mode(message: types.Message, state: FSMContext):
    await message.answer(phrase('f-in_send_mode',
        lang_code=message.from_user.language_code))
