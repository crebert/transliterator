import unittest
import translit


class TranslitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.transliterator = translit.Transliterator('ben')

    def test_diacritic(self):
        self.assertEqual(self.transliterator.convert('জি'), 'ji')

    def test_longstring(self):
        s = 'এটাকে অন্ধকার দেখাচ্ছে যেন ভূতুড়ে জাহাজের মত'
        self.assertEqual(self.transliterator.convert(s), 'ēṭākē andhakāra dēkhācchē yēna bhūtuṛē jāhājēra mata')


if __name__ == '__main__':
    unittest.main()
