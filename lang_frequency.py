import argparse
import re
from collections import Counter


def get_commandline_arguments():
    parser = argparse.ArgumentParser(description='Get the link to json file.')
    parser.add_argument('filepath', type=str)
    return parser.parse_args()


def load_data(filepath):
    with open(filepath) as text_file:
        filedata = text_file.read()
    return filedata


def get_most_frequent_words(raw_text):
    match_pattern = re.findall(r'\b[a-я]{4,}\b', raw_text.lower())
    return Counter(match_pattern)


if __name__ == '__main__':
    word_quantity = 10
    try:
        raw_text = load_data(get_commandline_arguments().filepath)
        print('Parsing text...')
    except (FileNotFoundError):
        exit('File is missing.')
    print('The most frequent words in file are:')
    for word in get_most_frequent_words(raw_text).most_common(word_quantity):
        print(word[0], '-', word[1])
