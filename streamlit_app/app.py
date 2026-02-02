import streamlit as st
import requests

BACKEND_URL = "http://localhost:8000"

st.set_page_config(page_title="Data Processing API Demo", layout="centered")

st.title("📊 Data Processing API – Demo UI")

# Upload CSV

st.header("Upload CSV File")

uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    files = {
        "file": (uploaded_file.name, uploaded_file.getvalue(), "text/csv")
    }

    if st.button("Upload"):
        with st.spinner("Uploading..."):
            response = requests.post(f"{BACKEND_URL}/upload/", files=files)

        if response.status_code == 200:
            st.success("File uploaded successfully")
            st.json(response.json())
        else:
            st.error("Upload failed")
            st.json(response.json())

# Aggregate Analytics

st.header("Aggregate Analytics")

column = st.text_input("Column name (numeric)")
operation = st.selectbox(
    "Operation",
    ["sum", "avg", "min", "max", "count"]
)

if st.button("Run Aggregate"):
    params = {
        "column": column,
        "operation": operation
    }

    with st.spinner("Computing..."):
        response = requests.get(
            f"{BACKEND_URL}/analytics/aggregate",
            params=params
        )

    if response.status_code == 200:
        st.success("Aggregation result")
        st.json(response.json())
    else:
        st.error("Aggregation failed")
        st.json(response.json())

# Top Rows

st.header("Top Rows")

top_column = st.text_input("Top column (numeric)", key="top_column")
n = st.number_input("Top N", min_value=1, max_value=50, value=5)

if st.button("Get Top Rows"):
    params = {
        "column": top_column,
        "n": n
    }

    with st.spinner("Fetching top rows..."):
        response = requests.get(
            f"{BACKEND_URL}/analytics/top",
            params=params
        )

    if response.status_code == 200:
        st.success("Top rows")
        st.json(response.json())
    else:
        st.error("Failed to fetch top rows")
        st.json(response.json())
