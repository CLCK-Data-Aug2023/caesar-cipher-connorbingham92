cipher = {}
for i in range(97,123):
    cipher[chr(i)] = chr((i+5) % 123 + 97*((i+5)//123))

output = ""
sentence = input("Please enter a sentence: ")
for letter in sentence:
    
    if letter in cipher.keys():
        output += cipher[letter]
    else:
        output += letter

    print(output)
# add your code here
