import argparse
import collections
import re


WORD_QUANTITY = 10


def get_commandline_arguments():
    parser = argparse.ArgumentParser(description='Get the link to json file.')
    parser.add_argument('filepath', type=str)
    return parser.parse_args()


def load_data(filepath):
    with open(filepath) as text_file:
        filedata = text_file.read()
    return filedata


def get_most_frequent_words(raw_text):
    frequency_list = collections.Counter()
    match_pattern = re.findall(r'\b[a-я]{4,25}\b', raw_text.lower())
    for word in match_pattern:
        frequency_list[word] += 1
    return frequency_list

if __name__ == '__main__':
    print('Parsing text...')
    try:
        raw_text = load_data(get_commandline_arguments().filepath)
    except (FileNotFoundError):
        exit('File is missing.')
    print('The most frequent words in file are:')
    for word in get_most_frequent_words(raw_text).most_common(WORD_QUANTITY):
        print(word)
