#! /usr/bin/env python3

from word import Word

class Noun(Word):

    def __init__(self, word, gender, definition):
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

        Word.__init__(self, word, forms, pic)


class En(Noun):

    def __init__(self, word, definition):
        Noun.__init__(self, word, 'en', definition)


class Ett(Noun):

    def __init__(self, word, definition):
        Noun.__init__(self, word, 'ett', definition)
