from db_operations import DBOperations
from weather_procesor import WeatherScraper

class WeatherProcessor:
    def __init__(self):
        self.db_operations = DBOperations()
        sel.

    def display_menu(self):
        print("Weather Processor Menu:")
        print("1. Download Full Set of Weather Data or ")
        print("2. Update Weather Data")
        print("3. Generate Box Plot for a Year Range")
        print("4. Generate Line Plot for a Month and Year")
        print("5. Exit")

    def download_full_set(self):
        # Implement downloading the full set of weather data
        pass

    def update_weather_data(self):
        # Implement updating weather data without duplicating
        pass

    def generate_box_plot(self, from_year, to_year):
        # Implement generating a box plot for the specified year range
        pass

    def generate_line_plot(self, year, month):
        # Implement generating a line plot for the specified year and month
        pass

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                self.download_full_set()
            elif choice == "2":
                self.update_weather_data()
            elif choice == "3":
                from_year = int(input("Enter the starting year: "))
                to_year = int(input("Enter the ending year: "))
                self.generate_box_plot(from_year, to_year)
            elif choice == "4":
                year = int(input("Enter the year: "))
                month = int(input("Enter the month: "))
                self.generate_line_plot(year, month)
            elif choice == "5":
                print("Exiting the Weather Processor. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    weather_processor = WeatherProcessor()
    weather_processor.run()
