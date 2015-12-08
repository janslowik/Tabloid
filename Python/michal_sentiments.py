# -*- coding: utf-8 -*-
import string
import os
import csv
import argparse



def read_file(name):
    with open(name, 'r') as f:
        raw_text = f.read()
        return raw_text


def write_results_file(output_file_name, results_list):
    with open(output_file_name, 'wb') as results_file:
        result_writer = csv.writer(results_file)
        for row in results_list:
            result_writer.writerow(row)


def program(working_directory, output_file_name, tabloid_list_name, not_tabloid_list_name):
    # the fastest way to strip punctuation from string in python
    # http://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python
    table = string.maketrans("", "")

    results_list = []

    with open(tabloid_list_name, 'rb') as f:
        reader = csv.reader(f)
        tabloid_words = [item for sublist in list(reader) for item in sublist]

    with open(not_tabloid_list_name, 'rb') as f:
        reader = csv.reader(f)
        not_tabloid_words = [item for sublist in list(reader) for item in sublist]

    for file in os.listdir(working_directory):

        if file.endswith(".txt.bas"):

            raw_text = read_file('/'.join([working_directory, file]))
            text_without_punctuation = raw_text.translate(table, string.punctuation)
            words = text_without_punctuation.split()

            tabloid_counter = 0
            not_tabloid_counter = 0
            for word in words:
                if word in tabloid_words:
                    tabloid_counter += 1
                elif word in not_tabloid_words:
                    not_tabloid_counter += 1

            uid = file.replace('.txt.bas', '')
            row = [int(uid), len(words), tabloid_counter, not_tabloid_counter]
            results_list.append(row)

    write_results_file(output_file_name, results_list)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-wd', '--working_directory',
                        help='the working directory which contains raw article files to analyze', required=True)
    parser.add_argument('-o', '--output_file', help='the name of output file', required=True)
    parser.add_argument('-t', '--tabloid_list', help='tabloid list of key words', required=True)
    parser.add_argument('-nt', '--not_tabloid_list', help='not tabloid list of key words', required=True)
    args = parser.parse_args()
    program(working_directory=args.working_directory, output_file_name=args.output_file, tabloid_list_name=args.tabloid_list,
            not_tabloid_list_name=args.not_tabloid_list)
