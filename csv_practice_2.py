import csv

with open("practice.csv", "r") as q:
    data = csv.reader(q)
    next(data)
    a = []
    yoe = []
    for row in data:
        if row[6] == '':
            print("MISSING")
        else:
           yoe.append(float(row[6]))
    avg = sum(yoe)/len(yoe)
    print(avg)
    for row in data:
        if row[6] == '':
            print("MISSING")
        else:
            if float(row[6]) > avg:
                a.append(row)
                print("Experienced Employee")
            else:
                pass
            

with open("export.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["Employee_ID","First_Name","Last_Name","Age","Department","Salary","Years_of_Experience","Performance_Score","Joining_Date"])
    writer.writerows(a)