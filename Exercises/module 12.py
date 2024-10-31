#1 Write a program that fetches and prints out a random Chuck Norris joke for the user. Use the API presented here: https://api.chucknorris.io/. The user should only be shown the joke text.
import requests
import json
user = input("Enter for new joke: ")
while user=="":
    request = "https://api.chucknorris.io/jokes/random"
    response = requests.get(request).json()
    print(response["value"])
    user = input("Enter for new joke or type 'exit' to exit: ")
    if user=="exit":
        break


#2 Familiarize yourself with the OpenWeather weather API at: https://openweathermap.org/api. Your task is to write a program that asks the user for the name of a municipality and then prints out the corresponding weather condition description text and temperature in Celsius degrees. Take a good look at the API documentation. You must register for the service to receive the API key required for making API requests. Furthermore, find out how you can convert Kelvin degrees into Celsius.
import requests
city_name = input("Enter municipality : ")
request3 = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=cf7d627164d523cc8b25fb096c74c299&units=metric"
response3 = requests.get(request3).json()
print(response3["weather"][0]["description"])
print(response3["main"]["temp"], "degrees Celsius")
