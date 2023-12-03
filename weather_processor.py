import datetime
from db_operations import DBOperations
from weather_scraper import WeatherScraper
from plot_operations import PlotOperations

import pandas as pd

class WeatherProcessor:
    def __init__(self):
        self.db_operations = DBOperations()
        self.db_operations.initialize_db()

    def display_menu(self):
        print("Weather Processor Menu:")
        print("1. Download/Update Weather Data")
        print("2. Generate Box Plot for a Year Range")
        print("3. Generate Line Plot for a Month and Year")
        print("4. Delete the database.")
        print("5. Exit")

    def download_update_weather_data(self):
        today = datetime.date.today()
        current_month, current_year = today.month, today.year

        WS = WeatherScraper()
        while True:
            # Construct the URL based on the current month and year
            url = f"https://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=27174&timeframe=2&StartYear=1840&EndYear=2023&Day=1&Year={current_year}&Month={current_month}"

            # Scraping weather data using the URL
            weather_data = WS.scrape_weather_data(url)

            # Insert data into the database
            not_done = self.db_operations.save_data(weather_data)
            
            if not not_done:
                print("Done data insertion. Stopping the process.")
                return

            # Move to the previous month and year
            current_month -= 1
            if current_month == 0:
                current_month = 12
                current_year -= 1


    def generate_box_plot(self, from_year, to_year):
        per = PlotOperations()
        df=self.db_operations.fetch_data()

        df['sample_date'] = pd.to_datetime(df['sample_date'])

        dt = pd.DataFrame()
        dt['year'] = df['sample_date'].dt.year
        dt['month'] = df['sample_date'].dt.month
        dt['val'] = df['avg_temp']

        bdf = pd.DataFrame(columns=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'])
        for i in range(to_year, from_year-1, -1):
            for j in range(1,13):
                filtered_values = dt.loc[(dt['year'] == i) & (dt['month'] == j), 'val'].tolist()
                if len(filtered_values)>0:
                    mean_val = round(sum(filtered_values) / len(filtered_values), 1)
                else:
                    mean_val=0
                bdf.at[i, j]=mean_val

        per.create_boxplot(bdf, from_year, to_year)

        

    def generate_line_plot(self, year, month):
        # Implement generating a line plot for the specified year and month
        per = PlotOperations()
        df=self.db_operations.fetch_data()
        df['sample_date'] = pd.to_datetime(df['sample_date'])
        dt = pd.DataFrame()
        dt['year'] = df['sample_date'].dt.year
        dt['month'] = df['sample_date'].dt.month
        dt['val'] = df['avg_temp']

        filtered_values = dt.loc[(dt['year'] == month) & (dt['month'] == month), 'val'].tolist()
        
        per.create_lineplot(filtered_values, year, month)

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                self.download_update_weather_data()
            elif choice == "2":
                from_year = int(input("Enter the starting year: "))
                to_year = int(input("Enter the ending year: "))
                self.generate_box_plot(from_year, to_year)
            elif choice == "3":
                year = int(input("Enter the year: "))
                month = int(input("Enter the month: "))
                self.generate_line_plot(year, month)
            elif choice=='4':
                self.db_operations.purge_data()
            elif choice == "5":
                print("Exiting the Weather Processor. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    weather_processor = WeatherProcessor()
    weather_processor.run()


