# beForecast - WIP

Finally, a website that tells you the weather, retrospectively. 

## What Is beForecast?

beForecast is a cutting edge technology that enables you to check the weather. Yesterday.
How many times have you wondered, if you should've brought an umbrella, last week?
beForecast is here to save you! Now you can be the king of "I told you so".

## Sounds GREAT! How Can I Use It?

Simply go to https://be-forecast.herokuapp.com/ . Enter a city and any date you want (from yesterday to last week), and just hit submit. 
You will discover all the information you ever wanted to know: Averge temperature, hourly update, and when was the sunset.
You're Welcome.

## How Can I Run This Locally?

* Clone the repository by typing:
```bash
git clone https://github.com/NogaOs/beForecast.git
```
* Install the requirements file by using command `pip install -r requirements.txt`
* Activate the virtual environment by using command `heroku\Scripts\activate.bat`
* Set the Flask application.
  * For bash, please use `set FLASK_APP=beForecast.py`
  * For powershell, please use `env FLASK_APP=beForecast.py`
* Run flask app using `flask run`
* The app should now be available on localhost, port 5000.
* That's it! :bowtie:
