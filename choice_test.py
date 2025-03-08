message = input("Please enter a message111: ")
#instruction = "Please answer shortly to that message: "
# words_from_text = message.split()
# print(words_from_text)
# word_to_find = "short"
# for word in words_from_text:
#     if word == word_to_find:
#         message = (instruction + message)
#         break
standard_prompt = "standard_prompt: "
modified_prompt = "answer shortly: "
modified_prompt_2 = "answer thoughtfully: "
key = "*"
key_2 = "="



print(message)
first_key = message[:1]
print(first_key)

if first_key == key:
    print(modified_prompt + message[1:])

elif first_key == key_2:
    print(modified_prompt_2 + message[1:])

else:
    print(standard_prompt + message)