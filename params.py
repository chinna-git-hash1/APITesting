import json

import requests



base_url="https://reqres.in/api/users"

header_test={'content-type':'application/json'}

# payload={
#     "name":"chinna",
#     "job":"QA"
# }
json_file=open('./json')
json_payload=json.load(json_file)

response= requests.post(url=base_url,headers=header_test,json=json_payload)
print(response.status_code)
print(response.json())
