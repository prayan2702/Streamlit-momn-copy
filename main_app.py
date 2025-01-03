import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Portfolio", layout="wide")

# Define the pages in the app (use page titles directly)
pages = {
    "Momentum Ranking": "momentum_ranking",  # Page title as it appears in the navbar
    "Strategy Performance": "strategy_performance",
    "Strategy Tearsheet": "strategy_tearsheet",
}

# Create a navigation bar
selected = option_menu("Portfolio", list(pages.keys()),
                       icons=['house', 'speedometer2', 'book'],
                       menu_icon="cast", default_index=0)

# Display the selected page (the page will be imported from pages folder)
st.write(f"You have selected : {selected}")
