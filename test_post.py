import requests

url = 'http://apitestfs.zapto.org:8080/api/v1/assets/model/'

# Create the form data
form_data = {
    'meta': '{"name": "ksr"}',
    'folder': 'python-RestApi'
}

# Create a fields and their paths
files = {
    'asset': ('test.txt', open('test.txt', 'rb'))
}

#response
response = requests.post(url, data=form_data, files=files)

print('POST Request:')
print('Status Code:', response.status_code)
print('Method:', response.request.method)
print('Headers:', response.request.headers)
print('Response:', response.json())
print('uuid:', response.json()['uuid'])

