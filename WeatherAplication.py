import requests

def get_weather(city):
    api_key = ""  # Replace with your API key
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # To show temperature in Celsius
    }
    
    response = requests.get(base_url, params=params)
    data = response.json()
    
    if data["cod"] == 200:
        print("\n------------ Weather Information ------------")
        print(f"City: {data['name']}")
        print(f"Weather: {data['weather'][0]['main']} - {data['weather'][0]['description']}")
        print(f"Temperature: {data['main']['temp']} °C")
        print(f"Feels Like: {data['main']['feels_like']} °C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Pressure: {data['main']['pressure']} hPa")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
        print("---------------------------------------------\n")
    else:
        print("City not found! Please enter a valid city name.")

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    get_weather(city_name)
