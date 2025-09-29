import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate

load_dotenv(dotenv_path="../.env")

api_key = os.getenv("OPENAI_API_KEY")
model_name = os.getenv("MODEL_NAME")
model_url = os.getenv("MODEL_URL")

'''
# 打印env变量
print(api_key)
print(model_name)
print(model_url)
'''

model = ChatOpenAI(base_url=model_url, api_key=api_key, model=model_name)

'''
# 普通调用
messages = [
    SystemMessage(content="Translate the following from English into Chinese"),
    HumanMessage(content="Because chat models are Runnables, they expose a standard interface that includes async and streaming modes of invocation. This allows us to stream individual tokens from a chat model"),
]
'''


# 使用提示词调用
system_template = "Translate the following from English into {language}"
prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

prompt = prompt_template.invoke({"language": "Italian", "text": "hi!"})

res = model.invoke(prompt)
print(res.content)

