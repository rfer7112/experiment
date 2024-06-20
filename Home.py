import streamlit as st
import pandas

st.set_page_config(layout='wide')

text1 = """
        Learn Python from zero to complete by building real 
        programs to gain the skills needed to land an entry-level job. """

st.header("The best Company")
st.info(text1)
st.subheader("Our Team")

df = pandas.read_csv('data.csv', sep=',')
col1, col2, col3 = st.columns([2, 2, 2])

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.image("images/" + row['image'])
        st.write(row['role'])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.image("images/" + row['image'])
        st.write(row['role'])

with col3:
    for index, row in df[8:12].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.image("images/" + row['image'])
        st.write(row['role'])
