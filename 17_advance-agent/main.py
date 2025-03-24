import os 
import chainlit as cl
from dotenv import load_dotenv
from typing import Optional ,Dict
from agents import Agent , Runner, OpenAIChatCompletionsModel, AsyncOpenAI 
from agents.tool import function_tool


# load enviroment variables
load_dotenv()

gemini_api_key=os.getenv("GEMINI_API_KEY")
provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)

model =OpenAIChatCompletionsModel(model="gemini-2.0-flash",openai_client=provider)


# @function_tool("get_question")
# def get_question() -> str:
#     """
#     Retrieves an industry-level interview question,  and returns it.
#     """
#     return "What is your experience with the latest technologies in the industry?"
    

agent = Agent(
    name="Ai Interview Coach",
    instructions='''You are an AI Interview Coach trained to conduct realistic job interviews for Frontend and Backend Developers specializing in HTML, CSS, JavaScript, Next.js, and Python. Your tasks include:

Asking technical and behavioral interview questions ONLY from HTML, CSS, JavaScript, Next.js, and Python.
Evaluating the user's response based on clarity, accuracy, and depth.
Providing constructive feedback & improvement suggestions based on best industry practices.
Suggesting follow-up questions to challenge the candidate further.
💡 If the response is weak, provide encouragement and learning resources to help the user improve.
🎙 Keep the conversation natural and engaging, just like a real interview.''',
     model=model,
)
@cl.oauth_callback
def oauth_callback (
        provider_id:str,
        token:str,
        new_user_data:Dict[str,str],
        default_user: cl.User
)-> Optional[cl.User]:
    """
    handle the Oath callback from github
    Return the user object if authentication is successful
    """
    print(f"user id ,{provider_id}")
    print(f" user data: {new_user_data}")
    return default_user


@cl.on_chat_start
async def handle_chat_start():
    cl.user_session.set("history",[])

    await cl.Message(content="Hello How are you today").send()



@cl.on_message
async def handle_message(message:cl.Message):
    history = cl.user_session.get("history")
    history.append({"role":"user","content":message.content})

    result = await cl.make_async(Runner.run_sync)(agent,input=history)

    response_text = result.final_output
    await cl.Message(content=response_text).send()

    history.append({"role":"assistant","content":response_text})
    cl.user_session.set("history",history)