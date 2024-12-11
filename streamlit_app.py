import streamlit as st
import pandas as pd

# Define GitHub raw URLs for the files
file_urls = {
    "File 1": "https://github.com/gilsane/base99/raw/refs/heads/main/a.csv"
}

# Function to load a file with multiple encoding attempts
@st.cache_data
def load_file(file_url):
    encodings = ['utf-8', 'cp949', 'utf-8-sig']
    for encoding in encodings:
        try:
            return pd.read_csv(file_url, encoding=encoding), encoding
        except UnicodeDecodeError:
            continue  # Try the next encoding
    return None, None  # Return None if all encodings fail

# Streamlit app
st.title("Multiple File Loader in Streamlit")

# Select a file to display
selected_file = st.selectbox("Select a file to load", list(file_urls.keys()))

# Load and display the selected file
if selected_file:
    st.write(f"Loading data for: {selected_file}")
    df, encoding_used = load_file(file_urls[selected_file])
    if df is not None:
        st.success(f"File successfully read with encoding: {encoding_used}")
        st.dataframe(df)
    else:
        st.error("Failed to read the file with utf-8, cp949, and utf-8-sig encodings.")

# Load and combine all files
if st.button("Load All Files"):
    st.write("Loading all files...")
    all_dataframes = []
    failed_files = []
    for name, url in file_urls.items():
        df, encoding_used = load_file(url)
        if df is not None:
            st.write(f"{name} loaded successfully with encoding: {encoding_used}")
            all_dataframes.append(df)
        else:
            st.error(f"Failed to load {name}")
            failed_files.append(name)

    # Combine loaded files
    if all_dataframes:
        combined_df = pd.concat(all_dataframes)
        st.write("Combined Data:")
        st.dataframe(combined_df)
    if failed_files:
        st.error(f"Failed to load the following files: {', '.join(failed_files)}")
