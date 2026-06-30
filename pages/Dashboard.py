import streamlit as st

st.set_page_config(page_title="NexCall Ward Dashboard", layout="wide")

st.title("🚨 ศูนย์บัญชาการพยาบาล - NexCall Dashboard")

# เชื่อมต่อกับ Google Sheets
conn = st.connection("gsheets", type="gsheets")

# ดึงข้อมูลมาแสดง
df = conn.read(spreadsheet="https://docs.google.com/spreadsheets/d/1DL9iBA7j4vaC7BdofkDaFIP06idn_rfXLHede6sUTV8", usecols=[0, 1, 2, 3, 4])

# แสดงผลเป็นตาราง
st.dataframe(df, use_container_width=True)

# ฟังก์ชันใส่สีให้สถานะ (ถ้าต้องการสีแดง/เหลือง)
def color_urgency(val):
    color = 'red' if val == 'สีแดง' else 'orange' if val == 'สีเหลือง' else 'green'
    return f'background-color: {color}'

# โชว์ข้อมูลแบบสวยงาม
st.subheader("สถานะเตียงในวอร์ด")
st.table(df)

# ปุ่มกดรีเฟรชเองทุก 5 วินาที
if st.button('อัปเดตข้อมูล'):
    st.rerun()
