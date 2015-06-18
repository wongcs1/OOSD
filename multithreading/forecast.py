__author__ = 'cwong_000'

import threading
import urllib2
import json


class QueryCityForecast(threading.Thread):

    METSERVICE_BASE = 'http://metservice.com/publicData/'
    LOCAL_FORECAST = 'localForecast'

    def __init__(self, city):
        threading.Thread.__init__(self)
        self.city = city.lower()
        self.forecast = {}

    def get_response(self, url):
        try:
            response = urllib2.urlopen(url)
        except urllib2.HTTPError:
            self.forecast = {}
        self.forecast = json.loads(response.read())

    def get_forecast(self):
        try:
            weekdays = self.forecast["Days"]
            today = weekdays[0]
            weather_description = today["Forecast"]
            return weather_description
        except TypeError:
            return "No info available!"


if __name__ == "__main__":
    cities = []
    forecasts = []

    print("Please enter 3 NZ city names"
    #asking the user to input 3 NZ city names
    for i in range(3):
        city = raw_input("Please enter a city: ")
        current = QueryCityForecast(city)
        url = current.METSERVICE_BASE + current.LOCAL_FORECAST + city
        current.start()
        current.get_response(url)
        forecasts.append(current)

    for forecast in forecasts:
        forecast.join()
        city_formatting = forecast.city[0].upper() + forecast.city[1:]
        print(city_formatting + ": " + forecast.get_forecast())
