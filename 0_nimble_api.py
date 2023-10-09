import base64
import requests

auth = 'username@example.com:yourpassword'
encoded_bytes = base64.b64encode(auth.encode('utf-8'))

# Convert the bytes to a string
nimble_auth = encoded_bytes.decode('utf-8')
# print(nimble_auth)

url = 'https://api.webit.live/api/v1/realtime/web'
headers = {
    'Authorization': f'Basic {nimble_auth}',
    'Content-Type': 'application/json'
}
data = {
    # Add your parameters here
    "url": "https://www.octachart.com",
    "method": "GET",
    "parse": False,
    "render": True,
    "country": "CA",
    "locale": "en-GB",
    "headers": {
        "Some-Extra-Header": "Some-Extra-Header"
    }
}

response = requests.post(url, headers=headers, json=data)

print("NIMBLE STATUS ", response.status_code)
# print(response.json())
