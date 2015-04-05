#! /usr/bin/env python3

from parts_of_speech import word as w

class Adjective(w.Word):

    def __init__(self, wid, word, definition):
        (en, 
        (ett,
        plural,
        comparative,
        superlative,
        adj_eng,
        comparative_eng,
        superlative_eng,
        pic)) = (word, definition)

        forms = {
            'en':               {
                                'sv': en,
                                'en': adj_eng
                                },
            'ett':              {
                                'sv': ett,
                                'en': adj_eng
                                },
            'plural':           {
                                'sv': plural,
                                'en': adj_eng
                                },
            'comparative':      {
                                'sv': comparative,
                                'en': comparative_eng
                                },
            'superlative':      {
                                'sv': superlative,
                                'en': superlative_eng
                                }
        }

        w.Word.__init__(self, wid, word, forms, pic)
