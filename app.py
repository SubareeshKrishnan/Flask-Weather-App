from flask import Flask, render_template, request
import requests
import configparser

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

def get_weather_results(zip_code, api_key):
    api_url = "https://api.openweathermap.org/data/2.5/weather?zip={}&units=metric&appid={}".format(zip_code, api_key)
    r = requests.get(api_url)
    return r.json()

@app.route('/result', methods=['POST'])
def weatherDashboard():
    zip_code = request.form['zipCode']
    api_key = "0154108295612a02bd735e466e7436ea"
    data = get_weather_results(zip_code, api_key)
    temp = '{0:.2f}'.format(data['main']['temp'])
    feels = '{0:.2f}'.format(data['main']['feels_like'])
    weather = data['weather'][0]['main']
    location = data['name']
    return render_template('weather.html', weather=weather, location=location, feels=feels, temp=temp, tempCmp=int(float(temp)))

@app.errorhandler(500)
def error_500(error):
    return render_template('500.html') , 500

if __name__ == '__main__':
    app.run()
