import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path

st.set_page_config(page_title="Cybersec Intrusion Detection System", layout="wide")

BASE_DIR = Path(__file__).resolve().parent

@st.cache_data
def load_data():
    df = pd.read_csv(BASE_DIR / "data" / "raw" / "cybersecurity_intrusion_data.csv")
    return df

df = load_data()

st.sidebar.title("Cybersec Intrusion Detection")
st.sidebar.markdown("Status: **ONLINE**")
st.sidebar.markdown("Version: **1.0.0**")

with st.sidebar:
    with st.form("intrusion_report"):
        st.subheader("Intrusion Report")
        session_id = st.text_input("Session ID", value="S_00001")
        network_packet_size = st.number_input("Network Packet Size", min_value=0.0, max_value=1500.0, value=583.0)
        protocol_type = st.selectbox("Protocol Type", options=["TCP", "UDP", "ICMP", "HTTPS"])
        login_attempts = st.number_input("Login Attempts", min_value=0, max_value=100, value=11)
        session_duration = st.number_input("Session Duration", min_value=0.0, max_value=10000.0, value=152.0)
        encryption_used = st.selectbox("Encryption Used", options=["AES-256", "DES", "AES", "None", "RSA"])
        ip_reputation_score = st.number_input("IP Reputation Score", min_value=0.0, max_value=100.0, value=36.0)
        failed_logins = st.number_input("Failed Logins", min_value=0, max_value=100, value=3)
        browser_type = st.selectbox("Browser Type", options=["Chrome", "Firefox", "Edge", "Safari", "Unknown"])
        unusual_time_access = st.selectbox("Unusual Time Access", options=["Oui", "Non"])
        
        submitted = st.form_submit_button("Analyze")
        
        if submitted:
            score = 0
            if protocol_type in ["ICMP", "HTTPS"]:
                score += 0.3
            if login_attempts > 10:
                score += 0.2
            if failed_logins > 2:
                score += 0.2
            if unusual_time_access == "Oui":
                score += 0.2
            if ip_reputation_score < 30:
                score += 0.1
            confidence = min(0.99, max(0.5, score + 0.3))
            prediction = "Attack Detected" if score > 0.4 else "Normal"
            
            st.success(f"Prediction: **{prediction}**")
            st.info(f"Confidence: **{confidence:.3f}**")

st.title("Cybersecurity Intrusion Analytics")

left_col, right_col = st.columns([1, 2])

with left_col:
    st.subheader("Attack Detection Distribution")
    attack_counts = df['attack_detected'].value_counts()
    attack_pct = attack_counts / attack_counts.sum() * 100
    st.write(f"**Attack**: {attack_pct.get(1, 0):.1f}%")
    st.write(f"**Normal**: {attack_pct.get(0, 0):.1f}%")
    
    chart_data = pd.DataFrame({
        'Label': ['Attack', 'Normal'],
        'Count': [attack_counts.get(1, 0), attack_counts.get(0, 0)]
    })
    st.bar_chart(chart_data.set_index('Label'))

with right_col:
    st.subheader("Feature Correlation Matrix")
    numeric_cols = ['network_packet_size', 'login_attempts', 'session_duration', 
                    'ip_reputation_score', 'failed_logins', 'unusual_time_access', 'attack_detected']
    corr = df[numeric_cols].corr()
    st.write(corr)

st.subheader("Intrusion Detection by Criteria")

criteria = st.selectbox("Select Criteria", [
    "Protocol Type", "Browser Type", "Encryption Used", 
    "Failed Logins", "Unusual Time Access", "Login Attempts", "IP Reputation Score"
])

col1, col2 = st.columns(2)

if criteria == "Protocol Type":
    with col1:
        st.write("**Protocol Type**")
        proto_df = df.groupby('protocol_type')['attack_detected'].agg(['count', 'sum']).reset_index()
        proto_df.columns = ['Protocol', 'Total', 'Attacks']
        st.bar_chart(proto_df.set_index('Protocol')['Total'])
    with col2:
        st.write("**Attack Rate by Protocol**")
        proto_df['Rate'] = proto_df['Attacks'] / proto_df['Total']
        st.bar_chart(proto_df.set_index('Protocol')['Rate'])

elif criteria == "Browser Type":
    with col1:
        st.write("**Browser Type**")
        browser_df = df.groupby('browser_type')['attack_detected'].agg(['count', 'sum']).reset_index()
        browser_df.columns = ['Browser', 'Total', 'Attacks']
        st.bar_chart(browser_df.set_index('Browser')['Total'])
    with col2:
        st.write("**Attack Rate by Browser**")
        browser_df['Rate'] = browser_df['Attacks'] / browser_df['Total']
        st.bar_chart(browser_df.set_index('Browser')['Rate'])

elif criteria == "Encryption Used":
    with col1:
        st.write("**Encryption Used**")
        enc_df = df.groupby('encryption_used')['attack_detected'].agg(['count', 'sum']).reset_index()
        enc_df.columns = ['Encryption', 'Total', 'Attacks']
        enc_df = enc_df.fillna('Unknown')
        st.bar_chart(enc_df.set_index('Encryption')['Total'])
    with col2:
        st.write("**Attack Rate by Encryption**")
        enc_df['Rate'] = enc_df['Attacks'] / enc_df['Total']
        st.bar_chart(enc_df.set_index('Encryption')['Rate'])

elif criteria == "Failed Logins":
    with col1:
        st.write("**Failed Logins Distribution**")
        fl = df.groupby('failed_logins')['attack_detected'].count()
        st.bar_chart(fl)
    with col2:
        st.write("**Attack Rate by Failed Logins**")
        fl_rate = df.groupby('failed_logins')['attack_detected'].mean()
        st.bar_chart(fl_rate)

elif criteria == "Unusual Time Access":
    with col1:
        st.write("**Unusual Time Access**")
        ut = df.groupby('unusual_time_access')['attack_detected'].agg(['count', 'sum']).reset_index()
        ut['label'] = ut['unusual_time_access'].map({0: 'Normal Time', 1: 'Unusual Time'})
        st.bar_chart(ut.set_index('label')['count'])
    with col2:
        st.write("**Attack Rate**")
        ut['rate'] = ut['sum'] / ut['count']
        st.bar_chart(ut.set_index('label')['rate'])

elif criteria == "Login Attempts":
    with col1:
        st.write("**Login Attempts**")
        st.metric("Min", int(df['login_attempts'].min()))
        st.metric("Max", int(df['login_attempts'].max()))
        st.metric("Avg", f"{df['login_attempts'].mean():.1f}")
    with col2:
        st.write("**Attack Rate by Login Attempts**")
        la_rate = df.groupby('login_attempts')['attack_detected'].mean()
        st.bar_chart(la_rate)

elif criteria == "IP Reputation Score":
    with col1:
        st.write("**IP Reputation Score**")
        st.metric("Min", f"{df['ip_reputation_score'].min():.2f}")
        st.metric("Max", f"{df['ip_reputation_score'].max():.2f}")
        st.metric("Avg", f"{df['ip_reputation_score'].mean():.2f}")
    with col2:
        st.write("**Attack Rate by Score (binned)**")
        df['ip_bin'] = pd.cut(df['ip_reputation_score'], bins=5)
        ip_rate = df.groupby('ip_bin')['attack_detected'].mean()
        st.bar_chart(ip_rate)
