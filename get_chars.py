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


def main():
    corpus = '../../git_projects/partree/corpus'
    # get all files in corpus
    files = file_finder(corpus)
    # get all chars in all files
    chars = []
    for i in files:
        # open file
        with open(i) as f:
            lines = f.readlines()
        # get Sinhala text
        sin_text = [x.split('\t')[1] for x in lines]
        # save all (unique) characters
        for line in sin_text:
            # split into chars (only add non-ASCII chars)
            local_chars = [x for x in line if not x.isascii()]
            # add to main list
            chars.extend(local_chars)
    # unique chars
    chars = set(chars)
    # print(len(chars))

    # save to file
    with open('chars.csv', 'w') as csv_file:
        # write to file
        writer = csv.writer(csv_file)
        writer.writerow(['sinhala', 'latin'])
        for i in chars:
            writer.writerow([i, ''])
    return


if __name__ == '__main__':
    main()
