import streamlit as st
import pandas as pd

st.title("Website Developing using Python")
#st.header("🍭Website Developing using Python🍭")
st.subheader("🍬Chanakan Jangeejang🍬")
st.image('chanakan.jpg')

dt=pd.read_csv('./data/iris.csv')
st.subheader("ข้อมูลดอกไม้ Iris")
st.write(dt.head(10))

#Index(['sepal.length', 'sepal.width', 'petal.length', 'petal.width',
#       'variety'],
#      dtype='object')

st.subheader("สถิติข้อมูลดอกไม้ Iris")
st.write('ผลรวม')
cl1,cl2,cl3,cl4=st.columns(4)
cl1.write(dt['sepal.length'].sum())
cl2.write(dt['sepal.width'].sum())
cl3.write(dt['petal.length'].sum())
cl4.write(dt['petal.width'].sum())
cols=['sepal.length', 'sepal.width','petal.length']
dx=dt[cols]
st.bar_chart(dx,x='sepal.length',y='sepal.width',color='petal.length')

st.write('ค่าเฉลี่ย')
cl1,cl2,cl3,cl4=st.columns(4)
cl1.write(dt['sepal.length'].mean())
cl2.write(dt['sepal.width'].mean())
cl3.write(dt['petal.length'].mean())
cl4.write(dt['petal.width'].mean())

st.write('ค่ามากที่สุด')
cl1,cl2,cl3,cl4=st.columns(4)
cl1.write(dt['sepal.length'].max())
cl2.write(dt['sepal.width'].max())
cl3.write(dt['petal.length'].max())
cl4.write(dt['petal.width'].max())

st.write('ค่าน้อยที่สุด')
cl1,cl2,cl3,cl4=st.columns(4)
cl1.write(dt['sepal.length'].min())
cl2.write(dt['sepal.width'].min())
cl3.write(dt['petal.length'].min())
cl4.write(dt['petal.width'].min())