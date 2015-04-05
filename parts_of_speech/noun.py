#! /usr/bin/env python3

from parts_of_speech import word as w

class Noun(w.Word):

    def __init__(self, wid, word, gender, definition):
        (indef_singular, 
        (indef_plural,
        def_singular,
        def_plural,
        singular_eng,
        plural_eng,
        pic)) = (word, definition)

        forms = {
            'indef_singular':   {
                                'sv': gender + ' ' + indef_singular,
                                'en': 'a(n) ' + singular_eng
                                },
            'indef_plural':     {
                                'sv': indef_plural,
                                'en': plural_eng
                                },
            'def_singular':     {
                                'sv': def_singular,
                                'en': 'the ' + singular_eng
                                },
            'def_plural':       {
                                'sv': def_plural,
                                'en': 'the ' + plural_eng
                                }
        }

        w.Word.__init__(self, wid, word, forms, pic)


class En(Noun):

    def __init__(self, wid, word, definition):
        Noun.__init__(self, wid, word, 'en', definition)


class Ett(Noun):

    def __init__(self, wid, word, definition):
        Noun.__init__(self, wid, word, 'ett', definition)
