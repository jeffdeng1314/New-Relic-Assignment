# 100 most common three-word sequences

import os
import sys
import string
import re

# referrence https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string
REGEX = re.compile('[%s]' % re.escape(string.punctuation))


# accept input as files or line-by-line from pipe
def main():

    # process stdin
    if not sys.argv[1::] or len(sys.argv[1::]) == 0:

        # process the stdin from pipe if it's not referring to terminal inputs
        if not sys.stdin.isatty():
            print('>>>>>>> Process from stdin <<<<<<<')
            parse_and_print(sys.stdin.read())
        else:
            print('No input detected')
            exit(-1)

    # process the file/s from argument
    else:
        for f in sys.argv[1::]:
            print(f'>>>>>>> {f} <<<<<<<')
            parse_and_print(process_file(f))


# # reads from the stdin and print out the list of common sequences
# def process_stdin(buff):


# reads from a file and returns a string
def process_file(target):
    with open(target, 'r') as f:
        s = ''

        # storing the file content to a string variable in case of a large file
        for line in f:
            s += line
    return s

# takes in the string data, parse it, and print out the list of common sequences


def parse_and_print(data):
    dictionary = {}

    matches = find_matches_as_list(data)
    dictionary = get_map_of_all_content(matches)
    print_result(dictionary)


# takes in a string of text and returns a list of valid words
def find_matches_as_list(line):
    matches = []

    # removing punctuactions from a string using regular expression
    res = REGEX.sub('', line)

    # append each word from the string after removing white spaces
    for word in res.split():
        matches.append(word.lower())

    return matches


# takes in a list of valid words and returns a dictionary/map of phrases with count as value
def get_map_of_all_content(matches):
    d = {}

    # insert the current word and the next two words as a key and their occurrences to the dictionary/map
    for i in range(0, len(matches)-2):
        phrase = get_phrase(matches[i], matches[i+1], matches[i+2])

        try:
            d[phrase] += 1
        except:
            d[phrase] = 1

    return d


# takes in three strings and returns a combined string with spaces in between
def get_phrase(first, second, third):
    return first + ' ' + second + ' ' + third


# takes in a dictionary/map and prints out the first 100 most common three word sequences to the screen
def print_result(d):
    if len(d) > 0:
        counter = 100

        # sorts the dictionary in descending order based on its value (number of appearances)
        sorted_by_values = sorted(d, key=d.get, reverse=True)

        print('Phrase                      | Count')
        print('-------------------------------------')

        for key in sorted_by_values:
            if counter == 0:
                break

            print(f"{key:30s} {d[key]}")

            counter -= 1

        print('-------------------------------------\n')

    else:
        print('-------------------------------------')
        print('No three-word sequences found')
        print('-------------------------------------\n')


if __name__ == '__main__':
    main()
