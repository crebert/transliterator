import translit
import sys
import argparse
import langcodes


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '-i', help='input file')
    parser.add_argument('--output', '-o', help='output file', default="output.txt")
    parser.add_argument('--lang', '-l', help='3-digit language isocode', default="ben")
    parser.add_argument('--demo', '-d', help='print short demo', action='store_true', dest='demo')
    args = parser.parse_args()

    if args.demo:
        # run demo and return
        demo()
        return

    # setup Transliterator
    Transliterator = translit.Transliterator(args.lang)
    # open file
    with open(args.input, 'r') as f:
        content = f.read()

    # convert to Latin alphabet
    converted = Transliterator.convert(content)

    # save to file
    with open(args.output, 'w') as f:
        f.write(converted)

    return


def demo():
    # set language
    lang = 'ben'
    # get standard isocode and language name
    standard_isocode = langcodes.standardize_tag(lang)
    language = langcodes.Language.make(language=standard_isocode).display_name()
    print(f"Running demo for language {language} ({lang})\n")

    print("Step 1: Create Transliterator object with \n>>> Transliterator = translit.Transliterator(<lang>)\n")
    # create transliterator for Bengali (isocode)
    Transliterator = translit.Transliterator(lang)

    # show Latin character
    # print(Transliterator.conversion_table['ত'])

    # show char_type (diacritic or non-diacritic)
    # print(Transliterator.conversion_table['ত']['char_type'])

    # transliteration of a string
    print("Step 2: Convert string to Latin alphabet with  \n>>> Transliterator.convert(<test_string>)\n")
    ben_test = 'এটাকে অন্ধকার দেখাচ্ছে যেন ভূতুড়ে জাহাজের মত'
    ben_transliterated = Transliterator.convert(ben_test)
    print(f"Demo input: {ben_test}")
    print(f"Demo output: {ben_transliterated}\n")
    return


if __name__ == '__main__':
    main()
