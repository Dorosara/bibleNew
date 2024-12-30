import json
import re
from pathlib import Path

class BibleService:
    def __init__(self):
        self.bible_data = self._load_bible_data()

    def _load_bible_data(self):
        data_file = Path(__file__).parent / "data" / "bible.json"
        with open(data_file, 'r', encoding='utf-8') as f:
            return json.load(f)['verses']

    def search(self, query):
        results = []
        for verse in self.bible_data:
            if re.search(query, verse['text'], re.IGNORECASE):
                results.append(
                    f"{verse['book']} {verse['chapter']}:{verse['verse']} - {verse['text']}"
                )
        return results