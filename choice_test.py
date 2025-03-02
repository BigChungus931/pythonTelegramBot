message = input("Please enter a message111: ")
instruction = "Please answer shortly to that message: "
words_from_text = message.split()
print(words_from_text)
word_to_find = "short"
for word in words_from_text:
    if word == word_to_find:
        message = (instruction + message)
        break

print(message)
