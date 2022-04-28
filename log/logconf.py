import os
import json
import logging
import logging.config



APP_NAME = os.path.basename(os.getcwd())
LOG_SEP = '-==-'  # разделитель между частями записи в журнале


def namer(default_name):
    stem, suffix_num = os.path.splitext(default_name)
    stem_base, suffix_ext = os.path.splitext(stem)
    return f'{stem_base[:-1]}{suffix_num[1:]}.{suffix_ext[1:]}'


def init_log(file):
    main_file_stem = os.path.splitext(os.path.basename(file))[0]
    path_and_cur_file_stem = os.path.splitext(__file__)[0]
    with open(f'{path_and_cur_file_stem}.json', encoding='utf-8') as f:
        string = f.read().replace(r'{{app_name}}', APP_NAME)
    deserialized = json.loads(string)

    deserialized['formatters']['detailed']['format'] = \
        deserialized['formatters']['detailed']['format'].replace(r'{{sep}}', LOG_SEP)

    path_to_log_file = os.path.join(os.path.dirname(path_and_cur_file_stem), main_file_stem)
    deserialized['handlers']['file']['filename'] = \
        deserialized['handlers']['file']['filename'].replace(r'{{log_file}}', f'{path_to_log_file}_0.log')
    # print(json.dumps(deserialized, indent=4, ensure_ascii=False))

    logging.config.dictConfig(deserialized)
    logger = logging.getLogger(f'{APP_NAME}.{main_file_stem}')
    logger.parent.handlers[1].namer = namer
    return logger


def get_logger(file):
    file_stem = os.path.splitext(os.path.basename(file))[0]
    logger = logging.getLogger(f'{APP_NAME}.{file_stem}')
    return logger
