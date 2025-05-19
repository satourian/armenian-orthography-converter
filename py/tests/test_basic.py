import json, re, pathlib
import unittest
from py import converter

def load_js_data(path):
    text = pathlib.Path(path).read_text(encoding='utf-8')
    text = re.sub(r'^module\.exports\s*=\s*', '', text)
    text = re.sub(r';\s*$', '', text.strip())
    return json.loads(text)

words = load_js_data('test/data/test1.js')[:50]

class TestRoundtrip(unittest.TestCase):
    def test_roundtrip(self):
        for pair in words:
            modern = pair['modern']
            traditional = pair['traditional']
            self.assertEqual(converter.mashtots_to_soviet(traditional), modern)
            self.assertEqual(converter.soviet_to_mashtots(modern), traditional)

if __name__ == '__main__':
    unittest.main()
