from flask import Flask, render_template, request, redirect, url_for

from config.secret_stuff import API_KEY

from config.funcs import get_weather_data


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        date = request.form.get('date') 
        city = request.form.get('city')
        return redirect(url_for('get_weather', city=city, date=date))
    return render_template('index.html')


@app.route('/weather-in/<city>/<date>', methods=['GET', 'POST'])
def get_weather(city, date):
    city_name, country, daily_desc, avg_temp, sunset, hours = get_weather_data(city, date, API_KEY)
    return render_template(
        'result.html', 
        city_name=city_name,
        country=country,
        daily_desc=daily_desc,
        avg_temp=avg_temp,
        sunset=sunset,
        hours=hours
    )


if __name__ == "__main__":
    app.run(debug=True, threaded=True, port=5000)
