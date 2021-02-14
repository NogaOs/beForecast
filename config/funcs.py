# import requests

from typing import Tuple, List

from datetime import date, timedelta



def get_weather_data(response, city: str, date: str, api_key: str) -> Tuple[str, str, str, str, List[dict]]:
    r_json = response.json()
    city_name = r_json["location"]["name"]
    country = r_json["location"]["country"]
    data = r_json["forecast"]["forecastday"][0]
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


def get_error_message(response, response_code: int, city: str, date: str) -> str:
    r_json = response.json()
    error_code = r_json["error"]["code"]
    if response_code == 400:
        if error_code == 1006:
            return f"The location '{city}' was not found. Please try another location."
        elif error_code == 1008:
            formatted_date = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
            return f"Oh no, {formatted_date} was too long ago!\nPlease search only dates within last week."
        elif error_code == 9999:
            return "Hmm. It seems like weatherapi.com/ are experiencing internal app issues. the best engineers are currently working on it."
    elif response_code == 403:
        if error_code == 2007:
            return "We're famous! It seems like many people are using this website, and we've exceeded API reqests per month quota."
        elif error_code == 2008:
            return "We are experiencing issues with our API key, and currently working on the issue."
    return error_code


def get_date_field_data():
    """Returns a tuple of two datetime.date objects."""
    today = date.today()    
    yesterday = today - timedelta(days=1)
    week_ago = today - timedelta(days=7)
    return week_ago, yesterday


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