#! /usr/bin/env python3

from parts_of_speech import word as w

class Verb(w.Word):

    def __init__(self, wid, word, definition):
        (infinitive, 
        (imperative,
        present_tense,
        past_tense,
        supine,
        infinitive_eng,
        past_tense_eng,
        past_participle_eng,
        pic)) = (word, definition)

        forms = {
            'imperative':       {
                                'sv': imperative + '!',
                                'en': infinitive_eng + '!'
                                },
            'infinitive':       {
                                'sv': 'att ' + infinitive,
                                'en': 'to ' + infinitive_eng
                                },
            'present_tense':    {
                                'sv': present_tense,
                                'en': infinitive_eng + '((e)s)'
                                },
            'past_tense':       {
                                'sv': past_tense,
                                'en': past_tense_eng
                                },
            'supine':           {
                                'sv': supine,
                                'en': past_participle_eng
                                }
        }

        w.Word.__init__(self, wid, word, forms, pic)
