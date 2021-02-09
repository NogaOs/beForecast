import requests

from typing import Tuple, List


def get_weather_data(city: str, date: str, api_key: str) -> Tuple[str, str, str, str, str]:
    r = requests.get(f'http://api.weatherapi.com/v1/history.json?key={api_key}&q={city}&dt={date}')
    resp = r.json()

    city_name = resp["location"]["name"]
    country = resp["location"]["country"]
    data = resp["forecast"]["forecastday"][0]
    daily_desc = data["day"]["condition"]["text"]
    avg_temp = data["day"]["avgtemp_c"]
    sunset = data["astro"]["sunset"]
    hours = data["hour"]

    return (
        city_name,
        country,
        daily_desc,
        avg_temp,
        sunset,
        hours
    )


# def get_hourly_data(hour_json):  
#     return [
#         {
#             'time': hour["time"].split(" ")[1],
#             'c': hour["temp_c"],
#             'desc': hour["condition"]["text"]
#         }
#         for hour in hour_json
#     ]