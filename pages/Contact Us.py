import streamlit as st
import pandas
import smtplib

email_sender = "russel.nlwork@gmail.com"
email_receiver = st.text_input("Your Email Address")

df = pandas.read_csv('topics.csv')
options = [row['topic'] for index, row in df.iterrows()]


subject = st.selectbox('What topics you want to discuss?', options)
body = st.text_area("Enter your query")

st.button("Send")

if st.button:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_sender, "DarkSeason24@")
    server.sendmail(email_sender, email_receiver, msg.as_string())
    server.quit()



