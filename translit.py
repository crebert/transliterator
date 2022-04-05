import csv
import os


sin_table = {
    'ෞ': '__X__au',
    'ූ': '__X__ū',
    'ෲ': '__X__ṝ',
    'ී': '__X__ī',
    'ෘ': '__X__ṛ',
    'ේ': '__X__ē',
    'ෙ': '__X__e',
    'ො': '__X__o',
    'ෝ': '__X__ō',
    'ා': '__X__ā',
    'ු': '__X__u',
    'ෟ': '__X__ḷ',
    'ෑ': '__X__ǣ',
    'ි': '__X__i',
    'ෛ': '__X__ai',
    'ැ': '__X__æ',
    '්': '__X__',
    'ං': 'ṁ',
    'ඬ': 'n̆ḍa',
    'ඉ': 'i',
    'ඟ': 'n̆ga',
    'හ': 'ha',
    'ස': 'sa',
    'ඕ': 'ō',
    'උ': 'u',
    'ඈ': 'ǣ',
    'ඹ': 'm̆ba',
    'ර': 'ra',
    'ඡ': 'cha',
    'ත': 'ta',
    'ළ': 'ḷa',
    'ද': 'da',
    'ක': 'ka',
    'ෆ': 'fa',
    'ණ': 'ṇa',
    'ඔ': 'o',
    'ඌ': 'ū',
    'ට': 'ṭa',
    'ජ': 'ja',
    'ඨ': 'ṭha',
    'ම': 'ma',
    'ආ': 'ā',
    'ඛ': 'kha',
    'ල': 'la',
    'එ': 'e',
    'ග': 'ga',
    'ඊ': 'ī',
    'ඳ': 'n̆da',
    'ධ': 'dha',
    'ඥ': 'gna',
    'ඇ': 'æ',
    'ඵ': 'pha',
    'අ': 'a',
    'භ': 'bha',
    'ඝ': 'gha',
    'ඖ': 'au',
    'ය': 'ya',
    'ව': 'va',
    'ප': 'pa',
    'ෂ': 'ṣa',
    'ශ': 'śa',
    'ඩ': 'ḍa',
    'බ': 'ba',
    'ච': 'ca',
    'ථ': 'tha',
    'න': 'na',
    'ඒ': 'ē'
}


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


def main():
    # marking diacritics (for vowels)
    diacrit = '__X__'
    # create conversion_table for transliteration
    conversion_table = setup(diacrit_str=diacrit)
    # for x in conversion_table:
    #     # print dictionary
    #     line = "'{}': '{}',".format(x, conversion_table[x])
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
        output_file = 'output/' + file_base + '.translit.csv'

        # save files
        with open(output_file, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['id', 'sinhala', 'translit'])
            for (i, j, g) in zip(sent_id, sin_text, new_text):
                writer.writerow([i, j, g])

    return


def transliterate(text, conversion_table, diacrit_str):
    # split line into characters
    local_chars = [x for x in text]
    # transliterate (insert dictionaries)
    translit = [conversion_table.get(x) if x in conversion_table.keys() else x for x in local_chars]
    # refine transliteration (vowels!)
    new_chars = []
    for i, x in enumerate(translit):
        # remove final '-a' if followed by vowel (vowels are marked with diacrit_str)
        if i < len(translit) - 1 and translit[i+1].startswith(diacrit_str):
            if x[-1] == 'a':
                x = x[:-1]

        # remove diacrit_str from vowels
        x = x.replace(diacrit_str, '')
        new_chars.extend(x)
    return ''.join(new_chars)


if __name__ == '__main__':
    main()
