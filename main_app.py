import streamlit as st

# Define the pages in the app
pages = {
    "Momentum Ranking": st.Page("momn_streamlit_app.py", default=True),
    "Strategy Performance": st.Page("Strategy_performance.py"),
    "Strategy Tearsheet": st.Page("strategy-tearsheet.py"),
}

# Create a navigation bar
pg = st.navigation(pages)

# Run the navigation bar
pg.run()
