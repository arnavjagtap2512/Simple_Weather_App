import streamlit as st
import requests
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Access the API key
api_key = os.getenv("API_KEY")

# Function to fetch real-time weather data
def fetch_realtime_weather(api_key, location):
    # API URL and headers
    url = f"https://api.tomorrow.io/v4/weather/realtime?location={location}&apikey={api_key}"
    headers = {"accept": "application/json"}

    # Making the GET request to the API
    response = requests.get(url, headers=headers)

    # Parsing the JSON response
    if response.status_code == 200:
        data = response.json()
        return data.get('data', {}).get('values', {})
    else:
        st.error(f"Failed to fetch data: {response.status_code}")
        return {}

# Streamlit App
st.title("Real-Time Weather App")

# Input fields for location
location = st.text_input("Enter Location")

# Fetch and display real-time weather data when the button is clicked
if st.button("Get Real-Time Weather"):
    weather_data = fetch_realtime_weather(api_key, location)

    if weather_data:
        temperature = weather_data.get('temperature', 'N/A')
        humidity = weather_data.get('humidity', 'N/A')
        wind_speed = weather_data.get('windSpeed', 'N/A')
        precipitation_probability = weather_data.get('precipitationProbability', 'N/A')
        uv_index = weather_data.get('uvIndex', 'N/A')
        visibility = weather_data.get('visibility', 'N/A')

        st.write(f"Temperature: {temperature}°C")
        st.write(f"Humidity: {humidity}%")
        st.write(f"Wind Speed: {wind_speed} m/s")
        st.write(f"Precipitation Probability: {precipitation_probability}%")
        st.write(f"UV Index: {uv_index}")
        st.write(f"Visibility: {visibility} km")
    else:
        st.error("No real-time weather data available.")
