import time

from pytrends.request import TrendReq
from datetime import datetime
import click
import util
import os


@click.command()
@click.option('--keyword', required=True, help='Keyword to search on Google Trends')
@click.option('--time-frame', required=True,
              help='Time period to search for (include start date and end date). Format: "YYYY-MM-DD YYYY-MM-DD"')
@click.option('--sleep', required=False, default=2, help='Time to sleep after a request to Google API')
def scrape(keyword, time_frame, sleep):
    print(f"keyword = {keyword}")
    print(f"time-frame = {time_frame}")
    print(f"sleep = {sleep}")

    if not os.path.exists(f'result/{keyword.replace(" ", "_")}'):
        os.makedirs(f'result/{keyword.replace(" ", "_")}')

    pytrends = TrendReq()

    time_ranges = util.get_time_range(time_frame)

    geocodes = util.load_geocode()

    for time_range in time_ranges:
        time_range_str = f'{time_range.get("year_start")}-{time_range.get("month_start")}-{time_range.get("day_start")} ' \
                         f'{time_range.get("year_end")}-{time_range.get("month_end")}-{time_range.get("day_end")}'
        for i, geocode in enumerate(geocodes):
            print(f"{datetime.now()} - {keyword} - {time_range_str} - {geocode[1].strip()}")
            run_time = datetime.now()
            tmp_df = pytrends.get_historical_interest([keyword], year_start=time_range.get("year_start"),
                                                      month_start=time_range.get("month_start"),
                                                      day_start=time_range.get("day_start"),
                                                      hour_start=0,
                                                      year_end=time_range.get("year_end"),
                                                      month_end=time_range.get("month_end"),
                                                      day_end=time_range.get("day_end"),
                                                      hour_end=23, gprop='', sleep=sleep, geo=geocode[0])
            print(f"Request time: {datetime.now() - run_time}")

            if tmp_df.empty:
                with open('log/logs.txt', 'a') as f:
                    f.write(f"{datetime.now()} - {keyword} - {time_range_str} - {geocode[1].strip()} : no data\n")
                continue
            else:
                tmp_df = tmp_df[keyword].to_frame(name=f'{geocode[1].strip()}')
                tmp_df.to_csv(
                    f'result/{keyword.replace(" ", "_")}/{geocode[1].strip().replace(" ", "_")}-{time_range.get("year_start")}.csv')

            time.sleep(sleep)


if __name__ == '__main__':
    scrape()
