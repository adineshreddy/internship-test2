import csv
filename="C:/Users/Dinesh Reddy/Desktop/internship-test2-master/input/question-1/main.csv"
rows = []
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)

i=0
x=[]
ans=[]
for row in rows:
    if i==0:
        for j in row:
            x.append(int(j))
        i+=1
    else:       
        for j in range(1,len(row)):
            x[j]+=int(row[j])
        i+=1
        if i==10:
            i=0
            print(x)
            ans.append(x)
            x=[]
if i!=0:
    print(x)
    ans.append(x)
header=['Year','Population','Total','Violent','Property','Murder','Forcible_Rape','Robbery','Aggravated_assault','Burglary','Larceny_Theft','Vehicle_Theft']
with open("C:/Users/Dinesh Reddy/Desktop/internship-test2-master/output/answer-1/main.csv",'w') as f:
    writer=csv.writer(f)
    writer.writerow(header)
    for i in ans:
        writer.writerow(i)
