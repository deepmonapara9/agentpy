from langgraph.prebuilt import create_react_agent
from api.ai.llms import get_openai_llm
from api.ai.tools import (research_email, send_me_email, get_unread_email)

# This is the list of tools that will be used by the email assistant agent and can add more tools as needed
EMAIL_TOOLS_LIST = [
    send_me_email,
    get_unread_email,
    research_email,
]

# Here this will be used to create the email assistant agent
def get_email_agent():
    model = get_openai_llm()
    agent = create_react_agent(
        model=model,
        tools=EMAIL_TOOLS_LIST,
        prompt="You are a helpful assistant for managing my email inbox for generating, sending, and reviewing emails.",
        name="email_agent"
    )

    return agent


# This is the research agent that will be used to generate emails
def get_research_agent():
    model = get_openai_llm()
    agent = create_react_agent(
        model=model,
        tools=[research_email],
        prompt="You are a helpful research assistant for preparing email data",
        name='research_agent',
    )

    return agent
