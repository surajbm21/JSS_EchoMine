# app_streamlit.py

import streamlit as st
import pandas as pd
from echo_extractor import extract_echo_data  # your existing extraction logic

st.set_page_config(page_title="JSS EchoMine", page_icon="💓")

st.title("💓 JSS EchoMine - Echocardiogram Report Extractor")

st.write("Upload your echocardiogram PDF reports below to extract key values automatically.")

uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

if uploaded_file:
    with open("uploads/temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    st.info("Processing your report... please wait ⏳")

    try:
        # Assuming your echo_extractor.py has a function named `extract_echo_data`
        extracted_data = extract_echo_data("uploads/temp.pdf")
        df = pd.DataFrame([extracted_data])
        st.success("✅ Data extracted successfully!")
        st.dataframe(df)

        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("Download Extracted Data as CSV", csv, "echo_data.csv", "text/csv")
    except Exception as e:
        st.error(f"❌ Error: {e}")
