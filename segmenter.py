#!/usr/bin/env python3

import sys
import argparse
from tokenizer import tokenize

def my_best_segmenter(token_list): 
    """ TODO: Replace this with an improved sentence segmenter. """
    pass

def baseline_segmenter(token_list):
    all_sentences = []
    this_sentence = []
    for token in token_list:
        this_sentence.append(token)
        if token in ['.', ':', ';', '!', '?']:
            all_sentences.append(this_sentence)
            this_sentence = []
    return all_sentences

def write_sentence_boundaries(sentence_list, out):
    """ TODO: Write out the token numbers of the sentence boundaries. """
    pass

def main(args):
    pass

if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description="Sentence Segmenter for NLP Lab")
    parser.add_argument('--textfile', "-t", metavar="FILE", type=argparse.FileType('r'),
                        required=True, help="Unlabled text is in FILE.")
    parser.add_argument("--hypothesis_file", "-y", metavar="FILE", type=argparse.FileType('w'),
                        required=False, default=sys.stdout,
                        help="Write hypothesized boundaries to FILE")
    args = parser.parse_args()
    main(args)

# Discover NLP course materials authored by Julie Medero, Xanda Schofield, and Richard Wicentowski
# This work is licensed under a Creative Commons Attribution-ShareAlike 2.0 Generic License# https://creativecommons.org/licenses/by-sa/2.0/
