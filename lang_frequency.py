import argparse
import re
from collections import Counter


def get_commandline_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath')
    return parser.parse_args()


def load_data(filepath):
    with open(filepath) as text_file:
        filedata = text_file.read()
    return filedata


def get_most_frequent_words(raw_text):
    word_quantity = 10
    filtered_list = re.findall(r'\b[a-я]{4,}\b', raw_text.lower())
    return Counter(filtered_list).most_common(word_quantity)


if __name__ == '__main__':
    try:
        raw_text = load_data(get_commandline_arguments().filepath)
        print('Parsing text...')
    except (FileNotFoundError):
        exit('File is missing.')
    print('The most frequent words in file are:')
    for word, count in get_most_frequent_words(raw_text):
        print(word, '-', count)
