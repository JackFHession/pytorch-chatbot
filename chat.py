from brain.main import *

while True:
    sentence = input("You: ")
    response = chat(sentence)
    print(response)