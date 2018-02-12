import argparse
import operator
import re


def get_commandline_arguments():
    parser = argparse.ArgumentParser(description='Get the link to json file.')
    parser.add_argument('filepath', type=str)
    return parser.parse_args()


def load_data(filepath):
    with open(filepath) as text_file:
        filedata = text_file.read()
    return filedata


def get_most_frequent_words(raw_text):
    frequency = {}
    match_pattern = re.findall(r'\b[a-я]{4,25}\b', raw_text.lower())
    for word in match_pattern:
        count = frequency.get(word, 0)
        frequency[word] = count + 1
    frequency_list = sorted(
                            frequency.items(),
                            key=operator.itemgetter(1),
                            reverse=True
    )
    return frequency_list

if __name__ == '__main__':
    print('Parsing text...')
    try:
        raw_text = load_data(get_commandline_arguments().filepath)
    except (FileNotFoundError):
        exit('File is missing.')
    print('The most frequent words in file are:')
    for word in get_most_frequent_words(raw_text)[0:10]:
        print(word)
