import requests, json

apiKey = '5056c44a77f40026c9c833ec7a211060'

baseURL = "http://api.openweathermap.org/data/2.5/weather?q="

cityName = input("Enter your City : ")

completeURL = baseURL + cityName + "&appid=" + apiKey

reponse = requests.get(completeURL)

data = response.json()

print(data)

print("Current Temperature ",data["main"]["temp"])
