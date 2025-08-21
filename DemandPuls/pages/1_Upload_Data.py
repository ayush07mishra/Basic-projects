import streamlit as st
import pandas as pd

st.title("📤 Upload Sales Data")

uploaded_file = st.file_uploader("Upload your .CSV file", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.session_state['df'] = df
    st.success("✅ Data Uploaded Successfully!")
    st.dataframe(df.head())

    if st.button("➡️ Proceed to Train Model"):
        st.switch_page("pages/2_Train_Model.py")
