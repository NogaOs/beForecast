from flask import Flask, render_template, request, redirect, url_for

from config.funcs import get_weather_data, get_sentence, get_error_message, get_date_field_data

from decouple import config

import requests


app = Flask(__name__)
app.secret_key = config('SECRET_KEY')
API_KEY = config('API_KEY')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        date = request.form.get('date') 
        city = request.form.get('city')
        return redirect(url_for('get_weather', city=city, date=date))
        
    sub_title = get_sentence()
    date_of_week_ago, yesterdate = get_date_field_data()
    return render_template(
        'index.html', 
        sub_title=sub_title,
        value=yesterdate,
        max=yesterdate,
        min=date_of_week_ago
    )


@app.route('/weather-in/<city>/<date>', methods=['GET', 'POST'])
def get_weather(city, date):
    
    if request.method == 'POST':
        date = request.form.get('date') 
        city = request.form.get('city')
        return redirect(url_for('get_weather', city=city, date=date))

    r = requests.get(f'http://api.weatherapi.com/v1/history.json?key={API_KEY}&q={city}&dt={date}')
    resp_code = r.status_code

    if resp_code != 200:
        error_message = get_error_message(r, resp_code, city, date)
        return render_template('error-400.html', error_message=error_message)

    city_name, country, daily_desc, avg_temp, sunset, hours = get_weather_data(r, city, date, API_KEY)
    return render_template(
        'result.html', 
        city_name=city_name,
        country=country,
        daily_desc=daily_desc,
        avg_temp=avg_temp,
        sunset=sunset,
        hours=hours
    )


@app.errorhandler(404)
def page_not_found(e):
    return "404! Should link to index."  # TODO


@app.errorhandler(500)
def internal_server_error(e):
    return "Oh no! Working on it."


if __name__ == "__main__":
    app.run(debug=True, threaded=True, port=5000)
