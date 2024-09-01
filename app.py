import streamlit as st
import requests
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Access the API key
api_key = os.getenv("API_KEY")

# Function to fetch weather data
def fetch_weather_data(api_key, location):
    # API URL and headers
    url = f"https://api.tomorrow.io/v4/weather/forecast?location={location}&apikey={api_key}"
    headers = {"accept": "application/json"}

    # Making the GET request to the API
    response = requests.get(url, headers=headers)

    # Parsing the JSON response
    if response.status_code == 200:
        data = response.json()
        return data.get('timelines', {}).get('daily', [])
    else:
        st.error(f"Failed to fetch data: {response.status_code}")
        return []

# Streamlit App
st.title("Weather Forecast App")

# Input fields for location
location = st.text_input("Enter Location")

# Fetch and display weather data when the button is clicked
if st.button("Get Weather Forecast"):
    daily_forecasts = fetch_weather_data(api_key, location)

    if daily_forecasts:
        # Display only the current day's forecast
        current_forecast = daily_forecasts[0]
        
        if current_forecast:
            date = current_forecast.get('time', 'N/A')
            formatted_date = date.split('T')[0]
            temperature_max = current_forecast.get('values', {}).get('temperatureMax', 'N/A')
            temperature_min = current_forecast.get('values', {}).get('temperatureMin', 'N/A')
            humidity_avg = current_forecast.get('values', {}).get('humidityAvg', 'N/A')
            wind_speed_avg = current_forecast.get('values', {}).get('windSpeedAvg', 'N/A')
            precipitation_probability = current_forecast.get('values', {}).get('precipitationProbabilityAvg', 'N/A')

            st.subheader(f"Date: {formatted_date}")
            st.write(f"Max Temperature: {temperature_max}°C")
            st.write(f"Min Temperature: {temperature_min}°C")
            st.write(f"Average Humidity: {humidity_avg}%")
            st.write(f"Average Wind Speed: {wind_speed_avg} m/s")
            st.write(f"Precipitation Probability: {precipitation_probability}%")
        else:
            st.error("No forecast data available.")