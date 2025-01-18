import requests

def fetch_weather(city):
    """Fetch weather data from a public API."""
    api_key = 'ENTER_API_KEY_HERE'  # Your actual API key
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(base_url)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        
        # Extract relevant information
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        weather_description = data['weather'][0]['description']
        
        # Display the weather information
        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {weather_description.capitalize()}")
        
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    city = input("Enter the city name: ")
    fetch_weather(city)

if __name__ == "__main__":
    main()
