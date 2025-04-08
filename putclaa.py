import requests



head={
    'accept':'text/plain'
}

response = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities/12",headers=head)

print("Before Update")
print(response.json())

headerPut={
    'accept':'text/plain',
    'Content-Type': 'application/json'
}

putpayload ={

    "id": 14,
    "title": "Lucky",
    "dueDate": "2025-04-08T09:16:14.927Z",
    "completed": True
}

print("Ofter Update")


response=requests.put("https://fakerestapi.azurewebsites.net/api/v1/Activities/12",
                      headers=headerPut,
                      json=putpayload)

print(response.json())


