import streamlit as st
import requests

# ฐานข้อมูลคนไข้ (ในอนาคตเราค่อยไปดึงจาก Database)
patient_db = {
    "เตียง 1": "นาย ก", "เตียง 2": "นาย ข", "เตียง 3": "นาย ค",
    "เตียง 4": "นาย ง", "เตียง 5": "นาย จ", "เตียง 6": "นาย ฉ",
    "เตียง 7": "นาย ช", "เตียง 8": "นาย ซ", "เตียง 9": "นาย ฌ", "เตียง 10": "นาย ญ"
}

st.title("NexCall - เลือกเตียง")

# 1. เลือกเตียง
select_bed = st.selectbox("กรุณาเลือกเตียง:", list(patient_db.keys()))

# 2. ดึงชื่อขึ้นอัตโนมัติ
patient_name = patient_db[select_bed]
st.info(f"ผู้ป่วย: {patient_name} ({select_bed})")

# 3. เลือกข้อความ (Quick Selection)
st.subheader("ความต้องการ")
option = st.radio("เลือกหัวข้อที่ต้องการ:", ["ขอน้ำ", "ขอห้องน้ำ", "เจ็บแผล", "อื่นๆ (พิมพ์เอง)"])

message = ""
if option == "อื่นๆ (พิมพ์เอง)":
    message = st.text_input("ระบุเพิ่มเติม:")
else:
    message = option

# 4. ปุ่มส่ง
if st.button("ส่งข้อความด่วน"):
    TOKEN = '8871249436:AAFEqJ2sNQZLXvHV3PsC0nHg9BXKlln3q3E'
    CHAT_ID = '8812758125'
    full_msg = f"🔔 แจ้งเตือนจาก {select_bed}\n👤 ผู้ป่วย: {patient_name}\n💬 ความต้องการ: {message}"
    
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {'chat_id': CHAT_ID, 'text': full_msg}
    requests.post(url, params=params)
    
    st.success("ส่งข้อมูลเรียบร้อย พยาบาลกำลังไปหาเจ้า!")
