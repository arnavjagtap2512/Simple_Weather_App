# Simple Weather App

This is a simple weather app built with Streamlit. It uses the Tomorrow.io API to show the daily weather forecast for a specific location.

## Features

- Shows the current day’s weather forecast.
- Displays max and min temperatures, average humidity, wind speed, and precipitation chance.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Streamlit
- Requests library

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/arnavjagtap2512/Simple_Weather_App.git
    cd Simple_Weather_App
    ```

2. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up your API key:**

   - Create a `.env` file in the root directory.
   - Add your Tomorrow.io API key to the `.env` file like this:

    ```plaintext
    API_KEY=your_api_key_here
    ```

4. **Run the app:**

    ```bash
    streamlit run app.py
    ```

## Usage

- Enter the location for which you want the weather forecast.
- Click the button to get the forecast for the current day.