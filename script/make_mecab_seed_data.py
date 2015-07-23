#!/usr/bin/env python
# encoding: utf-8

import codecs
import sys

def make_mecab_seed_data(input_file, output_file):
    input_data = codecs.open(input_file, 'r', 'utf-8')
    output_data = codecs.open(output_file, 'w', 'utf-8')
    for line in input_data.readlines():
        word = line.strip()
        output_data.write(word + ",0,0,0,0,0,0\n")
    input_data.close()
    output_data.close()

if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.exit()

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    make_mecab_seed_data(input_file, output_file)
