import streamlit as st

# Define the pages in the app
pages = {
    "Page 1": st.Page("page1.py", default=True),  # page1.py को डिफ़ॉल्ट पेज के रूप में सेट करें
    "Page 2": st.Page("page2.py"),
    "Page 3": st.Page("page3.py"),
}

# Create a navigation bar
pg = st.navigation(pages)

# Run the navigation bar
pg.run()
