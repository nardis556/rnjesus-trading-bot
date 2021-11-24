import ccxt
import config
import schedule
from random import randint
from config import marketPair
from config import quoteAsset
import warnings
warnings.filterwarnings('ignore')

import numpy as np
from datetime import datetime
import time

exchange = ccxt.binance({
    "apiKey": config.BINANCE_API_KEY,
    "secret": config.BINANCE_SECRET_KEY
})

in_position = False

#0 buy 1 sell

def prayRNG():
    global in_position
    rnjesus = randint(0,1)
    print("praying to rnjesus")

    if rnjesus == 0:
        print("rnjesus says buy")
        if not in_position:
            order = exchange.create_market_buy_order(marketPair, quoteAsset)
            print(order)
            in_position = True
        else:
            print("already bought")
    
    if rnjesus == 1:
        print("rnjesus says sell")
        if in_position:
            order = exchange.create_market_sell_order(marketPair, quoteAsset)
            print(order)
            in_position = False
        else:
            print("already sold")

print("all profits must be donated to teh church xd, if lose money blame rnjesus")

schedule.every(69).seconds.do(prayRNG)

while True:
    schedule.run_pending()
    time.sleep(1)

#started with $230 USD
#now @ $215 xd