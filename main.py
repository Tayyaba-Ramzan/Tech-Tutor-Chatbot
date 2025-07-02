import os
from dotenv import load_dotenv
import chainlit as cl
from agents import Agent, Runner, RunConfig, AsyncOpenAI, OpenAIChatCompletionsModel
from openai.types.responses import ResponseTextDeltaEvent

load_dotenv()

# 🌐 API Key and Client Setup
gemini_api_key = os.getenv("GEMINI_API_KEY")  # Use uppercase for env variable name

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# 🎯 Tech Expert Agent (like W3Schools)
agent = Agent(
    name="Tech Tutor",
    instructions="""
You are a professional and experienced technical tutor, similar to W3Schools.
Only respond to technology-related questions. If the user asks about anything outside tech (like politics, religion, sports, etc.), politely say:
'Sorry, I only assist with technology-related topics. Please ask a tech-related question.'

You can answer questions about:
- Programming languages (Python, JavaScript, C++, etc.)
- Web development (HTML, CSS, React, Node.js, etc.)
- Databases (SQL, MongoDB, etc.)
- DevOps (Git, Docker, CI/CD, etc.)
- Computer Science fundamentals (data structures, algorithms, OS, networking)
- APIs, libraries, tools, and frameworks
- Tech errors and debugging help

Always give clear explanations with code examples where relevant. Think like a real tech tutor who gives accurate, concise, and friendly responses.
"""
)

# 💬 Start of Chat
@cl.on_chat_start
async def handle_chat_start():
    cl.user_session.set("history", [])
    await cl.Message(content="👋 Hello! I'm your Tech Tutor. Ask me anything related to technology, programming, or web development.").send()

# 💡 Message Handler
@cl.on_message
async def handle_message(message: cl.Message):
    history = cl.user_session.get("history")
    history.append({"role": "user", "content": message.content})

    # 📩 Initial Response
    msg = cl.Message(content="")
    await msg.send()

    # 🚀 Run agent
    result = Runner.run_streamed(
        agent,
        input=history,
        run_config=config
    )

    # 🔁 Stream Tokens
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            await msg.stream_token(event.data.delta)

    history.append({"role": "assistant", "content": result.final_output})
    cl.user_session.set("history", history)
