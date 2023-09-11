# Paul Lawrence Z Sales
# Applicant: Data Engineer
# Solution summary:
# 1. Read the lines of the file
# 2. Extract the ZOP lines using regex from the previously extracted lines
# 3. Remove the 'ZOP' marker from the lines and print the poem
# 4. For the word stats. extract each word from the lines (tokenize, clean, normalize)
# 5. Use a dictionary to keep track of the occurrence of a word
# 6. Print the word stat

# NOTE: this assumes that the file input is in inputs/input.in
# This allows us to just use `python exam1.py` to run the file

import re

INPUT_FILE_PATH = 'inputs/input.in'


def count_word_stats(lines: list[str]):
    try:
        # keep track of the stat with a dictionary
        stat_dict = {}
        # extract each word
        for line in lines:
            tokens = line.split(' ')
            for token in tokens:
                # clean and normalize the word so that the == The
                stripped_token = token.strip('.!*').lower()
                if stripped_token in stat_dict:
                    stat_dict[stripped_token] += 1
                else:
                    stat_dict[stripped_token] = 1
        # sort by highest count first and only print the top five words
        sorted_words = sorted(stat_dict.items(), key=lambda x: x[1], reverse=True)
        for word, count in sorted_words[:5]:
            # use .ljust() to format printing
            print(f'{word.ljust(5)}\t\t:\t{count}')
    except:
        print('countWordStats error')


def zen_of_python(file):
    try:
        zop_lines_arr = []
        # Open the file and read its contents line by line
        with open(file, 'r') as opened_file:
            content = opened_file.readlines()
            # print(content)
        # read each line
        for line in content:
            # use re.findAll to find all ZOP lines
            # figuring out the regex pattern was really challenging!
            pattern = r'\bZOP.*?[.!]'
            zop_lines: list[str] = re.findall(pattern, line)

            # left strip the ZOP marker to extract just the line
            for zls in zop_lines:
                zop_lines_arr.append(zls.lstrip('ZOP '))

        # print ZOP
        print('\n'.join(zop_lines_arr))

        # Print the top 5 words
        print('\nTOP 5 WORDS')
        count_word_stats(zop_lines_arr)
    except:
        print('zen_of_python error')


if __name__ == '__main__':
    zen_of_python(INPUT_FILE_PATH)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
