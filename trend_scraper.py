import pandas as pd
from pytrends.request import TrendReq

pytrends = TrendReq()

kw_list = ["Blockchain"]

pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')
