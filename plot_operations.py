import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class PlotOperations:
    def create_boxplot(self, weather_data, start_year, end_year):
        selected_data = weather_data
        selected_data.boxplot(column=list(range(1, 13)))
        plt.title(f'Monthly Temperatures Distribution {start_year} to {end_year}')
        plt.xlabel('Month')
        plt.ylabel('Temperature (Celsius)')
        plt.show()
       

    def create_lineplot(self, weather_data, selected_year, selected_month):
        # Extract the list for the specified year and month
        selected_data = weather_data
        days_in_month = range(1, len(selected_data) + 1)

        # Create a line plot
        plt.plot(days_in_month, selected_data, marker='x')
        plt.title(f'Daily Average Temperatures {selected_month}/{selected_year}')
        plt.xlabel('Day of Month')
        plt.ylabel('Average Daily Temp.')

        plt.xticks(days_in_month)

        plt.grid(True, linestyle = '--')  # Add grid
        plt.show()