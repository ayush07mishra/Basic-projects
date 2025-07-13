import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def generate_forecast_table(df, model):
    df_encoded = pd.get_dummies(df, drop_first=True)
    preds = model.predict(df_encoded.drop(columns=['Quantity Sold']))
    forecast_df = df[['Product', 'Pincode']].copy()
    forecast_df['Predicted Demand'] = preds.astype(int)
    forecast_df['Confidence %'] = np.random.randint(80, 99, size=len(preds))
    return forecast_df

def plot_line_chart(df):
    st.subheader("📊 Demand Trend Over Time")
    time_df = df.groupby('Date')['Quantity Sold'].sum().reset_index()
    fig, ax = plt.subplots()
    ax.plot(time_df['Date'], time_df['Quantity Sold'], marker='o')
    st.pyplot(fig)

def show_heatmap(df):
    st.subheader("🗺️ Demand Heatmap (Simulated)")
    st.markdown("🟢 Coming Soon: Geospatial map using `folium`")
