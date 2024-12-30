import streamlit as st
from ..services.bible_service import BibleService
from .components import render_search_section

def create_app():
    st.set_page_config(
        page_title="Bible Search App",
        page_icon="📖"
    )
    
    st.title("Bible Search App")
    
    bible_service = BibleService()
    render_search_section(bible_service)