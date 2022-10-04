import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv")
plt.scatter(data['Mortality rate, infant (per 1,000 live births)'], data["GDP per capita (constant 2010 US$)"])
plt.show()


#chwiugcv