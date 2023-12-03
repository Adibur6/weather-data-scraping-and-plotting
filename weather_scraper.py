import requests
from datetime import datetime
from bs4 import BeautifulSoup
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}
class WeatherScraper():
    
    def scrape_weather_data(self,url):
        html_page=requests.get(url,headers=headers)
        soup=BeautifulSoup(html_page.content,'html.parser')
        daily_temparature={}
        header_info=soup.find_all("table",class_="table table-striped table-hover align-cells-right data-table")
        if header_info is None:
            return daily_temparature
        header_info=header_info[0]
        title=header_info.find("caption",class_="hidden-print").get_text()
        print("Importing "+title)
        table_info=header_info.find_all("tbody")[0].find_all("tr")
        for i in range(0,31):
            if table_info:
                temparature_info=table_info[i].find_all("td")
                if temparature_info or date_info:   
                    date_info=header_info.find_all("tbody")[0].find_all("tr")[i].find("th")
                    date=date_info.find("abbr")
                    if date==None:
                        break
                    MAX_temp=temparature_info[0].get_text()
                    min_temp=temparature_info[1].get_text()
                    mean_temp=temparature_info[2].get_text()
                    date=date["title"]
                    date = datetime.strptime(date, "%B %d, %Y").strftime("%Y-%m-%d")

                   
                    temparature={"Max":MAX_temp,"Min":min_temp,"Mean":mean_temp}
                    daily_temparature[date]=temparature
                else:
                    continue
            
            else:
                print("Do not have the temparature data")
        daily_temparature = {date: {key: ''.join('0' if c.isalpha() else c for c in value) for key, value in data.items()} for date, data in daily_temparature.items()}
        daily_temparature = {date: {key: float(value) if value.replace('.', '', 1).isdigit() else 0 for key, value in data.items()} for date, data in daily_temparature.items()}

        return daily_temparature

    
