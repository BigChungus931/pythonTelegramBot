import requests

#r = requests.get('https://api.github.com/events')
#r = requests.post('https://httpbin.org/post', data={'key': 'value'})
data = {
    "model": "mistral",
    "prompt": "Hi, how are you?",
    "stream": False
    }
r = requests.post("http://localhost:11434/api/generate", json= data)
#curl http://localhost:11434/api/generate -d '{
  #"model": "llama3.2",
  #"prompt": "Why is the sky blue?",
  #"stream": false
#}'
print(r)