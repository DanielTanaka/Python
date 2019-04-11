import re
import argparse
import sys


def read_file_with_options(*files, pattern, show_only_file_names, print_lines):
    '''
        Reads files from the specified path
        This sofware should be executed on the same path where the files are located.
    '''

    for file in files:
        with open(file, encoding='utf-8') as openedFile:
            if show_only_file_names:
                if has_a_matching_item(openedFile, pattern):
                    print(openedFile.name)
            else:
                default_file_reading(openedFile, pattern, print_lines)


def has_a_matching_item(file, pattern):
    '''
        This function reads a file passed as argument and check if it has at least one
        line matching to the given pattern. Then, the result will be returned
    '''

    line = file.readline()
    is_a_match = False
    while not is_a_match and line:
        is_a_match = text_matches_pattern(line, pattern)
        line = file.readline()

    return is_a_match


def text_matches_pattern(text, pattern):
    return bool(re.search(pattern, text))


def default_file_reading(file, pattern, should_print_line):
    print("Occurrences in file:", file.name)

    if should_print_line:
        lineNumber = 0
        for line in file:
            lineNumber += 1
            if text_matches_pattern(line, pattern):
                print('{:>4} {}'.format(lineNumber, line.rstrip()))
    else:
        for line in file:
            if text_matches_pattern(line, pattern):
                print('{:>4}'.format(line.rstrip()))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('infiles', nargs='?', type=str,
                        help="The name of the files to be read")
    parser.add_argument("-l", help="Show only the names of the files that contain at least one matching line",
                        action="store_true")
    parser.add_argument("-n", help="Show also the number of the lines matching a pattern",
                        action="store_true")
    arguments = parser.parse_args()

    read_file_with_options(arguments.infiles, pattern='hello',
                           show_only_file_names=arguments.l, print_lines=arguments.n)
