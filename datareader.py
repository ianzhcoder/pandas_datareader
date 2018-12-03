#股票資料讀入

import matplotlib.pyplot as plt
import pandas_datareader.data  as web
import datetime


start_t = datetime.datetime(2018,10,1)
end_t = datetime.datetime(2018,11,30)

#從yahoo抓美股AAPL 10.11月資料
df = web.DataReader("AAPL","yahoo",start_t,end_t)

#最後7筆資料的開始、結束、平均
print (df [["Open","Close","Volume"]].tail(7))

#印出圖形
plt.show(df [["Open","Close"]].tail(7).plot())

plt.show(df [["Volume"]].tail(7).plot())
