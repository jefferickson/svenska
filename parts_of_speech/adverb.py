#! /usr/bin/env python3

from parts_of_speech import word as w

class Adverb(w.Word):

    def __init__(self, wid, word, definition):
        (adv, 
        (adv_eng,
        pic)) = (word, definition)

        forms = {
            'all':              {
                                'sv': adv,
                                'en': adv_eng
                                }
        }

        w.Word.__init__(self, wid, word, forms, pic)
