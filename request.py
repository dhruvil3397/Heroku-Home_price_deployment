import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={"Area":2600,"Bedrooms":3,"Age":20})

print(r.json())