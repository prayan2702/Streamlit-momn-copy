import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Portfolio", layout="wide")

# Define the pages in the app
pages = {
    "Momentum Ranking": "momn_streamlit_app.py",
    "Strategy Performance": "Strategy_performance.py",
    "Strategy Tearsheet": "strategy-tearsheet.py",
}

# Create a navigation bar
with st.sidebar:
    selected = option_menu("Portfolio", list(pages.keys()), 
        icons=['house', 'speedometer2','book'], menu_icon="cast", default_index=0)

# Run the selected page
if selected in pages:
    file = pages[selected]
    exec(open(file).read())
