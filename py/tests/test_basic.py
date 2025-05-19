import json
import pathlib
import unittest

from py import converter


def load_data(path):
    text = pathlib.Path(path).read_text(encoding='utf-8')
    return json.loads(text)


DATA_PATH = pathlib.Path(__file__).resolve().parent / 'data' / 'test1.json'
words = load_data(DATA_PATH)[:50]

class TestRoundtrip(unittest.TestCase):
    def test_roundtrip(self):
        for pair in words:
            modern = pair['modern']
            traditional = pair['traditional']
            self.assertEqual(converter.mashtots_to_soviet(traditional), modern)
            self.assertEqual(converter.soviet_to_mashtots(modern), traditional)

if __name__ == '__main__':
    unittest.main()