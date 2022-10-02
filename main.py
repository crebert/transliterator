import translit


def main():
    # create transliterator for Bengali (isocode)
    Transliterator = translit.Transliterator('ben')

    # show Latin character
    print(Transliterator.conversion_table['ত'])

    # show char_type (diacritic or non-diacritic)
    print(Transliterator.conversion_table['ত']['char_type'])

    # transliteration of a string
    ben_test = 'এটাকে অন্ধকার দেখাচ্ছে যেন ভূতুড়ে জাহাজের মত'
    ben_transliterated = Transliterator.convert(ben_test)
    print(ben_transliterated)
    return


if __name__ == '__main__':
    main()
