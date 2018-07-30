import urllib2
import json

url_litecoin = "https://api.binance.com/api/v1/ticker/price?symbol=LTCBTC"

reponse = urllib2.urlopen(url_litecoin)
data = json.load(reponse)

print data["symbol"] #Affiche le symbol
print data["price"] #Affiche le last price 
