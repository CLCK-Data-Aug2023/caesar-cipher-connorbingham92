# add your code here
sentence = input("please enter a sentence:") 
sentence = sentence.lower()

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] 
output = ""

for letter in sentence: 
    for i in range(0,len(alphabet)): 
        if letter == alphabet[i]: output = output + (alphabet[(i+5)%26]) 
        elif letter not in alphabet: output = output + letter 
    print(output)
