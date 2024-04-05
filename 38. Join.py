words = ["Hey","Subscribe","to","my channel"]

sentence = ""
for word in words:
    sentence += word + " "

print(sentence)

#You can type same code as below

sentence = " ".join(words)
print(sentence)