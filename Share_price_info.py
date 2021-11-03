#Share info analysis

import os
import pandas as pd
import numpy as np
import matplotlib
from bs4 import BeautifulSoup as soup     #This parses the html text
import requests
import xlrd

#Get the current working directory
os.getcwd()
os.path.isfile("KIO.csv")

#Read the csv file
df = pd.read_excel("KIO.xlsx")

#Specify how many rows to print from the top
#print df.head(5)

#How many rows and how many columns in the dataset
#print df.shape

#Only selecting the "Close" column from the dataframe and then print first 5 rows
closing = df["Close"]
print closing[[0,1,2,3,4]]

#Average closing price for full year
#average_close = closing.mean()
#print average_close

#Need to have a user-agent in order to allow the yahoo server to realise I am using a browser and fool it into allowing
#me access to all the html info. There are user agent strings for all browsers. The info sent to the server is within
#the header of the User Agent and that is why it is needed in order for the server to know what info to relay back to
#my computer.
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
#ping the website
r = requests.get("https://finance.yahoo.com/quote/KIO.JO?p=KIO.JO", headers=headers)

#This will print all the html on the webpage
#kio_html = kio_site.read()

#now you want to parse the html file
page_soup = soup(r.text, "html.parser")
# print page_soup.h1
# print page_soup.ul

#print the html webpage to be properly nested:
#print page_soup.prettify()

#Specifically find certain elements
kio_price = page_soup.find("span", {"class": "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"}).text

#Better to not use variables otherwise the AttributeError shows up within the variable. But when you use the error handling
#it will ignore the error if necessary.

def share_movement():
    try:
        return page_soup.find("span", {"class": "Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($dataGreen)"}).text
    except:
        return page_soup.find("span", {"class": "Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($dataRed)"}).text





#this parses the sheet in question
excel_file = "STD.xls"
df1 = pd.read_excel(excel_file, na_values=["NA"])

print df1.head()