import streamlit as st

st.title("ระบบสื่อสารคนไข้")

ent = ["นาย ก B1", "นาย ข B2", "นาย ค B3", "นาย ง B4", "นาย จ B5"]

# เปลี่ยนจาก input() เป็นselectbox ของ streamlit
select_patient = st.selectbox("เลือกรายชื่อผู้ป่วย:", ent)

# เปลี่ยนจาก input() เป็นtext_input ของ streamlit
message = st.text_input("ระบุความต้องการของท่าน:")

if st.button("ส่งข้อความ"):
    st.success("---ส่งข้อความสำเร็จ---")
    st.write(f"เตียง: {select_patient}")
    st.write(f"ข้อความ: {message}")
