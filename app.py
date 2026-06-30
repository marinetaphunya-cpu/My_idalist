import streamlit as st
import time

st.title("Welcome to NexCall 🩺")
st.write("ระบบสื่อสารคนไข้ไร้รอยต่อ")

# ทำ Loading bar แบบเท่ๆ
progress = st.progress(0)
for i in range(100):
    time.sleep(0.02)
    progress.progress(i + 1)

st.success("โหลดระบบเสร็จสิ้น!")
st.page_link("pages/2_Request_Page.py", label="ไปหน้าเรียกพยาบาล", icon="👉")
