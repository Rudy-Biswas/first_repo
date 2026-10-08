import csv

a = 0
b = 0
c = 0
d = 0
e = 0
with open("practice.csv", "r") as f:
    data = csv.reader(f)
    next(data)
    for row in data: 
        score = row[7]
        if score == '':
            print("Missing")
        else:
            score = float(score)
            if score > 0 and score <= 1:
                a = a+1
                
            elif score > 1 and score <= 2:
                b = b+1
                
            elif score > 2 and score <= 3:
                c = c+1
                
            elif score > 3 and score <= 4:
                d = d+1
                
            else:
                e = e+1
print("Number of employees with p.score <=1 is",a)
print("Number of employees with p.score <=2 but >1 is",b)
print("Number of employees with p.score <=3 but >2 is",c)
print("Number of employees with p.score <=4 but >3 is",d)
print("The number of GOAT employees",e)
                
           