import os 
from dotenv import load_dotenv
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI


load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash", 
    openai_client=provider
)

agent = Agent(
    name="News Detection Agent",
    instructions="You are an AI journalist who verifies news articles for credibility. Analyze the following news article and determine if it is fake or real, and in a reply also use emojis.",
    model=model
)

user_question = input("Enter the news article to verify: ")
result =  Runner.run_sync(agent, user_question)               
print(f"✅ Result:  {result.final_output}")
        