import csv
import os


def file_finder(path: str, lang: str):
    """
    list of all monotext files in corpus with given language code
    :param path: path name to corpus files
    :param lang: 3-digit language isocode
    :return: list
    """
    all_files = []
    movies = [i for i in os.listdir(path) if not i.startswith('.')]
    for dirs in movies:
        local_path = os.path.join(path, dirs, 'monotext')
        monotext_files = [i for i in os.listdir(local_path) if i.endswith(lang + '.monotext.txt')]
        files_full_path = [os.path.join(local_path, x) for x in monotext_files]
        all_files.extend(files_full_path)
    return all_files


def main():
    corpus = '../../git_projects/partree/corpus'
    # language code
    lang = 'ben'
    # get all files in corpus
    files = file_finder(corpus, lang=lang)
    # get all chars in all files
    chars = []
    for i in files:
        # open file
        with open(i) as f:
            lines = f.readlines()
        # get text (second column in tab separated file)
        text = [x.split('\t')[1] for x in lines]
        # save all (unique) characters
        for line in text:
            # split into chars (only add non-ASCII chars)
            local_chars = [x for x in line if not x.isascii()]
            # add to main list
            chars.extend(local_chars)
    # unique chars
    chars = set(chars)
    # print(len(chars))

    # save to file
    with open(f"{lang}_conversiontable.csv", 'w') as csv_file:
        # write to filse
        writer = csv.writer(csv_file)
        writer.writerow(['native', 'latin'])
        for i in chars:
            writer.writerow([i, ''])
    return


if __name__ == '__main__':
    main()
