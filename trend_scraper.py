import pandas as pd
from pytrends.request import TrendReq
from datetime import datetime

pytrends = TrendReq()

# kw_list = ["climate change", "global warming"]
kw_list = ["global warming"]
TIME_FRAME = ["2004-01-01 2020-10-31"]

with open('data/us_city_codes.txt') as f:
    geocodes = f.readlines()
geocodes = [tuple(geocode.strip().split(',', 1)) for geocode in geocodes]
df = pd.DataFrame()
for i, geocode in enumerate(geocodes[:2]):
    print(geocode[1].strip())
    print(f"Start time: {datetime.now()}")
    tmp_df = pytrends.get_historical_interest(kw_list, year_start=2020, month_start=10, day_start=20, hour_start=0,
                                              year_end=2020,
                                              month_end=10, day_end=31, hour_end=23, gprop='', sleep=10, geo=geocode[0])
    # tmp_df.to_csv(f'data/{geocode[1].strip()}.csv')
    tmp_df = tmp_df['global warming'].to_frame(name=f'{geocode[1].strip()}')

    if i == 0:
        df = tmp_df.copy()
    else:
        df = df.join(tmp_df)
    print(f"End time: {datetime.now()}")
df.to_csv(f'result/df.csv')
