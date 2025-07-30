import os
from langchain_openai import ChatOpenAI

# Here we are setting the environment variables for the OpenAI API key and the model name
OPENAI_BASE_URL = os.environ.get('OPENAI_BASE_URL') or None
OPENAI_MODEL_NAME = os.environ.get('OPENAI_MODEL_NAME') or 'gpt-4o-mini'
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise NotImplementedError("`OPENAI_API_KEY` is required")

# Here we are creating a dictionary with the OpenAI parameters
openai_params = {
    "model": OPENAI_MODEL_NAME,
    "api_key": OPENAI_API_KEY,
}
if OPENAI_BASE_URL:
    openai_params["base_url"] = OPENAI_BASE_URL

# Here we are creating an instance of the ChatOpenAI class with the OpenAI parameters
llm_base = ChatOpenAI(**openai_params)
