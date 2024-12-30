import json
import re
from pathlib import Path
from typing import List
from ..models.verse import Verse

class BibleService:
    def __init__(self):
        self.verses = self._load_verses()
    
    def _load_verses(self) -> List[Verse]:
        data_file = Path(__file__).parent.parent / "data" / "bible.json"
        with open(data_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Verse(**verse) for verse in data['verses']]
    
    def search(self, query: str) -> List[str]:
        if not query:
            return []
            
        results = []
        for verse in self.verses:
            if re.search(query, verse.text, re.IGNORECASE):
                results.append(verse.format())
        return results