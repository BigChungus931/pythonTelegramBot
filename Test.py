message = "Hello, do you know what is 2+2?"
word_to_find = "short"
instructions = "Give short response to the message: "
words_from_text = message.split()
for word in words_from_text:
    #print(word)
    if word == word_to_find:
        print(instructions + message)
    elif word != word_to_find:
        print("No keyword in the message")