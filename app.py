import streamlit as st
import requests

# เอา Token ของไอด้ามาใส่ตรงนี้ (ต้องมี '...' ครอบไว้ด้วยนะเจ้า)
TOKEN = 'ใส่รหัสTokenที่ได้จากไลน์มาวางตรงนี้เจ้า'

def send_line(msg):
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': 'Bearer ' + TOKEN}
    data = {'message': msg}
    requests.post(url, headers=headers, data=data)

st.title("🩺 ระบบสื่อสารคนไข้")

ent = ["นาย ก B1", "นาย ข B2", "นาย ค B3", "นาย ง B4", "นาย จ B5"]
select_patient = st.selectbox("เลือกรายชื่อผู้ป่วย:", ent)
message = st.text_input("ระบุความต้องการของท่าน:")

if st.button("ส่งข้อความ"):
    if TOKEN == 'ใส่รหัสTokenที่ได้จากไลน์มาวางตรงนี้เจ้า':
        st.error("ไอด้ายังไม่ได้ใส่ Token นะเจ้า!")
    else:
        full_msg = f"\nคนไข้: {select_patient}\nความต้องการ: {message}"
        send_line(full_msg)
        st.success("---ส่งข้อความสำเร็จ---")
        st.write(f"เตียง: {select_patient}")
        st.write(f"ข้อความ: {message}")
