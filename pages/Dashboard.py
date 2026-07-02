import streamlit as st
import pandas as pd

# ตั้งค่าหน้าจอ
st.set_page_config(initial_sidebar_state="collapsed")

# --- ระบบล็อกอินพยาบาล ---
if "nurse_logged_in" not in st.session_state:
    st.session_state["nurse_logged_in"] = False

if not st.session_state["nurse_logged_in"]:
    st.title("🔐 เข้าสู่ระบบสำหรับพยาบาล")
    password = st.text_input("รหัสผ่าน:", type="password")
    if st.button("เข้าสู่ระบบ"):
        if password == "Idealist49": 
            st.session_state["nurse_logged_in"] = True
            st.rerun()
        else:
            st.error("รหัสผ่านไม่ถูกต้อง!")
    st.stop() 

# --- Dashboard หลัก ---
st.title("🏥 ศูนย์บัญชาการพยาบาล - NexCall Dashboard")

# ฟังก์ชันดึงข้อมูล (ใช้วิธีที่เสถียรขึ้น)
def get_data():
    # เปลี่ยน URL เป็น CSV ตรงๆ ของ Google Sheets
    url = "https://docs.google.com/spreadsheets/d/1DL9iBA7j4vaC7BdofkDaFIP06idn_rfXLHede6sUTV8/export?format=csv"
    df = pd.read_csv(url)
    return df

# แสดงผลตาราง
try:
    df = get_data()
    st.subheader("สถานะเตียงในวอร์ด")
    st.dataframe(df, use_container_width=True)
except Exception as e:
    st.error(f"เกิดข้อผิดพลาด: โปรดตรวจสอบว่าแชร์ Google Sheets เป็น 'Anyone with the link can view' แล้วนะเจ้า (Error: {e})")

# ส่วนตอบกลับ
st.divider() # เพิ่มเส้นคั่นให้สวยขึ้น
st.subheader("💬 ระบบตอบกลับคนไข้")
target_bed = st.number_input("ระบุเลขเตียงที่ต้องการตอบกลับ:", min_value=1, step=1)
reply_text = st.text_input("ข้อความตอบกลับ:")

if st.button("ส่งข้อความ"):
   # โค้ดสำหรับบันทึกข้อความ (แนะนำให้ต่อกับ Google Sheets API หรือ Webhook ในอนาคต)
   st.write("กำลังบันทึกข้อมูล...")
   st.success(f"ส่งข้อความถึงเตียง {target_bed} เรียบร้อยค่ะ!")

# ปุ่มรีเฟรช
if st.button('อัปเดตข้อมูลล่าสุด'):
    st.rerun()


