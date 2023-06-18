import requests
import uuid

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

# Perform the POST request
response = requests.post(url, data=form_data, files=files)

# Extract the UUID value from the response (POST)
uuid_value = response.json()['uuid']

# Generate the URL for the PUT request
put_url = f'http://apitestfs.zapto.org:8080/api/v1/assets/model/{uuid_value}'

# Update the form data and files for the PUT request
updated_form_data = {
    'meta': '{"name": "updated-ksr"}',
    'folder': 'python-RestApi'
}

updated_files = {
    'asset': ('updated_test.txt', open('updated_test.txt', 'rb'))
}

# Perform the PUT request
put_response = requests.put(put_url, data=updated_form_data, files=updated_files)

# Extract the UUID value from the response (PUT)
put_value = put_response.json()['uuid']

print('POST Request:')
print('Status Code:', response.status_code)
print('Method:', response.request.method)
print('Headers:', response.request.headers)
print('Response:', response.json())
print('uuid:', uuid_value)

print('PUT Request:')
print('Status Code:', put_response.status_code)
print('Method:', put_response.request.method)
print('Headers:', put_response.request.headers)
print('Response:', put_response.json())
print('uuid:', put_value)


#GET Method
# Generate the URL for the GET request
get_url = f'http://apitestfs.zapto.org:8080/api/v1/assets/model/{put_value}'

# Perform the GET request
get_response = requests.get(get_url)
# Print the details and response of the GET request
print('GET Request:')
print('Status Code:', get_response.status_code)
print('Method:', get_response.request.method)
print('Headers:', get_response.request.headers)
print('uuid:', put_value)


