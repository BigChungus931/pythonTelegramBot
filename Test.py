import requests

message = input("Please enter a message:")
word_to_find = "short"
instructions = "Give short response to the message: "
words_from_text = message.split()
print(words_from_text)
for word in words_from_text:
    #print(word)
    if word == word_to_find:
        print(instructions + message)
        data = {
            "model": "mistral",
            "prompt": instructions + message,
            "stream": False
        }
        r = requests.post("http://localhost:11434/api/generate", json=data)

        response = r.json()
        response_text = response.get("response", "answer not received")
        print(response_text)
        break
    elif word != word_to_find:
        print(message)
        data = {
            "model": "mistral",
            "prompt": message,
            "stream": False
        }
        r = requests.post("http://localhost:11434/api/generate", json=data)

        response = r.json()
        response_text = response.get("response", "answer not received")
        print(response_text)
