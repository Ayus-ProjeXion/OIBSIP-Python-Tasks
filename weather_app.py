#Project:weather app
#Name:Ayusman Mishra
import requests
def main():
    print("Weather app by Ayusman")
    api_key="PASTE_YOUR_KEY_HERE"
    city=input("Enter city name: ")
    url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response=requests.get(url)
    data=response.json()
    if data.get("cod")==200:
        temp=data["main"]["temp"]
        desc=data["weather"][0]["description"]
        print(f"Temperature in {city}: {temp}C")
        print(f"Condition: {desc}")
    else:
        print("Error: City not found or Key not yet active.")
main()        