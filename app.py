from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Тойға шақыру 💍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
[data-testid="stHeader"], footer, #MainMenu {
    display: none !important;
}
[data-testid="stMainBlockContainer"] {
    padding: 0 !important;
    max-width: 100% !important;
}
iframe {
    width: 100%;
    height: 100dvh;
    border: none;
}
</style>
""", unsafe_allow_html=True)

html_file = Path(__file__).parent / "index.html"
components.html(
    html_file.read_text(encoding="utf-8"),
    height=900,
    scrolling=True
)
