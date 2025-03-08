import streamlit as st

import random
import time
import  requests



st.title("🏧Money Making Machine")

def generate_money():
    return random.randint(1, 1000)

st.subheader("Instant Cash generator")
if st.button("Generate Money"):
    # st.loader()
    st.write("Counting your Money")
    time.sleep(random.randint(1,5))
    amount = generate_money()
    st.success(f"You made ${amount}!")


def fetch_side_hustle():
    try:
        response = requests.get("http://127.0.0.1:8000/side_hustle")
        if response.status_code == 200:
             hustle = response.json()
             return hustle["side_hustles"]
        else:
             return ("Freelancing")

    except:
            return ("Something went wrong")
    
st.subheader("Side Hustle ideas")
if st.button("Generate Hustle"):
     idea = fetch_side_hustle()
     st.write(idea)


def fetch_money_quotes():
    try:
        response = requests.get("http://127.0.0.1:8000/money_quotes")
        if response.status_code == 200:
             quote = response.json()
             return quote["money_quotes"]
        else:
             return ("Freelancing")

    except:
            return ("Something went wrong")
    
st.subheader("Money Quotes")
if st.button("Generate Mone Quotes"):
     idea = fetch_money_quotes()
     st.write(idea)
