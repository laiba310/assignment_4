import requests

API_key = "26955221fd92d156362c7e5d2d3f82d5"  # <-- yahan apni new wali key lagao
city = input("🌆 Enter a city: ").strip()

# Base URL with proper formatting
base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units=metric"

# Send request and get data
response = requests.get(base_url)
weather_data = response.json()

# Error Handling
if response.status_code == 200:
    print(f"\n🌤️ Weather in {city.title()}:")
    print(f"🌡️ Temperature: {weather_data['main']['temp']}°C")
    print(f"☁️ Weather: {weather_data['weather'][0]['description'].title()}")
    print(f"💨 Wind Speed: {weather_data['wind']['speed']} m/s")
else:
    print("\n❌ City not found or API key is invalid!")
    print("📦 Error message:", weather_data.get("message", "Unknown error"))
