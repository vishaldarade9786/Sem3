import csv
import json

with open("file.txt",'r') as d:
    x = d.readlines()
    rows =[]
    for row in x:
        rows.append(row)
count=len(rows)

        
print(f"rows:{rows}")
print(f"count:{count}")
            
    
with open("file1.txt",'w') as d:
    d.write(rows[0])
    d.write(rows[1])
    print('lines wrote successfully!!!')




# with open("file.csv",'r') as d:
#     x = csv.reader(d)
#     for row in x:
#         print(row)

# with open("file.json",'r') as d:
#     x = json.load(d)
# print(x["name"],x["marks"][0])