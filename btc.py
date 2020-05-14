#Import "requests" Lib
import requests

#Import "BS4" Lib
from bs4 import BeautifulSoup

#Import Colored Lib
from termcolor import colored

#Url Target
url = 'https://arzdigital.com/coins/bitcoin/'

#Mode Transfer Data
r = requests.get(url)

data = r.text

#Creat A Soup 
soup = BeautifulSoup(data,'html.parser')

#Print Title
print (colored('The price of bitcoin virtual change moment by moment','blue'))

#Find Price BTC For Dollar
btcdollar = soup.find('div',attrs={"class":"arz-coin-page-data-coin-price coinPrice btcprice pulser"})

#Print Price BTC For Dollar
print ("Bitcoin price in dollars : ", btcdollar.string)

#Find Price BTC For Toman
btctoman = soup.find('div',attrs={"class":"arz-coin-page-data-coin-toman-price"})

#Pring Price BTC For Toman
print("Bitcoin price in Toman : ", btctoman.text)
