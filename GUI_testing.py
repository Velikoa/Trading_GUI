import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as pltdate
import datetime
from itertools import islice
import csv
from cStringIO import StringIO
import numpy as np
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates

kio_excel = "KIO.xlsx"
df = pd.read_excel(kio_excel, na_values=["NA"])
#df = pd.read_excel("KIO-excel")
#pd.read_excel()
#df.head()

sio = StringIO()
#
# with open("USD-ZAR.csv") as exchange_file:
#     for line in exchange_file:
#         if not line.startswith(("The Value", "Description", "Rand")):
#             sio.write(line)

#sio.seek(0)  #Rewind to the beginning of the StringIO object

#NB!!! Not that skipped the first 3 rows - but starting from row number 0.
#df1 = pd.read_csv("USD-ZAR.csv", sep=",", index_col=False, skiprows=3)    #Index column = false to ensure that python does not think first col. is the index col.
# def forex_file():
#     with open("USD-ZAR.csv", "r+") as exchange_file:
#         for row in islice(csv.reader(exchange_file), 3, 256, None):
#             sio.write(row)
#
# sio.seek(0)
forex_excel = "STD.xls"
df1 = pd.read_excel(forex_excel, na_values=["NA"])

#Opening the excel file for the iron ore prices
df2 = pd.read_excel("IronOrePrices.xlsx", na_values=["NA"])

kio_close = pd.DataFrame(df.Close)

dates = df["Date"]
dates1 = df1["Date"]
exchange = df1["Exchange"]
ore_price = df2["ORE"]

#x_ma = [datetime.datetime.strptime(d, "%Y-%m-%d").date() for d in dates]    #Use capital Y to parse 4 digit year format
#y_ma = range(len(x_ma))

#x_currency = [datetime.datetime.strptime(d, "%Y-%m-%d").date() for d in dates1]



def price_over_one_year():
    df = pd.read_excel("KIO.xlsx")

    dates = df["Date"]
    closing_prices = df["Close"]
    volume = df["Volume"]

    fig = plt.figure()
    ax1 = fig.add_subplot(111)

    y = closing_prices

    #Can change "plot" to "scatter" if want a scatter plot.
    ax1.plot(dates, y, label="Shares")

    # Adding the volume to the graph as a histogram
    ax2 = ax1.twinx()
    ax2.bar(dates, volume, label="Volume")

    plt.title("Kumba Iron Ore Share Price Over the past Year with Volume")
    plt.xlabel("Date")
    plt.ylabel("Share Prices")
    plt.legend()

    #Always need this in order to draw the graph on screen!
    plt.show()

price_over_one_year()

