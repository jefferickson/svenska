#! /usr/bin/env python3

import csv
import sys
import argparse
import shelve

# Import our parts of speech classes
sys.path.append('..')
import parts_of_speech as pos


class Svenska_Parser:
    '''This is the main parser class. It can read CSV word lists and create word objects.'''

    # Class attrs
    ## key for word list in a shelve
    key_word_list = 'word_list'

    def __init__(self, dispatcher_override = None):
        self.parsed_words = {}
        self.words_from_shelve = {}
        
        if not dispatcher_override:
            self.dispatcher = {
                'adj':      pos.adjective.Adjective,
                'adv':      pos.adverb.Adverb,
                'sent adv': pos.adverb.Adverb,
                'en':       pos.noun.En,
                'ett':      pos.noun.Ett,
                'verb':     pos.verb.Verb,
                'word':     pos.word.Word
            }
        else:
            self.dispatcher = dispatcher_override

    def parse_word_list(self, files, delimiter = ','):
        '''For each line in each file, dispatch to proper class definition.'''

        for a_file in files:
            with open(a_file, 'r') as f:
                reader = csv.reader(f, delimiter = delimiter)
                for row in reader:
                    wid, part_of_speech, word, *definition = row
                    if row[0][0] == '#': continue # skip comments
                    self.parsed_words.setdefault(word, []).append(self.dispatcher[part_of_speech](wid, word, definition))

    def shelve_word_list(self, shelve_file):
        '''Shelve the parsed word list.'''

        with shelve.open(shelve_file, 'c') as shelf:
            shelf[self.key_word_list] = self.parsed_words

    def unshelve_word_list(self, shelve_file):
        '''Un-shelve word objects from file.'''

        with shelve.open(shelve_file, 'r') as shelf:
            self.words_from_shelve = shelf[self.key_word_list]


if __name__ == '__main__':

    args = argparse.ArgumentParser()
    args.add_argument('-w', '--parse-word-list', help = 'Word list(s) to process.', action = 'store_true')
    args.add_argument('-o', help = 'Output file.', default = None)
    args.add_argument('files', nargs = '+', default = None)

    cmd_line_args = args.parse_args()

    # If files exist to be parsed, let's parse them
    if cmd_line_args.parse_word_list:
        parser = Svenska_Parser()
        parser.parse_word_list(cmd_line_args.files)
        # And if an output file is specified, let's store the shelve of parsed words there
        if cmd_line_args.o:
            parser.shelve_word_list(cmd_line_args.o)
