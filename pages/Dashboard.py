import streamlit as st
import gspread

# ตั้งค่าหน้าจอ
st.set_page_config(page_title="NexCall Ward Dashboard", layout="wide")
st.title("🚨 ศูนย์บัญชาการพยาบาล - NexCall Dashboard")

# ส่วนของการเชื่อมต่อ Google Sheets แบบใหม่ (สาธารณะ)
# หมายเหตุ: วิธีนี้ใช้ได้เพราะไอด้าตั้งค่า Sheet เป็น "ทุกคนที่มีลิงก์เข้าถึงได้"
def get_data():
    # ในกรณีที่เป็นสาธารณะ เราจะใช้ URL ตรงๆ ในการเข้าถึงผ่าน library gspread
    # ไอด้าต้องเปิดไฟล์ให้คนเข้าถึงได้แบบ "Anyone with the link can view" นะเจ้า
    url = "https://docs.google.com/spreadsheets/d/1DL9iBA7j4vaC7BdofkDaFIP06idn_rfXLHede6sUTV8/export?format=csv"
    
    # วิธีนี้คือการดึงข้อมูลแบบง่ายและเสถียรที่สุดสำหรับแอปฯ ของไอด้า
    import pandas as pd
    import gspread
    
    # ใช้การดึงข้อมูลผ่านการ export เป็น CSV ซึ่งเป็นวิธีที่ง่ายที่สุดสำหรับไฟล์สาธารณะ
    sheet_url = url.replace('/edit', '/export?format=csv')
    df = pd.read_csv(sheet_url)
    return df

# ดึงข้อมูล
try:
    df = get_data()
    
    # แสดงผลตารางแบบสวยงาม
    st.subheader("สถานะเตียงในวอร์ด")
    st.dataframe(df, use_container_width=True)
    
    # ปุ่มกดรีเฟรช
    if st.button('อัปเดตข้อมูลล่าสุด'):
        st.rerun()
        
except Exception as e:
    st.error("เกิดข้อผิดพลาดในการดึงข้อมูล โปรดตรวจสอบว่าไอด้าเปิดแชร์ลิงก์เป็นสาธารณะแล้วนะเจ้า")

if st.button('อัปเดตข้อมูล'):
    st.rerun()
