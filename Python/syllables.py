# -*- coding: utf-8 -*-
import string
import os
import csv
import argparse


def syllables(word):
    count = 0
    vowels = 'aeiouy'
    word = word.lower().strip(".:;?!")
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith('e'):
        count -= 1
    if word.endswith('le'):
        count += 1
    if count == 0:
        count += 1
    return count


def read_file(name):
    with open(name, 'r') as f:
        raw_text = f.read()
        return raw_text


def write_results_file(output_file_name, results_list):
    with open(output_file_name, 'wb') as results_file:
        result_writer = csv.writer(results_file)
        for row in results_list:
            result_writer.writerow(row)


def program(working_directory, output_file_name, threshold):
    results_list = []

    el

    for file in os.listdir(working_directory):

        if file.endswith(".txt"):
            raw_text = read_file('/'.join([working_directory, file]))
            text_without_punctuation = raw_text.translate(table, string.punctuation)
            words = text_without_punctuation.split()
            number_of_syllables_list = []
            for word in words:
                number_of_syllables_list.append(syllables(word))
            number_of_i_syllables_words = []
            for j in range(1, threshold):
                number_of_i_syllables_words.append(number_of_syllables_list.count(j))
            number_of_i_syllables_words.append(sum([number_of_syllables_list.count(j) for j in range(threshold, 11)]))
            uid = file.replace('.txt', '')
            row = [uid]
            row.extend(number_of_i_syllables_words)
            results_list.append(row)

    write_results_file(output_file_name, results_list)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-wd', '--working_directory',
                        help='the working directory which contains raw article files to analyze', required=True)
    parser.add_argument('-o', '--output_file', help='the name of output file', required=True)
    parser.add_argument('-t', '--threshold', help='syllabes threshold', type=int, required=True)
    args = parser.parse_args()
    program(working_directory=args.working_directory, output_file_name=args.output_file, threshold=args.threshold)
