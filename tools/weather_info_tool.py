import os
from typing import Any, Dict, Optional, List
from dotenv import load_dotenv
from langchain.tools import tool
from utils.weather_info import WeatherForecastTool
from datetime import datetime


class WeatherInfoTool:

    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("OPENWEATHERMAP_API_KEY")
        self.weather_service = WeatherForecastTool(self.api_key)
        self.weather_tool_list = self._setup_tools()

    def _setup_tools(self) -> List:
        """Setup all the tools for the weather forecast tools"""

        @tool
        def get_current_weather(location: str) -> str:
            """
            Get the current weather for a given city.
            """
            weather_data = self.weather_service.get_current_weather(location)
            if weather_data:
                temp = weather_data.get("main", {}).get("temp","N/A")
                desc = weather_data.get("weather", [{}])[0].get("description", "N/A")
                return f"The current weather in {location}: {temp}°C, {desc}"
            return f"Could not retrieve weather data for {location}."
        
        @tool
        def get_weather_forecast(location: str) -> str:
            """
            Get the weather forecast for a given city.
            """
            forecast_data = self.weather_service.get_weather_forecast(location)
            if forecast_data and 'list' in forecast_data:
                forecast_summary = []
                for i in range(len(forecast_data['list'])):
                    item = forecast_data['list'][i]
                    date = datetime.fromtimestamp(item['dt']).strftime('%Y-%m-%d %H:%M:%S')
                    temp = item['main']['temp']
                    desc = item['weather'][0]['description']
                    forecast_summary.append(f"{date}: {temp} degree celcius , {desc}")
                return f"Weather forecast for {location}:\n" + "\n".join(forecast_summary)
            return f"Could not fetch forecast for {location}"
    
        return [get_current_weather, get_weather_forecast]