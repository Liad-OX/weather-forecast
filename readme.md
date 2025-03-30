**⚠️ DISCLAIMER:**  
This repository and associated scripts are **strictly for research and educational purposes only**.  
It includes intentionally vulnerable code demonstrating how sensitive information could be exfiltrated from within a seemingly benign utility that developers might download and use from GitHub repositories.  
**DO NOT** use or execute this code in any production or real-world environment.
The exfiltration attempt fails silently, ensuring the end user remains unaware of malicious activity, strictly for demonstrating potential vulnerabilities.

# Weather Forecast Utility

A simple and lightweight Python utility that allows you to fetch current weather forecasts from OpenWeatherMap easily. Integrate weather information into your apps seamlessly, using customizable geographic coordinates.

---

## 🌤 Features

- Fetches current weather data easily via OpenWeatherMap API.
- Supports default location (San Francisco – Moscone Center) or custom coordinates.
- Easy setup with environment variables or direct API key injection.
- Robust logging and clear error handling.

---

## 📂 Project Structure

- `weather_forecast.py`: Core Python script containing the utility.
- `.env.example`: Template for setting your OpenWeatherMap API key.
- `requirements.txt`: List of dependencies for easy installation.

---

## 🚀 Installation & Setup

Clone the repository:

    git clone <your-repo-url>
    cd weather-forecast-utility

Install dependencies:

    pip install -r requirements.txt

Configure your API key by copying `.env.example` to `.env`:

    cp .env.example .env

Then, edit `.env` to set your OpenWeatherMap API key:

    OWM_API_KEY=your_openweathermap_api_key_here

Alternatively, you can pass your API key directly into the Python class.

---

## ⚙️ Usage Example

Basic usage:

    from weather_forecast import WeatherForecast

    forecast = WeatherForecast()
    weather_data = forecast.get_current_weather()
    print(weather_data)

Custom coordinates (example for New York City):

    ny_weather = forecast.get_current_weather(lat=40.7128, lon=-74.0060)
    print(ny_weather)

Direct API key injection without `.env`:

    forecast = WeatherForecast(api_key="your_openweathermap_api_key_here")
    print(forecast.get_current_weather())

---

## 🛠 Available Weather Data

The utility provides a JSON response including:

- Weather description
- Current temperature
- Feels-like temperature
- Min/Max temperature
- Atmospheric pressure
- Humidity percentage
- Wind speed and direction
- Sunrise and sunset times
- Country code

---

## 🤝 Contributing

Feel free to open issues or submit pull requests to improve the utility.

---

## 📄 License

MIT License
