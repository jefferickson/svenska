#! /usr/bin/env python3


import csv
import sys
import argparse

sys.path.append('./parts_of_speech/')
import adjective as adj
import adverb as adv
import noun
import verb
import word


class Svenska_Parser:

    def __init__(self, dispatcher_override = None):
        
        if not dispatcher_override:
            self.dispatcher = {
                'adj': adj.Adjective,
                'adv': adv.Adverb,
                'sent adv': adv.Adverb,
                'en': noun.En,
                'ett': noun.Ett,
                'verb': verb.Verb,
                'word': word.Word
            }
        else:
            self.dispatcher = dispatcher_override

    def parse_word_list(self, files, delimiter = ','):
        '''For each line in each file, dispatch to proper class definition.'''
        self.parsed_words = {}

        for a_file in files:
            with open(a_file, 'r') as f:
                reader = csv.reader(f, delimiter = delimiter)
                for row in reader:
                    part_of_speech, word, *definition = row
                    if row[0][0] == '#': continue # skip comments
                    self.parsed_words.setdefault(word, []).append(self.dispatcher[part_of_speech](word, definition))


if __name__ == '__main__':

    args = argparse.ArgumentParser()
    args.add_argument('-w', '--parse-word-list', help = 'Word list(s) to process.', action = 'store_true')
    args.add_argument('-o', help = 'Output file.', default = None)
    args.add_argument('files', nargs = '+', default = None)

    cmd_line_args = args.parse_args()

    if cmd_line_args.parse_word_list:
        parser = Svenska_Parser()
        parser.parse_word_list(cmd_line_args.files)

        print(parser.parsed_words)
