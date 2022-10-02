import unittest
import translit


class TranslitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.transliterator = translit.Transliterator('sin')

    def test_diacritic(self):
        self.assertEqual(self.transliterator.convert('වු'), 'vu')

    def test_longstring(self):
        s = 'මම නිදහස් වුණා.'
        self.assertEqual(self.transliterator.convert(s), 'mama nidahas vuṇā.')


if __name__ == '__main__':
    unittest.main()
