export class BibleService {
  constructor(verses) {
    this.verses = verses;
  }

  search(query) {
    if (!query) return [];
    
    const regex = new RegExp(query, 'i');
    return this.verses.filter(verse => 
      regex.test(verse.text)
    ).map(verse => 
      `${verse.book} ${verse.chapter}:${verse.verse} - ${verse.text}`
    );
  }
}