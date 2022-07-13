def print_as_dict(x):
    """
    print conversion table as dictionary
    :param x: file name (+ path)
    :return: None
    """
    # load conversion table from csv
    with open(x) as f:
        lines = f.readlines()
        # remove '\n'
        lines = [x.replace('\n', '') for x in lines]
        for x in lines[1:]:
            try:
                native, lat, char_type = x.split(',')
            except ValueError:
                if x.count(',') >= 1:
                    native, lat = x.split(',')
                    char_type = ''
                else:
                    native = x
                    lat = ''
                    char_type = ''
            print(f"'{native}': {{'char': '{lat}', 'char_type': '{char_type}'}},")
    return


def main():
    print_as_dict('mapping/ben_conversiontable.csv')


if __name__ == '__main__':
    main()

