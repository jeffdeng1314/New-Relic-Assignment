# 100 most common three-word sequences

import os
import sys
import string
import re

# referrence https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string
REGEX = re.compile('[%s]' % re.escape(string.punctuation))

# accept inpurt as files or line-by-line


def main():

    # process stdin
    if not sys.argv[1::] or len(sys.argv[1::]) == 0:

        # checks if the stdin is not referring to terminal input
        if not sys.stdin.isatty():
            process_stdin(sys.stdin)
        else:
            print('No input detected')
            exit(-1)

    # process the file/s from argument
    else:
        for f in sys.argv[1::]:
            process_file(f)


# def process_stdin(buff):

def process_file(target):
    dictionary = {}

    with open(target, 'r') as f:
        s = ''

        for line in f:
            s += line
            # print(s)

    matches = find_matches_as_list(s)
    dictionary = get_map_of_all_content(matches)
    print_result(dictionary)


# process the text and return the valid words as a list


def find_matches_as_list(line):
    matches = []

    res = REGEX.sub('', line)

    for word in res.split():
        matches.append(word.lower())

    return matches


def get_map_of_all_content(matches):
    d = {}
    for i in range(0, len(matches)-2):
        phrase = get_phrase(matches[i], matches[i+1], matches[i+2])

        try:
            d[phrase] += 1
        except:
            d[phrase] = 1

    return d


def get_phrase(first, second, third):
    return first + ' ' + second + ' ' + third


def print_result(d):
    if len(d) > 0:
        counter = 100

        sorted_by_values = sorted(d, key=d.get, reverse=True)

        print('Phrase                           | Count')
        print('----------------------------------------')

        for key in sorted_by_values:
            if counter == 0:
                break

            print(f"{key:30s} {d[key]}")

            counter -= 1

        print('----------------------------------------\n')

    else:
        print('----------------------------------------')
        print('No three-word sequences found')
        print('----------------------------------------\n')


if __name__ == '__main__':
    main()
