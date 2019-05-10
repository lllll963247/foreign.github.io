from bs4 import BeautifulSoup
import requests
re = requests.get("https://rate.bot.com.tw/xrt?Lang=zh-TW")  
sp = BeautifulSoup(re.text, 'html.parser')

#print('臺灣銀行')

time = sp.select('.time')

print(time[0].string)

#--------------------------

cash = sp.select('.rate-content-cash')

#日幣
print(cash[17].string)    #現金買入
print(cash[18].string)    #現金賣出	

sight = sp.select('.rate-content-sight')

print(sight[17].string)    #即期買入	
print(sight[18].string)    #即期賣出

