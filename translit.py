import csv
import os


def file_finder(path):
    all_files = []
    movies = [i for i in os.listdir(path) if not i.startswith('.')]
    for dirs in movies:
        local_path = os.path.join(path, dirs, 'monotext')
        sin_files = [i for i in os.listdir(local_path) if i.endswith('_sin.monotext.txt')]
        files_full_path = [os.path.join(local_path, x) for x in sin_files]
        all_files.extend(files_full_path)
    return all_files


def setup_translit():
    conversion_table = {}
    with open('conversiontable.csv') as f:
        lines = f.readlines()
        for x in lines:
            sin, lat, ctype = x.split(',')
            ctype = ctype.replace('\n', '')
            conversion_table[sin] = {'latin': lat, 'char_type': ctype}
    return conversion_table


def transliterate(x):
    return


def main():
    # create conversion_table for transliteration
    conversion_table = setup_translit()
    print(conversion_table)

    corpus = '../../git_projects/partree/corpus'
    # get all files in corpus
    files = file_finder(corpus)
    for fn in files:
        # open file
        with open(fn) as f:
            lines = f.readlines()
        # get Sinhala text (second column)
        sin_text = [x.split('\t')[1] for x in lines]
        for line in sin_text:
            print(line)
            print(transliterate(line, conversion_table=conversion_table))
    return


def transliterate(text, conversion_table):
    # split line into characters
    local_chars = [x for x in text]
    # transliterate (insert dictionaries)
    translit = [conversion_table[x].get('latin') if x in conversion_table.keys() else x for x in local_chars]
    # refine transliteration (vowels!)
    new_chars = []
    for i, x in enumerate(translit):
        # remove final '-a' if followed by vowel
        if i < len(translit) - 1 and '_' in translit[i+1]:
            if x[-1] == 'a':
                x = x[:-1]

        # remove '_' from vowels (but do not remove single underscores)
        if len(x) > 1:
            x = x.replace('_', '')
        new_chars.extend(x)
    return ''.join(new_chars)


if __name__ == '__main__':
    main()
