import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("C:/Users/Veliko/Documents/Documents/Trading/KIO.csv")

Date = df['Date']
Closing_price = df['Close']

first_rows = df.head(10)
print first_rows

graph = pd.DataFrame(Closing_price,index=Date)


fig = plt.figure()
ax1 = fig.add_subplot(111)

#First add this line to generate the graph in the background.
ax1.plot(Date, Closing_price, label="Shares")


plt.xlabel("Date")
plt.ylabel("Closing Price for Kumba Iron Ore")
plt.legend()




#ALways need to add this next line in order to actually call up what is displayed in the background.
plt.show()

