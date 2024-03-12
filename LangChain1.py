import os
os.environ['openai_api_key'] = "sk-74Oxb8Ej3wI0E7vHLRrKvJnjh4P0b1DING3zK6xQFg4DTXF2pV0C"
os.environ['openai_api_base'] = "http://paas-chat-api.paas.ding.paas.test.ding/v1"

from langchain_openai import ChatOpenAI
print("begin")
#直接写入的方式
#llm = ChatOpenAI(openai_api_key="sk-xxx",openai_api_base="http://xxxxx/v1")

llm = ChatOpenAI()
response = llm.invoke("hi 你好 call me baba")
print(response)
print("end2")
