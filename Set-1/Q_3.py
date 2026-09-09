n = [1,1,1,2,3,4,5,6,7,6,7,6,9,6,9,8,8]
no_d = set(n)

for i in no_d:
    if n.count(i)>1:
        print("The duplicate elements: ", str(i) + ", Number of clones: ", n.count(i))

max = n[0]
min = n[0]

for num in no_d:
    if num>max:
        max = num
    if num<min:
        min = num

print("The Max Value is: ", max, "and The Min Value is: ", min)



    