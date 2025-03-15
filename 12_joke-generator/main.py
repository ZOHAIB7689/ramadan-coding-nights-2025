import streamlit as st 
import requests


def  get_random_joke():
    """fetch a random joke from the API"""
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        if response.status_code == 200:
            joke_data = response.json()
            return f"{joke_data['setup']} \n\n {joke_data['punchline']}"
        else:
            return "Failed to fetch a joke. Please try again later."



    except Exception as e:
        return f"sorry we ran into a problem : {e}"
    

def main():
    st.title("Random joke Generator 🤣")
    st.write("Click the button below to generate a random joke 😄")

    if st.button("Tell me a joke"):
        joke = get_random_joke()
        st.write(joke)
        # st.success("Hope that made you smile! 😊")

    st.divider()
    st.markdown(
        """
        <div style='text-align:center; color:Green'>
        <p> Joke from official Joke API</p>
        </div>
        """,
        unsafe_allow_html=True
    )



if __name__ == "__main__":
    main()