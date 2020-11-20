import pandas as pd
from pytrends.request import TrendReq
from datetime import datetime

import util

pytrends = TrendReq(hl='en-US', tz=360, timeout=(10, 25), retries=2,
                    backoff_factor=0.1)

# kw_list = ["climate change", "global warming"]
kw_list = ["global warming"]
TIME_FRAME = "2004-01-01 2020-10-31"
time_ranges = util.get_time_range(TIME_FRAME)

with open('data/us_city_codes.txt') as f:
    geocodes = f.readlines()
geocodes = [tuple(geocode.strip().split(',', 1)) for geocode in geocodes]

df = pd.DataFrame()
for time_range in time_ranges:
    print(time_range)
    for i, geocode in enumerate(geocodes):
        print(f"{datetime.now()} - {geocode[1].strip()}")
        run_time = datetime.now()
        tmp_df = pytrends.get_historical_interest(kw_list, year_start=time_range.get("year_start"),
                                                  month_start=time_range.get("month_start"),
                                                  day_start=time_range.get("day_start"),
                                                  hour_start=0,
                                                  year_end=time_range.get("year_end"),
                                                  month_end=time_range.get("month_end"),
                                                  day_end=time_range.get("day_end"),
                                                  hour_end=23, gprop='', sleep=0.5, geo=geocode[0])
        print(f"Request time: {datetime.now() - run_time}")

        if tmp_df.empty:
            with open('log/logs.txt', 'a') as f:
                f.write(f"{datetime.now()} - {kw_list[0]} - {geocode[1]} :no data\n")
            continue
        else:
            tmp_df = tmp_df['global warming'].to_frame(name=f'{geocode[1].strip()}')
            tmp_df.to_csv(f'result/{geocode[0]}-{time_range.get("year_start")}.csv')

        if df.empty:
            df = tmp_df.copy()
        else:
            df = df.join(tmp_df)

    df.to_csv(f'result/global_warming_{time_range.get("year_start")}.csv')
