n = int(input("Enter the number of Entries: "))
inputs = []

for i in range(n):
    x = float(input("Enter the inputs: "))
    inputs.append(x)

import math

a = sum(inputs)/n
print("The Mean of the inputs is: ",a)

inputs.sort()

if (n%2) == 0:
    median = ((inputs[int(n/2)-1] + inputs[int(n/2)])/2)
else :
    median = (inputs[int((n+1)/2)-1])
print("The Median of the inputs is: ",median)


freq = {}
unique_list = set(inputs)

for num in unique_list:
    frequency = inputs.count(num)
    freq[num] = frequency

max_value = max(freq.values())

for items in freq.keys():
    if freq[items] == max_value:
        max_element = items

print("The Mode is: ",max_element)