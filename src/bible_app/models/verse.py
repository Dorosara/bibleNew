from dataclasses import dataclass

@dataclass
class Verse:
    book: str
    chapter: int
    verse: int
    text: str

    def format(self) -> str:
        return f"{self.book} {self.chapter}:{self.verse} - {self.text}"