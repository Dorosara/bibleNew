import streamlit as st
from ..services.bible_service import BibleService

def render_search_section(bible_service: BibleService):
    st.header("Search the Bible")
    query = st.text_input("Enter your search term")
    
    if st.button("Search"):
        if not query:
            st.warning("Please enter a search term")
            return
            
        results = bible_service.search(query)
        if not results:
            st.info("No results found")
        else:
            st.success(f"Found {len(results)} results")
            for result in results[:5]:
                st.write(result)