from curses import REPORT_MOUSE_POSITION
from api.ai.llms import get_openai_llm
from api.ai.tools import (send_me_email, get_unread_email)

EMAIL_TOOLS = {
    "send_me_email": send_me_email,
    "get_unread_email": get_unread_email,
}

# This function will be used to generate email messages based on user queries and tools
def email_assistant(query: str):
    llm_base = get_openai_llm()
   #  llm = llm_base.binds_tools([send_me_email, get_unread_email])
    llm = llm_base.bind_tools(list(EMAIL_TOOLS.values()))
    messages = [
        (
            "system",
            "You are a helpful assistant for managing my email inbox.",
        ),
        ("human", f"{query}.")
    ]
    response = llm.invoke(messages)
    messages.append(response)
   #  Here it will be used to check if the response contains any tool calls and if so, it will be executed
    if hasattr(response, "tool_calls") and response.tool_calls:
        for tool_call in response.tool_calls:
            tool_name = tool_call.get("name")
            tool_func = EMAIL_TOOLS.get(tool_name)
            tool_args = tool_call.get('args')
            if not tool_func:
                continue
            tool_result = tool_func.invoke(tool_args)
            messages.append(tool_result)
        final_response = llm.invoke(messages)
        return final_response
    return response
