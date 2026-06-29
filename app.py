import streamlit as st
import requests

# เอา Token และ Chat ID ที่ได้มาใส่ตรงนี้เจ้า
TOKEN = 'วางรหัสTokenที่ได้จากBotFatherที่นี่'
CHAT_ID = '8871249436:AAFEqJ2sNQZLXvHV3PsC0nHg9BXKlln3q3E'

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {'chat_id': CHAT_ID, 'text': msg}
    requests.post(url, params=params)

st.title("🩺 ระบบสื่อสารคนไข้")
select_patient = st.selectbox("เลือกรายชื่อผู้ป่วย:", ["นาย ก B1", "นาย ข B2"])
message = st.text_input("ระบุความต้องการ:")

if st.button("ส่งข้อความ"):
    full_msg = f"คนไข้: {select_patient}\nความต้องการ: {message}"
    send_telegram(full_msg)
    st.success("ข้อความเด้งเข้า Telegram แล้วเจ้า!")
