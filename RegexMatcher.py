import re
import argparse
import sys
import pprint


def read_file_with_options(files, pattern, show_only_file_names,
                           should_print_lines):
    '''
        Reads files from the specified path.
        This sofware should be executed on the same path where the files are located.
    '''

    for file in files:
        with open(file, encoding='utf-8') as openedFile:
            if show_only_file_names:
                if has_a_matching_item(openedFile, pattern):
                    print(openedFile.name)
            else:
                pretty_print = pprint.PrettyPrinter()
                matching_lines_dictionary = get_all_matching_lines_from_file(
                    openedFile, pattern, should_print_lines)
                pretty_print.pprint(matching_lines_dictionary)


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
    return re.search(pattern, text) is not None


def get_all_matching_lines_from_file(file, pattern, should_print_line):
    matching_lines_dictionary = {}
    matching_lines_list = []

    if should_print_line:
        lineNumber = 0
        for line in file:
            lineNumber += 1
            if text_matches_pattern(line, pattern):
                tuple_with_line_number = (lineNumber, line.rstrip())
                matching_lines_list.append(tuple_with_line_number)
    else:
        for line in file:
            if text_matches_pattern(line, pattern):
                matching_lines_list.append(line.strip())

    matching_lines_dictionary[file.name] = matching_lines_list
    return matching_lines_dictionary


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('infiles', nargs='+', type=str,
                        help="The name of the files to be read")
    parser.add_argument('pattern', type=str,
                        help="The pattern to be matched")
    parser.add_argument("-l", help="Show only the names of the files that contain at least one matching line",
                        action="store_true")
    parser.add_argument("-n", help="Show also the number of the lines matching a pattern",
                        action="store_true")
    arguments = parser.parse_args()

    read_file_with_options(arguments.infiles, pattern=arguments.pattern,
                           show_only_file_names=arguments.l, should_print_lines=arguments.n)
