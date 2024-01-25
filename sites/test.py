import requests

response = requests.get('https://intelligentbee.com/careers-ib').text

print(response)