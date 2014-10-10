from mechanize import Browser
from bs4 import BeautifulSoup
import urllib2
import re
import matplotlib.pyplot as plt
import numpy as np
import pylab
import csv
from matplotlib.dates import DateFormatter, WeekdayLocator,\
     DayLocator, MONDAY
from matplotlib.finance import quotes_historical_yahoo_ohlc, candlestick_ohlc
from datetime import datetime
import time


#2-15 MIN BITFINEX vs USD TRADE HISTORY-REAL TIME

#Bitcoincharts.com has a table which shows the weighted price in the BITFINEX index vs USD over a current 2-15 minute period
dates=[]
prices=[]
soup = BeautifulSoup(urllib2.urlopen("http://bitcoincharts.com/markets/bitfinexUSD_trades.html").read())    #Scrape the table 
table= soup('table')[4]
for row in table.findAll('tr'):
    lis=row('td')
    if(len(lis)>0):
        date=lis[0]
        cleanr =re.compile('<.*?>')  #Clean out the tags
        cleandate = re.sub(cleanr,'',str(date))
        dates.append(cleandate)

        price=lis[1]
        cleanr_2 =re.compile('<.*?>')
        cleanprice = re.sub(cleanr_2,'',str(price))
        prices.append(cleanprice)

day=dates[0][0:12]

dates=dates[::-1]
prices=prices[::-1]

dates_red=['']*len(dates)
dates_red[0]=dates[0][-8:]  #Dates are in a long format-I reduced it to a HH:SS format(Hours and seconds)"
dates_red[-1]=dates[-1][-8:]


x=[0]*len(dates)
for i in range(0,len(dates)):x[i]=i
y=prices

fig = plt.figure()
title_str='Live 2-15 minute BITFINEX vs USD Trade History-'+day
fig.suptitle(title_str)
plt.xlabel('TimeLine')
plt.ylabel('Price-USD')
plt.xticks(x,dates_red)
plt.grid()
plt.plot(x, y)
plt.show()


#BITFINEX vs USD ONE YEAR TRADING HISTORY

#Quandl.com has a link to a csv file which is downloadable.This file contains the weighted price,opening,high,low and closing prices vs USD over a one year time frame
data=[]
link = urllib2.urlopen("http://www.quandl.com/api/v1/datasets/BCHARTS/BITFINEXUSD.csv?trim_start=2013-03-31&trim_end=2014-10-07")
csv_file= csv.reader(link) #Download and read the CSV file
for row in csv_file:data.append(row)

data_dates=[]
data_wtdprice=[]
data_open=[]
data_high=[]
data_low=[]
data_close=[]

for row in data:
    data_dates.append(row[0])
    data_wtdprice.append(row[-1])
    data_open.append(row[1])
    data_high.append(row[2])
    data_low.append(row[3])
    data_close.append(row[4])
    


data_dates=data_dates[1:]
data_wtdprice=data_wtdprice[1:]
data_open=data_open[1:]
data_high=data_high[1:]
data_low=data_low[1:]
data_close=data_close[1:]

data_dates=data_dates[::-1]
data_wtdprice=data_wtdprice[::-1]
data_open=data_open[::-1]
data_high=data_high[::-1]
data_low=data_low[::-1]
data_close=data_close[::-1]

dates_red=['']*len(data_dates)
dates_red[0]=data_dates[0]
dates_red[-1]=data_dates[-1]
dates_red[len(data_dates)/2]=data_dates[len(data_dates)/2]

#User can select what kind of graph he wants to see

print "What graph do you want to see?....>","\n"
print "Press 1 for weighted price history vs USD","\n"
print "Press 2 for opening price history vs USD","\n"
print "Press 3 for high price history vs USD","\n"
print "Press 4 for low price history vs USD","\n"
print "Press 5 for closing price history vs USD","\n"
graph=raw_input(">>")

if(graph=='1'):
    
 data_wtdprice_float=[0]*len(data_wtdprice)
 for index,price in enumerate(data_wtdprice):data_wtdprice_float[index]=float(price)
 x=[0]*len(data_dates)
 for i in range(0,len(data_dates)):x[i]=i
 y=data_wtdprice_float
 fig = plt.figure()
 title_str='One Year BITFINEX(weighted price) vs USD Trade History'
 fig.suptitle(title_str)
 plt.xlabel('TimeLine',fontsize=15)
 plt.ylabel('Price-USD',fontsize=15)
 plt.xticks(x,dates_red)
 plt.grid()
 plt.plot(x, y,'r')
 plt.show()

if(graph=='2'):
    
 data_open_float=[0]*len(data_open)
 for index,price in enumerate(data_open):data_open_float[index]=float(price)
 x=[0]*len(data_dates)
 for i in range(0,len(data_dates)):x[i]=i
 y=data_open_float
 fig = plt.figure()
 title_str='One Year BITFINEX(Opening price) vs USD Trade History'
 fig.suptitle(title_str)
 plt.xlabel('TimeLine',fontsize=15)
 plt.ylabel('Price-USD',fontsize=15)
 plt.xticks(x,dates_red)
 plt.grid()
 plt.plot(x, y,'r')
 plt.show()
    
if(graph=='3'):
    
 data_high_float=[0]*len(data_high)
 for index,price in enumerate(data_high):data_high_float[index]=float(price)
 x=[0]*len(data_dates)
 for i in range(0,len(data_dates)):x[i]=i
 y=data_high_float
 fig = plt.figure()
 title_str='One Year BITFINEX(High price) vs USD Trade History'
 fig.suptitle(title_str)
 plt.xlabel('TimeLine',fontsize=15)
 plt.ylabel('Price-USD',fontsize=15)
 plt.xticks(x,dates_red)
 plt.grid()
 plt.plot(x, y,'r')
 plt.show()

if(graph=='4'):

 data_low_float=[0]*len(data_low)
 for index,price in enumerate(data_low):data_low_float[index]=float(price)
 x=[0]*len(data_dates)
 for i in range(0,len(data_dates)):x[i]=i
 y=data_low_float
 fig = plt.figure()
 title_str='One Year BITFINEX(Low price) vs USD Trade History'
 fig.suptitle(title_str)
 plt.xlabel('TimeLine',fontsize=15)
 plt.ylabel('Price-USD',fontsize=15)
 plt.xticks(x,dates_red)
 plt.grid()
 plt.plot(x, y,'r')
 plt.show()

if(graph=='5'):
    
 data_close_float=[0]*len(data_close)
 for index,price in enumerate(data_close):data_close_float[index]=float(price)
 x=[0]*len(data_dates)
 for i in range(0,len(data_dates)):x[i]=i
 y=data_close_float
 fig = plt.figure()
 title_str='One Year BITFINEX(Closing price) vs USD Trade History'
 fig.suptitle(title_str)
 plt.xlabel('TimeLine',fontsize=15)
 plt.ylabel('Price-USD',fontsize=15)
 plt.xticks(x,dates_red)
 plt.grid()
 plt.plot(x, y,'r')
 plt.show()
    



    






















