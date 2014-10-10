Bitcoin-price-history-graph
===========================

Graphs  which show the historical bitcoin (as well as a real time 15 minute)vs USD price from scrapped data.

Description
============================
The aim of the code is to graphically display Bitcoin price value in terms of US Dollars over a 15 minute live interval as well over a one year time period.

The 15 minute data is got from Bitcoincharts.com .I scrap the table using Beautiful Soup and then plot the graph

The one year time period data is got from quandl.com.The website gives a link to a .CSV file which is downloadable.The data is of the following form:
['Date', 'Open', 'High', 'Low', 'Close', 'Volume (BTC)', 'Volume (Currency)', 'Weighted Price'].
You can choose what kind of graph you want and that is plotted against the date.

Outputs
=========

The output graphs  are uploaded as well-figure_1.png and figure_2.png