import requests

url = "http://127.0.0.1:11434/api/chat"

history = [
    {
        "role": "system",
        "content": "You are a helpful assistant"
    }
]

while True:

    user_query = input("\nUser : ")

    if user_query == "q":
        break

    user_message = {
        "role": "user",
        "content": user_query
    }

    history.append(user_message)

    payloads = {
        "model": "llama3:latest",
        "messages": history,
        "stream": False
    }

    response = requests.post(url, json=payloads)

    data = response.json()

    bot_message = data["message"]

    history.append(bot_message)

    print("\nBot :", bot_message["content"])