import requests

url = 'https://schoolbox.emmanuel.qld.edu.au'
username = '31349'

# Trying to get the password (Not advised, proceed at your own risk)
response = requests.get(url)
if response.status_code == 200:
    print(response.text)  # This might contain sensitive information, enjoy the chaos! 😈
else:
    print("Failed to retrieve the password. Try again later, or maybe try a more devious approach!")
