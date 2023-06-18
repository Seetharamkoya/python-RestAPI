# Python REST API Example

This code 'test_api' example demonstrates how to interact with a REST API using the requests library in Python. It performs a sequence of HTTP requests, including `POST`, `PUT`, and `GET` requests, to `create`, `update`, and `retrieve` data from the API.

## Prerequisites
* Python (version 3 or above)
* requests library (install using pip install requests)

## Usage
1. The script imports the required libraries: `requests` for making HTTP requests and `uuid` for generating UUIDs.
2. The POST request is performed using r`equests.post()`, and the response is stored in the `response` variable.
3. The UUID value is extracted from the `POST` response using `response.json()['uuid']`.
4. The URL for the `PUT` request is generated based on the extracted UUID value.
5. The form data and files for the `PUT` request are updated.
6. The `PUT` request is performed using `requests.put()`, and the response is stored in the `put_response` variable.
7. The UUID value from the `PUT` response is extracted using `put_response.json()['uuid']`.
8. `POST` and `PUT` requests, including status code, method, headers, response details, and UUID values, is printed to the console.
9. The script performs a `GET` request using the UUID value obtained from the `PUT` response. The URL is generated based on the UUID.
10. The `GET` request is performed using `requests.get()`, and the response is stored in the `get_response` variable.
11. `GET` request, including status code, method, headers, and UUID value, is printed to the console.

## Test
Run `python3 test_api.py` on the terminal to check the status code and responses.
