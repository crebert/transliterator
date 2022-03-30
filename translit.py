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


def setup(diacrit_str='__X__'):
    conversion_table = {}
    with open('conversiontable.csv') as f:
        lines = f.readlines()
        for x in lines:
            sin, lat, char_type = x.split(',')
            if char_type.startswith('diacritic'):
                lat = diacrit_str + lat
            conversion_table[sin] = lat
    return conversion_table


def transliterate(x):
    return


def main():
    # marking diacritics (for vowels)
    diacrit = '__X__'
    # create conversion_table for transliteration
    conversion_table = setup(diacrit_str=diacrit)

    corpus = '../../git_projects/partree/corpus'
    # get all files in corpus
    files = file_finder(corpus)
    for fn in files:
        # open file
        with open(fn) as f:
            lines = f.readlines()
            # remove trailing '\n'
            lines = [x.replace('\n', '') for x in lines]
        # get Sinhala text (second column)
        sin_text = [x.split('\t')[1] for x in lines]
        sent_id = [x.split('\t')[0] for x in lines]
        new_text = []
        for line in sin_text:
            new_line = transliterate(line, conversion_table=conversion_table, diacrit_str=diacrit)
            new_text.append(new_line)

        file_base = os.path.basename(fn).split('.')[0]
        output_file = 'output/' + file_base + '.translit.txt'

        # save files
        with open(output_file, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['sinhala', 'latin'])
            for (id, text) in zip(sent_id, new_text):
                writer.writerow([id, text])

    return


def transliterate(text, conversion_table, diacrit_str):
    # split line into characters
    local_chars = [x for x in text]
    # transliterate (insert dictionaries)
    translit = [conversion_table.get(x) if x in conversion_table.keys() else x for x in local_chars]
    # refine transliteration (vowels!)
    new_chars = []
    for i, x in enumerate(translit):
        # remove final '-a' if followed by vowel (vowels are marked with '_')
        if i < len(translit) - 1 and translit[i+1].startswith('_'):
            if x[-1] == 'a':
                x = x[:-1]

        # remove diacrit_str from vowels (but do not remove single underscores)
        if len(x) > len(diacrit_str):
            x = x.replace(diacrit_str, '')
        new_chars.extend(x)
    return ''.join(new_chars)


if __name__ == '__main__':
    main()
