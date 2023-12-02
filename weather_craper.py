from db_operations import  DBOperations
import requests
from datetime import datetime
from bs4 import BeautifulSoup
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}
class WeatherScraper():
    
    def scrape_weather_data(self,url):
        html_page=requests.get(url,headers=headers)
        soup=BeautifulSoup(html_page.content,'html.parser')
        header_info=soup.find_all("table",class_="table table-striped table-hover align-cells-right data-table")[0]
        title=header_info.find("caption",class_="hidden-print").get_text()
        print(title)
        table_info=header_info.find_all("tbody")[0].find_all("tr")
        daily_temparature=[]
        for i in range(0,30):
            if table_info:
                temparature_info=table_info[i].find_all("td")
                if temparature_info or date_info:   
                    MAX_temp=temparature_info[0].get_text()
                    min_temp=temparature_info[1].get_text()
                    mean_temp=temparature_info[2].get_text()
                    date_info=header_info.find_all("tbody")[0].find_all("tr")[i].find("th")
                    date=date_info.find("abbr")["title"]
                    temparature={"Date":date,"Max":MAX_temp,"Min":min_temp,"Mean":mean_temp}
                    daily_temparature.append(temparature)
                else:
                    continue
            
            else:
                print("Do not have the temparature data")
        return daily_temparature
# data scrape by date    
url="https://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=27174&timeframe=2&StartYear=2020&EndYear=2016&Day=1&Year=2018&Month=7"
scraper = WeatherScraper()
db=DBOperations()
weather_data = scraper.scrape_weather_data(url)
date_format = "%B %d, %Y"
for data in weather_data:
    print(data)
    max=float(data["Max"])
    min=float(data["Min"])
    avg_data=float((max+min)/2)
    date=data["Date"]
    datetime= datetime.strptime(date,date_format)
    db.save_data(datetime,min,max,avg_data)
    
