import requests
url= input("Enter Valid url: ")
sql_query = input("Enter Query For Checking Error Based SQLi: ")
response = requests.get(url + sql_query)
if "error" in response.text.lower():
    print("The target URL is vulnerable to Error Based SQL injection\n")
else:
    print("The target URL is not vulnerable to Error Based SQL injection\n")

sql_query2 = input("\nEnter Query For Checking Union Based SQLi: ")
response = requests.get(url + sql_query2)
if "different number of columns" in response.text.lower():
    print("\he target URL has different number of columns\n")
else:
    print("The target URL has correct number of columns\n")


