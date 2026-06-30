import streamlit as st
import requests

# ฐานข้อมูลคนไข้ (ในอนาคตเราค่อยไปดึงจาก Database)
patient_db = {
    "เตียง 1": "นาย หม่องต้า", "เตียง 2": "นาย เกย์", "เตียง 3": "นางสาว ไอด้า",
    "เตียง 4": "นาย ยุก", "เตียง 5": "นางสาว แคท", "เตียง 6": "นาย แมว",
    "เตียง 7": "นาย บูม", "เตียง 8": "นาง แก้ว", "เตียง 9": "นาย คำ", "เตียง 10": "นาย วี"
}

st.title("NexCall - เลือกเตียง")

# 1. เลือกเตียง
select_bed = st.selectbox("กรุณาเลือกเตียง:", list(patient_db.keys()))

# 2. ดึงชื่อขึ้นอัตโนมัติ
patient_name = patient_db[select_bed]
st.info(f"ผู้ป่วย: {patient_name} ({select_bed})")


# 2. เพิ่มระบบ Triage (คัดกรองด่วน)
st.subheader("ระดับความด่วน")
urgency = st.radio("เลือกความเร่งด่วน:", [
    "🟢 เขียว: ปกติ (เช่น ขอเปลี่ยนผ้าปู, ขอน้ำ)",
    "🟡 เหลือง: กึ่งด่วน (เช่น ปวดแผล, ขอยาแก้ปวด)",
    "🔴 แดง: ฉุกเฉิน (เช่น หายใจหอบ, เลือดออกมาก)"
])

# 3. เลือกข้อความ
st.subheader("ความต้องการ")
option = st.radio("เลือกหัวข้อที่ต้องการ:", ["ขอน้ำ", "ขอห้องน้ำ", "ปวดหลัง", "ขอยาแก้ปวด", "เจ็บแผล", "อื่นๆ (พิมพ์เอง)"])

message = ""
if option == "อื่นๆ (พิมพ์เอง)":
    message = st.text_input("ระบุเพิ่มเติม:")
else:
    message = option

# 4. ปุ่มส่ง
if st.button("ส่งข้อมูล"):
    TOKEN = '8871249436:AAFEqJ2sNQZLXvHV3PsC0nHg9BXKlln3q3E'
    CHAT_ID = '8812758125'
    
    # รวมข้อความให้สวยงาม
    full_msg = f"{urgency}\n🔔 แจ้งเตือนจาก {select_bed}\n👤 ผู้ป่วย: {patient_name}\n💬 ความต้องการ: {message}"
    
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {'chat_id': CHAT_ID, 'text': full_msg}
    requests.post(url, params=params)
    
    st.success("ส่งข้อมูลเรียบร้อย พยาบาลรับทราบแล้วเจ้า!")


# 5. ปุ่มส่ง
if st.button("ส่งข้อความด่วน"):
    TOKEN = '8871249436:AAFEqJ2sNQZLXvHV3PsC0nHg9BXKlln3q3E'
    CHAT_ID = '8812758125'
    full_msg = f"🔔 แจ้งเตือนจาก {select_bed}\n👤 ผู้ป่วย: {patient_name}\n💬 ความต้องการ: {message}"
    
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {'chat_id': CHAT_ID, 'text': full_msg}
    requests.post(url, params=params)
    
    st.success("ส่งข้อมูลเรียบร้อย พยาบาลกำลังไปหานะคะ!")
