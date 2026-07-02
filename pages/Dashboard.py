import streamlit as st
import streamlit as st

# --- โค้ดปิดตายหน้าพยาบาล ---
if "nurse_logged_in" not in st.session_state or not st.session_state["nurse_logged_in"]:
    st.error("⚠️ หน้าสำหรับพยาบาลเท่านั้น!")
    st.stop()  # คำสั่งนี้สำคัญมาก: มันจะหยุดอ่านโค้ดที่เหลือทั้งหมด คนไข้จะเห็นแค่คำเตือนนี้หน้าเดียว

st.set_page_config(initial_sidebar_state="collapsed")

import gspread
import pandas as pd

# --- ระบบล็อกอินพยาบาล (เพิ่มตรงนี้เจ้า) ---
if "nurse_logged_in" not in st.session_state:
    st.session_state["nurse_logged_in"] = False

if not st.session_state["nurse_logged_in"]:
    st.title("🔐 เข้าสู่ระบบสำหรับพยาบาล")
    password = st.text_input("รหัสผ่าน:", type="password")
    if st.button("เข้าสู่ระบบ"):
        if password == "1234": # ไอด้าเปลี่ยนรหัสตรงนี้ได้ตามต้องการเจ้า
            st.session_state["nurse_logged_in"] = True
            st.rerun()
        else:
            st.error("รหัสผ่านไม่ถูกต้องเจ้า!")
    st.stop() # ถ้ายังไม่ได้ล็อกอิน ให้หยุดทำงานหน้า Dashboard ไว้ตรงนี้

# --- โค้ดเดิมของไอด้า (จะรันก็ต่อเมื่อล็อกอินผ่านแล้ว) ---
st.set_page_config(page_title="NexCall Ward Dashboard", layout="wide")
st.title("🏥 ศูนย์บัญชาการพยาบาล - NexCall Dashboard")

# ฟังก์ชันดึงข้อมูล
def get_data():
    url = "https://docs.google.com/spreadsheets/d/1DL9iBA7j4vaC7BdofkDaFIP06idn_rfXLHede6sUTV8/edit"
    sheet_url = url.replace('/edit', '/export?format=csv')
    df = pd.read_csv(sheet_url)
    return df

# แสดงผลตาราง
try:
    df = get_data()
    st.subheader("สถานะเตียงในวอร์ด")
    st.dataframe(df, use_container_width=True)
    
    # ปุ่มรีเฟรช
    if st.button('อัปเดตข้อมูลล่าสุด'):
        st.rerun()
        
except Exception as e:
    st.error("เกิดข้อผิดพลาดในการดึงข้อมูล โปรดตรวจสอบว่าไอด้าเปิดแชร์ Google Sheets เป็นสาธารณะแล้วนะเจ้า")

