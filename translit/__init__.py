import importlib


def load_conversion_table(language):
    """
    load conversion table from language module
    :param language: 3-digit language iso-code
    :return: dict conversion table
    """
    try:
        i = importlib.import_module(f"lang.{language}")
        ct = i.conversion_table
    except ImportError:
        print('No module found for language {}'.format(language))
        ct = {}
    return ct


def precedes_diacritic(char_i, string):
    """
    Does this character precede a diacritic that requires to delete a final vowel?
    :param char_i: index of the character in string
    :param string: larger string
    :return: boolean
    """

    # assume the next character is not a diacritic
    is_diacritic = False

    # test if there is a next character in string that is a diacritic
    if len(string) - 1 > char_i:
        next_char = string[char_i + 1]
        is_diacritic = next_char['char_type'] == 'diacritic'
    return is_diacritic


class Transliterator:
    def __init__(self, language: str):
        self.language = language
        self.conversion_table = load_conversion_table(language)

    def __str__(self):
        return f"Transliteration tool for language: {self.language}"

    def convert(self, x: str):
        """
        convert string to Latin alphabet
        :param x: string
        :return: string
        """

        # replace each character with dictionary from conversion table if possible
        new_chars = [self.conversion_table.get(i) if i in self.conversion_table.keys() else {'char': i, 'char_type': ''} for i in x]
        # refine transliteration (vowels!)

        # create a list to add converted characters
        converted_chars = []
        for i, j in enumerate(new_chars):
            if precedes_diacritic(i, new_chars) and j['char'].endswith('a'):
                # add converted character without final -a
                converted_chars.append(j['char'][:-1])
            else:
                # keep character as is
                converted_chars.append(j['char'])
        return ''.join(converted_chars)