#Calculating moving averages
def moving_averages():
    kio_close["MA_9"] = kio_close.Close.rolling(9).mean()
    kio_close["MA_21"] = kio_close.Close.rolling(21).mean()

    plt.gca().xaxis.set_major_formatter(pltdate.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(pltdate.DayLocator())

    plt.Figure(figsize=(15,10))
    plt.grid(True)
    plt.plot(dates, kio_close["Close"], label="KIO")
    plt.plot(dates, kio_close["MA_9"], label= "MA 9 day")
    plt.plot(dates, kio_close["MA_21"], label= "MA 21 day")
    plt.legend(loc=2)
    plt.show()

#print kio_close["MA_9"].head(12)  #Notice how the data starts showing from number 8 - meaning the 9th day is included in sma.
#can use ".shift()" to start from 10th day.

#Calculating the EMA
def EMA():
    kio_close["MA_9"] = kio_close.Close.rolling(9).mean()
    kio_close["MA_21"] = kio_close.Close.rolling(21).mean()

    #Need to use the new df.ewm function now that the old pd.ewma is deprecated.
    #EMA_12 = pd.ewma(df["Close"], span=12, adjust=True)
    EMA_12 = df["Close"].ewm(ignore_na=False,span=12, adjust=True).mean()
    #EMA_26 = pd.ewma(df["Close"], span=26, adjust=True)
    EMA_26 = df["Close"].ewm(ignore_na=False, span=26, adjust=True).mean()

    plt.gca().xaxis.set_major_formatter(pltdate.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(pltdate.DayLocator())


    plt.grid(True)
    plt.plot(dates, kio_close["Close"], label="KIO")
    plt.plot(dates, EMA_12, label="12 day EMA")
    plt.plot(dates, EMA_26, label="26 day EMA")
    plt.legend(loc=2)
    plt.show()

#Calculating the MACD
def MACD():
    #EMA_12 = pd.ewma(df["Close"], span=12, adjust=True)
    EMA_12 = df["Close"].ewm(ignore_na=False, span=12, adjust=True).mean()
    #EMA_26 = pd.ewma(df["Close"], span=26, adjust=True)
    EMA_26= df["Close"].ewm(ignore_na=False, span=26, adjust=True).mean()

    MACD_line = EMA_12 - EMA_26
    #signal_line = pd.ewma(MACD_line, span=9, adjust=True)
    #The old pd.ewma has been deprecated so need to use this newe formula now.
    signal_line = MACD_line.ewm(ignore_na=False, span=9, adjust=True).mean()

    plt.gca().xaxis.set_major_formatter(pltdate.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(pltdate.DayLocator())

    plt.grid(True)
    plt.plot(dates, MACD_line, label="MACD line")
    plt.plot(dates, signal_line, label="Signal line")
    plt.legend(loc=2)
    plt.show()

def share_vs_currency():

    fig = plt.figure()
    ax = fig.add_subplot(111)
    colorkio = plt.cm.viridis(0)
    colorexchange = plt.cm.viridis(0.5)
    ax.plot(dates, kio_close, "-", label="KIO Share Price", color=colorkio)
    #Where to place the legend
    ax.legend(loc=0)
    ax.set_xlabel("Date - 1 Year Period")
    ax.set_ylabel("Share Price")

    ax2 = ax.twinx()
    ax2.plot(dates, exchange, "-", label="USD-ZAR Exchange Rate", color=colorexchange)
    ax2.set_ylabel("USD-ZAR Exchange Rate")

    # plt.title("USD:ZAR currency movements over 1 year")
    plt.show()

def iron_ore_price_vs_share():
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.plot(dates, ore_price, "-", label="Fe 62% Spot Price", color="r")
    ax1.legend(loc=0)
    ax1.set_xlabel("Date - 1 Year Period")
    ax1.set_ylabel("Iron Orer Spot Price")

    ax2= ax1.twinx()
    ax2.plot(dates, kio_close, "-", label="KIO Share Price")
    ax2.set_ylabel("KIO Share Price")

    plt.show()

def RSI():

    delta = df["Close"].diff()
    difference = delta.diff()

    #select "i" every time in selected range when "i" is greater/less than zero.
    up = [i for i in difference if i > 0]
    up1 = np.array([up])
    #Changing from an array to a 1-dimensional list/array in order for pd.series to work
    upwards = np.ravel(up1)

    down = [i for i in difference if i < 0]
    down1 = np.array([down])
    # Changing from an array to a 1-dimensional list/array in order for pd.series to work
    downwards = np.ravel(down1)
    #Making sure that losses are also shown as positive values.
    downwards = downwards * -1

    #using Series in pandas since "Series" is one-dimensaional data compared to DataFrame which is 2 dimeensional.
    average_gain = pd.Series(upwards).ewm(ignore_na=False,span=14, adjust=True).mean()
    average_loss = pd.Series(downwards).ewm(ignore_na=False, span=14, adjust=True).mean()

    RS = average_gain/average_loss

    RSI = 100.0 - (100.0/(1.0 + RS))

    plt.gca().xaxis.set_major_formatter(pltdate.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(pltdate.DayLocator())

    plt.grid(True)
    plt.plot(RSI, label="RSI using EMA")
    plt.legend(loc=2)
    plt.show()