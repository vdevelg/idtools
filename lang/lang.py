import os
from functools import reduce

import conf



class Langs():
    def __init__(self, prefixes):
        def dict_upd(cur_ref, next_ref):
            self.loc_texts[language_code][cur_ref[1]] = \
                ''.join( lines[ cur_ref[0] + 1 : next_ref[0] ] ).strip()
            return next_ref
        
        loc_suffix = '.lang'
        self.loc_texts = {}
        cur_dir = os.path.dirname(__file__)
        for name in os.listdir(cur_dir):
            if name.endswith(loc_suffix):
                language_code = name.replace(loc_suffix, '')
                self.loc_texts[language_code] = {}
                lang_file_path = os.path.join(cur_dir, name)
                with open(lang_file_path, encoding='utf-8') as f:
                    lines = f.readlines()
                keys = []
                for index, line in enumerate(lines):
                    if any( set( map(line.startswith, prefixes) ) ):
                        phrase_reference = line.split(
                            conf.COMM_AND_DESCRIPT_SEP)[0].strip()
                        if conf.COMM_AND_DESCRIPT_SEP in line:
                            command_description = line.split(
                                conf.COMM_AND_DESCRIPT_SEP)[1].strip()
                        else:
                            command_description = None
                        keys.append( (index,
                                      phrase_reference,
                                      command_description) )
                keys.append( (len(lines), None, None) )
                reduce(dict_upd, keys)
                self.loc_texts[language_code]['commands'] = [
                    (command_name, command_description)
                    for _, command_name, command_description
                    in keys
                    if command_description
                ]
    
    
    def get_phrase(self, *args, lang_code='ru'):
        phrase_reference = args[0]
        format_args = args[1:]
        raw = self.loc_texts.get(lang_code).get(phrase_reference)
        if isinstance(raw, str):
            phrase = raw.format(*format_args)
        else:
            phrase = raw
        return phrase


phrase = Langs(conf.PHRASE_REFERENCE_PREFIXES).get_phrase
