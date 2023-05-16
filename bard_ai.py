""" import bardapi
import os

os.environ['_BARD_API_KEY']= "AP8dLtzc1UMMP35JWMiUSMwwnb0KvvAIyHBjxp82-vd0KMzh09HlmpKXG1lsHmF05pPNMq0w5g"

input_text = input("Enter your prompt:")

response = bardapi.core.Bard().get_answer(str(input_text))

print(str(response)) """


from os import environ
from Bard import Chatbot

token = environ.get("AP8dLtzc1UMMP35JWMiUSMwwnb0KvvAIyHBjxp82-vd0KMzh09HlmpKXG1lsHmF05pPNMq0w5g")

chatbot = Chatbot(token)

chatbot.ask("Hello, how are you?")