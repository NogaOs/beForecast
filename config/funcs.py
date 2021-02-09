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


def sub_title_gene():
    sentences = (
        "See if it was a good idea to go on that trip, yesterday.",
        "See what's the best time to go to London, last year.",
        "See if you should've taken an umbrella, last night."
    )
    i = 0
    while True:
        yield sentences[i]
        i = (i + 1) % len(sentences)


title_gene = sub_title_gene()


def get_sentence() -> str:
    return next(title_gene)


# def get_hourly_data(hour_json):  
#     return [
#         {
#             'time': hour["time"].split(" ")[1],
#             'c': hour["temp_c"],
#             'desc': hour["condition"]["text"]
#         }
#         for hour in hour_json
#     ]