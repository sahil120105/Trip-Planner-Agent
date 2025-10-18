import requests

class WeatherForecastTool:

    def __init__(self, api_key:str):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5"

    
    def get_current_weather(self, location: str) -> dict:
        """
        Get the current weather for a given location.
        """
        try:
            url = f"{self.base_url}/weather"
            params = {
                "q": location,
                "appid": self.api_key,
            }
            response = requests.get(url, params=params)
            return response.json() if response.status_code == 200 else {}
        except Exception as e:
            raise e
        
    def get_weather_forecast(self, location:str):
        """
        Get the weather forecast for a given location.
        """
        try:
            url = f"{self.base_url}/forecast"
            params = {
                "q": location,
                "appid": self.api_key,
                "cnt": 10,
                "units": "metric"
            }
            response = requests.get(url, params=params)
            return response.json() if response.status_code == 200 else {}
        except Exception as e:
            raise e