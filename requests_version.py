import requests

# print(requests.__version__)

print(requests.get('https://raw.githubusercontent.com/KaelenB/404_lab_venv_curl/master/requests_version.py').text)