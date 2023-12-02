from html.parser import HTMLParser
import requests
from datetime import date, timedelta

class WeatherScraper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_temperature_data = False
        self.current_date = None
        self.weather_data = {}

    def handle_starttag(self, tag, attrs):
        if tag == 'td' and ('class', 'daily_max_temp') in attrs:
            self.in_temperature_data = True

    def handle_data(self, data):
        if self.in_temperature_data and self.current_date:
            temperature = float(data.strip())
            if self.current_date not in self.weather_data:
                self.weather_data[self.current_date] = {'Max': None, 'Min': None, 'Mean': None}
            if 'Max' not in self.weather_data[self.current_date]:
                self.weather_data[self.current_date]['Max'] = temperature
            elif 'Min' not in self.weather_data[self.current_date]:
                self.weather_data[self.current_date]['Min'] = temperature
            elif 'Mean' not in self.weather_data[self.current_date]:
                self.weather_data[self.current_date]['Mean'] = temperature
                self.in_temperature_data = False

    def scrape_weather_data(self, start_url):
        current_date = date.today()
        while True:
            formatted_date = current_date.strftime('%Y-%m-%d')
            url = f"{start_url}&Day={current_date.day}&Year={current_date.year}&Month={current_date.month}"

            response = requests.get(url)
            if response.status_code != 200:
                break

            self.current_date = formatted_date
            self.feed(response.text)

            current_date -= timedelta(days=1)

        return self.weather_data

# Example Usage:timeframe
start_url = "https://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=27174&=2&StartYear=2020&EndYear=2016&Day=1&Year=2018&Month=7"
scraper = WeatherScraper()
weather_data = scraper.scrape_weather_data(start_url)

for date, temps in weather_data.items():
    print(f"{date}: {temps}")

    