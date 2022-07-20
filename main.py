import translit


def main():
    Transliterator = translit.Transliterator('ben')

    print(Transliterator.conversion_table['ত'])
    ben_test = 'এটাকে অন্ধকার দেখাচ্ছে যেন ভূতুড়ে জাহাজের মত'
    ben_transliterated = Transliterator.convert(ben_test)
    print(ben_transliterated)
    print(Transliterator.conversion_table['ত']['char_type'])
    return


if __name__ == '__main__':
    main()
