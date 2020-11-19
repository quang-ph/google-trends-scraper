import pandas as pd
from pytrends.request import TrendReq
from datetime import datetime

pytrends = TrendReq()

kw_list = ["climate change", "global warming"]
kw_list = ["global warming"]
TIME_FRAME = "2004-01-01 2020-10-31"
GEO = "US"

pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='US', gprop='')
pytrends.interest_by_region(resolution='CITY', inc_low_vol=True, inc_geo_code=False)

print(f"Start time: {datetime.now()}")
df = pytrends.get_historical_interest(kw_list, year_start=2020, month_start=10, day_start=20, hour_start=0,
                                      year_end=2020,
                                      month_end=10, day_end=31, hour_end=0, gprop='', sleep=10, geo=GEO)
print(f"End time: {datetime.now()}")
print(0)
