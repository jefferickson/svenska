#! /usr/bin/env python3

from word import Word

class Adjective(Word):

    def __init__(self, word, definition):
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

        Word.__init__(self, word, forms, pic)
