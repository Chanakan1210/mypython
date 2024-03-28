import streamlit as st

st.title("Website Developing using Python")
#st.header("🍭Website Developing using Python🍭")
st.subheader("🍬Chanakan Jangeejang🍬")
st.image('chanakan.jpg')

dt=pd.read_csv('./data/iris.csv')
st.subheader("🍬ข้อมูลดอกไม้ Iris🍬")
st.write(dt.head(10))

st.subheader("🍬สถิติข้อมูลดอกไม้ Iris🍬")