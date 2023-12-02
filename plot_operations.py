import matplotlib.pyplot as plt
from db_operations import DBOperations
import pandas as pd
fetch=DBOperations()
class PlotOperations:
    def Ploting(self):
        fetched_data=fetch.fetch_data()
        plt.figure(figsize=(10, 6))
        plt.boxplot(fetched_data,x_label=fetched_data["sample_date"],y=fetched_data["max_temp"])
        plt.title('Box Plot of Max Temperature by Date')
        plt.xlabel('Max Temperature')
        plt.ylabel('Date')
        plt.show()
plot=PlotOperations()
plot.Ploting()
        

    
    
    
    
    
    
    
    
    