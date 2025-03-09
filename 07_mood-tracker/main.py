import streamlit as st # for creating the web interface
import pandas as pd # for data manipulation
import datetime # for handling dates
import csv # for reading and writing the CSV file
import os # for file operations

MOOD_FILE =  "mood_log.csv" 

def load_mood_data():
    if not os.path.exists(MOOD_FILE):
        return pd.DataFrame(columns=["Date", "Mood" ])
    return pd.read_csv(MOOD_FILE, encoding='utf-8')

def save_mood_data(date, mood):
    with open(MOOD_FILE, "a", newline='', encoding='utf-8') as file:
       
        writer = csv.writer(file)

        writer.writerow([date, mood])  # Corrected to pass date and mood as a list

st.title("Mood Tracker 🌞")
today = datetime.date.today()

st.subheader("How are you feeling today? 🤔")

mood = st.selectbox("Select your mood",["Happy 😊","Sad 😔","Angry 😠", "Neutral 😐"])

if st.button("Log mood"):
    save_mood_data(today, mood)
    st.success("Mood Logged Successfully 🎉")


data = load_mood_data()

if not data.empty:
    st.subheader("Mood Trend Over Time")

    data["Date"] = pd.to_datetime(data["Date"])
    mood_counts = data.groupby("Mood").count()["Date"]

    st.bar_chart(mood_counts)