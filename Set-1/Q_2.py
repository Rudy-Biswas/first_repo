sentence = input("Write the sentence: ")
word_list = sentence.split()
y = False

for word in word_list:
     y = False
     for char in word:
       
        if y == False:
            if char in "aeiouAEIOU":
                 print(word)
                 y = True
            
        else:
            break

print(len(word_list))