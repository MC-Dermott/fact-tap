"""Fact Tap on Streamlit.

The game itself is index.html. This page loads it into a Streamlit app so it can be
shared from streamlit.app, which school networks allow.
"""

from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Fact Tap", page_icon="🔢", layout="wide", initial_sidebar_state="collapsed")

# Hide Streamlit's header, menu and footer so the game fills the page
st.markdown(
    """
    <style>
      header[data-testid="stHeader"], footer, #MainMenu { display: none; }
      .block-container { padding-top: 0.5rem; padding-bottom: 0; max-width: 1000px; }
    </style>
    """,
    unsafe_allow_html=True,
)

GAME = (Path(__file__).parent / "index.html").read_text(encoding="utf-8")
components.html(GAME, height=1150, scrolling=True)
