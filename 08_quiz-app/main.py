import streamlit as st  # Import the Streamlit library
import random
import time

# Set the title of the Streamlit application
st.title("📝 Quiz Application")

# Define a list of questions for the quiz
questions = [
    {"question": "What is the output of print(2 ** 3)?",
     "options": ["6", "8", "9", "12"],
     "answer": "8"},
    {"question": "Which of the following is a mutable data type in Python?",
     "options": ["tuple", "list", "string", "int"],
     "answer": "list"},
    {"question": "What is the correct file extension for Python files?",
     "options": [".py", ".java", ".cpp", ".txt"],
     "answer": ".py"},
    {"question": "How do you start a comment in Python?",
     "options": ["//", "##", "/*", "<!--"],
     "answer": "#"},
    {"question": "Which keyword is used to define a function in Python?",
     "options": ["func", "define", "def", "function"],
     "answer": "def"},
    {"question": "What is the output of print('Hello' + 'World')?",
     "options": ["Hello World", "HelloWorld", "Hello+World", "Error"],
     "answer": "HelloWorld"},
    {"question": "Which of the following is used to define a block of code in Python?",
     "options": ["{}", "[]", "()", "Indentation"],
     "answer": "Indentation"},
    {"question": "What is the output of print(type([]))?",
     "options": ["<class 'list'>", "<class 'tuple'>", "<class 'dict'>", "<class 'set'>"],
     "answer": "<class 'list'>"},
    {"question": "Which of the following is not a keyword in Python?",
     "options": ["pass", "eval", "assert", "nonlocal"],
     "answer": "eval"},
    {"question": "What is the output of print(10 // 3)?",
     "options": ["3.33", "3", "4", "3.0"],
     "answer": "3"}
]

# Check if the current question is not already set in the session state
if "current_question" not in st.session_state:
    # Randomly select a question from the list of questions
    st.session_state.current_question = random.choice(questions)

# Retrieve the current question from the session state
question =  st.session_state.current_question

# Display the question as a subheader
st.subheader(question["question"])

# Create a selectbox for the user to choose their answer
selected_option = st.radio("Choose your answer", question["options"],key="answer")

# Check if the user has clicked the "Submit Answer" button
if st.button("Submit Answer"):
    # Check if the user's answer is correct
    if selected_option == question["answer"]:
        st.success("✅ Correct Answer")    
        st.balloons()
    else:
        st.error("❌ Incorrect Answer")
        st.warning("The correct answer is:"+question["answer"])
    
    # Wait for 3 seconds before proceeding
    time.sleep(3)

    # Randomly select a new question from the list of questions
    st.session_state.current_question = random.choice(questions)

    # Rerun the application to display the new question
    st.rerun()