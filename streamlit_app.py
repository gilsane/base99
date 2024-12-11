import streamlit as st
import pandas as pd

# Define GitHub raw URLs for the files
file_urls = {
    "File 1": "https://github.com/gilsane/base99/raw/refs/heads/main/a.csv",
}

# Load a file from GitHub
@st.cache
def load_file(file_url):
    return pd.read_csv(file_url)

# Streamlit app
st.title("Multiple File Loader in Streamlit")

# Select a file to display
selected_file = st.selectbox("Select a file to load", list(file_urls.keys()))

# Load and display the selected file
if selected_file:
    st.write(f"Loading data for: {selected_file}")
    df = load_file(file_urls[selected_file])
    st.dataframe(df)

# Load and combine all files
if st.button("Load All Files"):
    st.write("Loading all files...")
    combined_df = pd.concat([load_file(url) for url in file_urls.values()])
    st.write("Combined Data:")
    st.dataframe(combined_df)
