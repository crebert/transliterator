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
        for i, char in enumerate(new_chars):
            # remove final '-a' if followed by vowel (vowels are written as diacritics)
            if i < len(new_chars) - 1 and new_chars[i + 1].get('char_type') is 'diacritic':
                if char.get('char')[-1] == 'a':
                    char['char'] = char.get('char')[:-1]
        return ''.join([i['char'] for i in new_chars])

