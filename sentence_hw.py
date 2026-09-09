sentence = input("Write the desired sentence: ")
word_list = sentence.split()

total = 0
for word in word_list:
    total = total + len(word)

print(total)

vc = 0
vowel = "aeiouAEIOU"
for char in sentence:
    if char in vowel:
        vc = vc + 1

print("Number of vowels: ", vc)
