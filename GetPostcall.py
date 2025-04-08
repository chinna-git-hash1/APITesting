import requests

header={
    'accept':'text/plain',
    'Content-Type':'application/json'
}

request_payload = {
    "id": 0,
    "title": "china api testing",
    "dueDate": "2025-04-08T07:48:05.233Z",
    "completed": True
}

response = requests.post("https://fakerestapi.azurewebsites.net/api/v1/Activities",
                         headers=header,
                         json=request_payload)
print(response.status_code)
print(response.json())

assert response.status_code==200
