import os



DEFAULT_LANGUAGE = 'ru'
# путь к примеру файла перевода
FT_EXAMPLE = './assets/146 Финальный Перевод ENG.docx'
# бланк шаблона для перевода
BLANK_OF_TEMPLATE = './assets/blank_of_template_for_translate.docx'

TG_API_TOKEN = os.getenv('TG_API_TOKEN')
ADMIN_TG_ID = os.getenv('TG_ID_ADMIN')

TG_COMM_PREFIX = '/'  # префикс команд в Telegram
# префикс ключевых строк в языковых файлах "*.lang"
PHRASE_REFERENCE_PREFIXES = set( (TG_COMM_PREFIX, 'f-') )
COMM_AND_DESCRIPT_SEP = ' - '
