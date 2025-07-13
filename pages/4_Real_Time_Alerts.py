import streamlit as st

st.title("📡 Real-Time Alerts")

st.markdown("""
<style>
.alert-card {
    background-color: #f8f9fa;
    border-left: 6px solid #e74c3c;
    padding: 16px;
    margin-bottom: 10px;
    border-radius: 5px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="alert-card"><b>🔺 Overstock Alert:</b> Soap in 110001 > 120% avg</div>', unsafe_allow_html=True)
st.markdown('<div class="alert-card"><b>🔻 Low Supply:</b> Shampoo in 560001 < 10 units</div>', unsafe_allow_html=True)
st.markdown('<div class="alert-card"><b>⚠️ Cancel Spike:</b> Orders from Tier-2 city jumped 50%</div>', unsafe_allow_html=True)
