

import streamlit as st
import pandas as pd
import os
from utils.ml_utils import train_model, load_model, predict

st.set_page_config(page_title="DemandPulse", layout="wide")


if 'df' not in st.session_state:
    st.session_state.df = None

if 'model' not in st.session_state:
    st.session_state.model = None


menu = st.sidebar.radio("📊 Navigate", [
    "🏠 Home", 
    "📤 Upload Data", 
    "🧠 Train Model", 
    "📈 Forecast Dashboard", 
    "⚠️ Real-Time Alerts"
])

# 1. HOME
if menu == "🏠 Home":
    st.title("DemandPulse – AI-Powered Demand Forecasting")
    st.subheader("Predict Smarter. Stock Better. Deliver Perfectly.")
    st.markdown("Built for modern retailers who want real-time demand insights by region.")
    st.image("https://cdn-icons-png.flaticon.com/512/4149/4149640.png", width=300)
    if st.button("🚀 Get Started"):
        st.experimental_set_query_params(page="Upload Data")

# 2. UPLOAD DATA
elif menu == "📤 Upload Data":
    st.title("Upload Your Sales Data (.csv)")
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
    
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.session_state.df = df
        st.success("✅ Data Uploaded Successfully!")
        st.write(df.head())

# 3. TRAIN MODEL
elif menu == "🧠 Train Model":
    st.title("Train ML Model")

    if st.session_state.df is not None:
        df = st.session_state.df
        target_col = st.selectbox("Select Prediction Target", options=df.columns, index=df.columns.get_loc("Quantity Sold") if "Quantity Sold" in df.columns else 0)
        
        if st.button("🔁 Train Model"):
            model = train_model(df, target_column=target_col)
            st.session_state.model = model
            st.success("✅ Model Trained Successfully!")
    else:
        st.warning("📂 Please upload data first.")

# 4. FORECAST DASHBOARD
elif menu == "📈 Forecast Dashboard":
    st.title("Forecast Dashboard")

    if st.session_state.df is not None and st.session_state.model is not None:
        df = st.session_state.df
        model = st.session_state.model

        filtered_df = df.drop(columns=["Quantity Sold"], errors="ignore")
        
        st.subheader("Filters")
        if "Product" in df.columns:
            product_filter = st.selectbox("Filter by Product", ["All"] + df["Product"].unique().tolist())
            if product_filter != "All":
                filtered_df = filtered_df[df["Product"] == product_filter]

        if st.button("▶️ Run Forecast"):
            preds = predict(model, filtered_df)
            result_df = filtered_df.copy()
            result_df["Predicted Demand"] = preds
            result_df["Confidence (%)"] = [round(abs(100 - abs(x - preds.mean())), 2) for x in preds]
            st.session_state['forecast_df'] = result_df

            st.success("📊 Forecast Results")
            st.dataframe(result_df.head())

            # Download
            st.download_button("⬇️ Download Report", result_df.to_csv(index=False), file_name="forecast_report.csv")
    else:
        st.warning("🚧 Please upload data and train the model first.")

# 5. REAL-TIME ALERTS
elif menu == "⚠️ Real-Time Alerts":
    st.title("Real-Time Alerts Panel")
    st.info("🚨 These alerts are simulated for now.")
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("🔴 Overstock Warning", "24 SKUs", "-13%")
        st.metric("🟡 Low Supply Zones", "8 Regions", "+5% risk")

    with col2:
        st.metric("📉 Cancel Rate Monitor", "3.2%", "+1.1%")
        st.metric("🔥 Sales Spike Alert", "4 SKUs", "+19% spike")
