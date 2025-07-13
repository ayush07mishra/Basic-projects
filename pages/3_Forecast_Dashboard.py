import streamlit as st
from utils.visuals import generate_forecast_table, plot_line_chart, show_heatmap

st.title("📈 Forecast Dashboard")

df = st.session_state.get('df', None)
model = st.session_state.get('model', None)

if df is None or model is None:
    st.warning("Please upload data and train model.")
    st.stop()

product_filter = st.selectbox("Filter by Product", df['Product'].unique())
pincode_filter = st.selectbox("Filter by Pincode", df['Pincode'].unique())
date_range = st.date_input("Select Date Range", [])

if st.button("▶️ Run Forecast"):
    st.success("Forecast Generated Below 👇")
    forecast_df = generate_forecast_table(df, model)
    st.dataframe(forecast_df.head())

if st.button("🌍 View Heatmap"):
    show_heatmap(df)
# Forecast Button
if st.button("▶️ Run Forecast"):
    forecast_df = generate_forecast_table(df, model)
    st.session_state['forecast_df'] = forecast_df
    st.success("Forecast Generated Below 👇")
    st.dataframe(forecast_df.head())

# Show Download Button ONLY if forecast has been generated
if 'forecast_df' in st.session_state:
    forecast_df = st.session_state['forecast_df']
    
    st.download_button(
        label="⬇️ Download Report",
        data=forecast_df.to_csv(index=False),
        file_name="forecast_report.csv",
        mime="text/csv"
    )


plot_line_chart(df)
