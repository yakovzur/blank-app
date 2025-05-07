# app.py
import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_db import User, Base


# הסתרת תפריט השלוש נקודות וכפתור ה-Deploy
hide_streamlit_style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# יצירת engine וחיבור למסד הנתונים
engine = create_engine("sqlite:///my_db.sqlite")
Session = sessionmaker(bind=engine)
session = Session()

st.title("מערכת משתמשים פשוטה")

name = st.text_input("הכנס שם")

if st.button("הוסף למסד הנתונים"):
    new_user = User(name=name)
    session.add(new_user)
    session.commit()
    st.success("המשתמש נוסף!")

if st.button("הצג את כל המשתמשים"):
    users = session.query(User).all()
    for u in users:
        st.write(f"{u.id}: {u.name}")
