# -*- coding: utf-8 -*-
import string
import os
import csv
import argparse

list_of_punctuation_marks = [
    ',',
    ';',
    ':',
    '!',
    '?',
    '.',
    '"',
    '...'
]

def count_punctuations(raw_text):
    lp = []
    for i in list_of_punctuation_marks:
        lp.append(raw_text.count(i))
    return lp


def read_file(name):
    with open(name, 'r') as f:
        raw_text = f.read()
        return raw_text


def write_results_file(output_file_name, results_list):
    with open(output_file_name, 'wb') as results_file:
        result_writer = csv.writer(results_file)
        for row in results_list:
            result_writer.writerow(row)


def program(working_directory, output_file_name):
    results_list = []


    for file in os.listdir(working_directory):

        if file.endswith(".txt"):
            raw_text = read_file('/'.join([working_directory, file]))
            punctuations_statistics = count_punctuations(raw_text)
            uid = file.replace('.txt', '')
            row = [uid]
            row.extend(punctuations_statistics)
            results_list.append(row)

    write_results_file(output_file_name, results_list)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-wd', '--working_directory',
                        help='the working directory which contains raw article files to analyze', required=True)
    parser.add_argument('-o', '--output_file', help='the name of output file', required=True)
    args = parser.parse_args()
    program(working_directory=args.working_directory, output_file_name=args.output_file)
