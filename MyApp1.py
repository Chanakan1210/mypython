import streamlit as st
import pandas as pd

st.title("Website Developing using Python")
#st.header("🍭Website Developing using Python🍭")
st.subheader("🍬Chanakan Jangeejang🍬")
st.image('chanakan.jpg')

dt=pd.read_csv('./data/iris.csv')
st.subheader("🍬ข้อมูลดอกไม้ Iris🍬")
st.write(dt.head(10))

st.subheader("🍬สถิติข้อมูลดอกไม้ Iris🍬")
st.write('ผลรวม')
st.write('ค่าเฉลี่ย')
st.write('ค่ามากที่สุด')
st.write('ค่าน้อยที่สุด')