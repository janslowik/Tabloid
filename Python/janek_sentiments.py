# -*- coding: utf-8 -*-
import string
import os
import csv
import argparse
from decimal import Decimal


def read_file(name):
    with open(name, 'r') as f:
        raw_text = f.read()
        return raw_text


def write_results_file(output_file_name, results_list):
    with open(output_file_name, 'wb') as results_file:
        result_writer = csv.writer(results_file)
        for row in results_list:
            result_writer.writerow(row)


def program(working_directory, output_file_name, feature_words_list_name):
    # the fastest way to strip punctuation from string in python
    # http://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python
    table = string.maketrans("", "")

    results_list = []

    with open(feature_words_list_name, 'rb') as f:
        reader = csv.reader(f)
        feature_words = list(reader)

    feature_words_dict = {}

    for rec in feature_words[1:]:
        feature_words_dict[rec[1]] = Decimal(rec[2])

    for file in os.listdir(working_directory):

        if file.endswith(".txt.bas"):

            raw_text = read_file('/'.join([working_directory, file]))
            text_without_punctuation = raw_text.translate(table, string.punctuation)
            words = text_without_punctuation.split()

            metrics = Decimal(0)
            for word in words:
                if word in feature_words_dict:
                    metrics += feature_words_dict[word]

            uid = file.replace('.txt.bas', '')
            row = [int(uid), "{:.9f}".format(metrics)]
            results_list.append(row)

    write_results_file(output_file_name, results_list)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-wd', '--working_directory',
                        help='the working directory which contains raw article files to analyze', required=True)
    parser.add_argument('-o', '--output_file', help='the name of output file', required=True)
    parser.add_argument('-f', '--feature_words_list', help='feature list of words', required=True)
    args = parser.parse_args()
    program(working_directory=args.working_directory, output_file_name=args.output_file,
            feature_words_list_name=args.feature_words_list)
