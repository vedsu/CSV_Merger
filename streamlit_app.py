import streamlit as st
import pandas as pd

def merge_csv_files(files):
    # Initialize an empty list to store DataFrames
    dfs = []
    # Iterate over the uploaded files
    for file in files:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file)
        # Append the DataFrame to the list
        dfs.append(df)
    # Concatenate all DataFrames in the list
    merged_df = pd.concat(dfs, ignore_index=True)
    return merged_df

def main():
    st.title("CSV File Merger")
    
    # Allow users to upload CSV files
    uploaded_files = st.file_uploader("Upload CSV files", accept_multiple_files=True)
    
    if uploaded_files:
        # Merge the uploaded CSV files into a single DataFrame
        merged_df = merge_csv_files(uploaded_files)
        
        # Display the merged DataFrame
        st.write("Merged DataFrame:")
        st.write(merged_df)
        st.download_button(
                    label="Download CSV",
                    data=merged_df.to_csv().encode(),
                    file_name=f"merged.csv",
                    mime="text/csv"
                )

if __name__ == "__main__":
    main()
