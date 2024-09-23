import requests

wind = 10
temp = 2
month = 2

url = 'http://127.0.0.1:5000/modelo/Wind='+str(wind)+'&Temp='+str(temp)+'&Month='+str(month)

response = requests.get(url)

print(response.json()['predicted_Ozone'])