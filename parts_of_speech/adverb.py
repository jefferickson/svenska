#! /usr/bin/env python3

from word import Word

class Adverb(Word):

    def __init__(self, word, definition):
        (adv, 
        (adv_eng,
        pic)) = (word, definition)

        forms = {
            'all':              {
                                'sv': adv,
                                'en': adv_eng
                                }
        }

        Word.__init__(self, word, forms, pic)
