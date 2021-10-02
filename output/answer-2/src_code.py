import csv
filename="C:/Users/Dinesh Reddy/Desktop/internship-test2-master/input/question-2/main.csv"

#reading
rows = []
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)

#task
from collections import defaultdict
d=defaultdict(list)
for row in rows:
    if d[row[3]]==[]:
        d[row[3]]=[int(row[1]),int(row[1])]
    else:
        d[row[3]][0]=min(int(row[1]),d[row[3]][0])
        d[row[3]][1]=max(int(row[1]),d[row[3]][1])
        
ans=[]
for i in d.keys():
    ans.append([i,d[i][0],d[i][1]])

#writing
header=['occupation','min','max']
with open("C:/Users/Dinesh Reddy/Desktop/internship-test2-master/output/answer-2/main.csv",'w') as f:
    writer=csv.writer(f)
    writer.writerow(header)
    for i in ans:
        writer.writerow(i)
