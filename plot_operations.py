import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class PlotOperations:
    def __init__(self, weather_data):
        self.weather_data = weather_data

    def create_boxplot(self, start_year, end_year):
        selected_data = self.weather_data.loc[start_year:end_year]

        selected_data.boxplot(column=list(range(1, 13)))
        plt.title(f'Monthly Temperatures Distribution {start_year} to {end_year}')
        plt.xlabel('Month')
        plt.ylabel('Temperature (Celcius)')
        plt.show()

    def create_lineplot(self, selected_year, selected_month):
        # Extract the list for the specified year and month
        selected_data = self.weather_data.loc[selected_year, selected_month]
        days_in_month = range(1, len(selected_data) + 1)
        print(days_in_month)

        # Create a line plot
        plt.plot(days_in_month, selected_data, marker='x')
        plt.title(f'Daily Average Temperatures {selected_month}/{selected_year}')
        plt.xlabel('Day of Month')
        plt.ylabel('Average Daily Temp.')

        plt.xticks(days_in_month)

        plt.grid(True, linestyle = '--')  # Add grid
        plt.show()