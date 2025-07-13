import streamlit as st
import pandas as pd
from utils.model import train_model

st.title("🧠 Train ML Model")

df = st.session_state.get('df', None)
if df is None:
    st.warning("Please upload data first.")
    st.stop()

st.write("Detected Columns:", list(df.columns))

target = st.selectbox("Select Target Variable", df.columns, index=len(df.columns)-1)

if st.button("⚙️ Train Model"):
    with st.spinner("Training..."):
        model = train_model(df, target)
        st.session_state['model'] = model
    st.success("🎉 Model Trained Successfully!")

    if st.button("➡️ Go to Forecast Dashboard"):
        st.switch_page("pages/3_Forecast_Dashboard.py")
