import os
from dotenv import load_dotenv
import chainlit as cl
from agents import Agent, Runner, RunConfig, AsyncOpenAI, OpenAIChatCompletionsModel
from openai.types.responses import ResponseTextDeltaEvent

load_dotenv()

# 🌐 Load Gemini API Key
gemini_api_key = os.getenv("GEMINI_API_KEY")

# 🌐 Setup External Client
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# 🔧 Setup Model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# 🧠 All-Tech Tutor Agent (W3Schools Style)
agent = Agent(
    name="Tech Tutor",
    instructions="""
You are a professional technical instructor who teaches a wide range of tech topics, similar to W3Schools.

✅ You must answer only technical/programming-related questions such as:
- Python, JavaScript, HTML, CSS, SQL, C++, Java, Bash, Git, APIs
- Topics like loops, variables, functions, databases, DOM, JSON, regex, etc.

❌ If a user asks anything unrelated to technology or programming (like love, religion, movies, personal life), strictly say:
"Sorry, I can only help with tech-related topics like Python, HTML, JavaScript, etc."

You must always respond in English.
Give clear, structured answers with code examples when relevant.
Never say "I don't know" for tech topics. Be like a real online tutor, similar to W3Schools but more interactive.
"""
)

# 💬 Chat Start Handler
@cl.on_chat_start
async def handle_chat_start():
    cl.user_session.set("history", [])
    await cl.Message(content="👋 Hello! I'm your technical tutor. Ask me anything related to tech (like Python, HTML, SQL, etc).").send()

# 💬 Message Handler
@cl.on_message
async def handle_message(message: cl.Message):
    history = cl.user_session.get("history")
    history.append({"role": "user", "content": message.content})

    msg = cl.Message(content="")
    await msg.send()

    result = Runner.run_streamed(
        agent,
        input=history,
        run_config=config
    )

    final_response = ""

    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            final_response += event.data.delta
            await msg.stream_token(event.data.delta)

    # ✅ Update final message to stop blinking effect
    await msg.update(content=final_response)

    history.append({"role": "assistant", "content": final_response})
    cl.user_session.set("history", history)

