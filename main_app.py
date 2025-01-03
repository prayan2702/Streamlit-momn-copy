import streamlit as st
import streamlit_navigation as nav

st.set_page_config(page_title="Portfolio", layout="wide")

# Define the pages in the app
pages = [
    st.StreamlitPage(name="Momentum Ranking", content=lambda: exec(open("momn_streamlit_app.py").read())),
    st.StreamlitPage(name="Strategy Performance", content=lambda: exec(open("Strategy_performance.py").read())),
    st.StreamlitPage(name="Strategy Tearsheet", content=lambda: exec(open("strategy-tearsheet.py").read())),
]

# Create a navigation bar
pg = nav.navigation(pages, default="Momentum Ranking")

# Run the navigation bar
pg.run()
