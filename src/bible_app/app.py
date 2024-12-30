from taipy.gui import Gui, notify, State
from .bible_service import BibleService
from .config import PAGE_LAYOUT

class BibleApp:
    def __init__(self):
        self.bible_service = BibleService()
        self.search_query = ""
        self.search_results = "Results will appear here..."

    def search_bible(self, state, query):
        if not query:
            return "Please enter a search term"
        
        results = self.bible_service.search(query)
        if not results:
            return "No results found"
        
        state.search_results = "\n\n".join(results[:5])
        notify(state, 'info', f"Found {len(results)} results")

def create_app():
    app = BibleApp()
    gui = Gui(PAGE_LAYOUT)
    return gui