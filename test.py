# testing

import unittest
import solution
import os

EMPTY_FILE = 'text files/empty_file.txt'
SHORT_TEST = 'text files/short_test.txt'

target_phrase = '--hi, do you know!'


class TestSolution(unittest.TestCase):

    def test_get_map_of_all_content_with_empty_input(self):
        matches = solution.find_matches_as_list('')
        d = {}
        self.assertEqual(solution.get_map_of_all_content(matches), d)

    def test_get_map_of_all_content_with_a_phrase(self):
        d = {
            'hi do you': 1,
            'do you know': 1
        }

        matches = solution.find_matches_as_list(target_phrase)
        self.assertEqual(solution.get_map_of_all_content(matches), d)

    def test_find_matches_as_list_with_a_phrase(self):
        arr = ['hi', 'do', 'you', 'know']
        self.assertEqual(solution.find_matches_as_list(target_phrase), arr)

    def test_find_matches_as_list_with_punctuations(self):
        arr = []
        self.assertEqual(solution.find_matches_as_list("-*+/...,,''%$"), arr)

    def test_get_phrase(self):
        self.assertEqual(solution.get_phrase(
            'one', 'two', 'three'), 'one two three')

    def test_process_file_with_empty_file(self):
        self.assertEqual(solution.process_file(EMPTY_FILE), '')

    def test_process_file_with_a_file(self):
        self.assertEqual(solution.process_file(
            SHORT_TEST), '--hi, do you know!')


# runs the unittest main class
if __name__ == '__main__':
    unittest.main()
