import os
import time

from pytrends.dailydata import get_daily_data
import click
import util


@click.command()
@click.option('--keyword', required=True, help='Keyword to search on Google Trends')
@click.option('--time-frame', required=True,
              help='Time period to search for (include start date and end date). Format: "YYYY-MM YYYY-MM"')
@click.option('--sleep', required=False, default=2, help='Time to sleep after a request to Google API')
@click.option('--geocode', required=False, help='Geocode')
def scrape(keyword, time_frame, sleep, geocode):
    folder = f'result/{keyword.replace(" ", "_")}_daily'
    if not os.path.exists(folder):
        os.makedirs(folder)

    start_time = time_frame.split(" ")[0]
    stop_time = time_frame.split(" ")[1]
    start_year = int(start_time.split("-")[0])
    start_month = int(start_time.split("-")[1])
    stop_year = int(stop_time.split("-")[0])
    stop_month = int(stop_time.split("-")[1])

    geocodes = util.load_geocode()
    if geocode:
        try:
            state = [i[1] for i in geocodes if i[0] == geocode][0]
            geocodes = [(geocode, state)]
        except:
            print("Geocode is not in list of geocodes")
            pass

    for geocode in geocodes:
        state_code = geocode[0]
        state_name = geocode[1].strip()
        print(f"----- {state_name}")
        file_name = f'{state_name.replace(" ", "_")}_{start_time.replace("-", "")}_{stop_time.replace("-", "")}.csv'

        try:
            df = get_daily_data(word=keyword, start_year=start_year, start_mon=start_month, stop_year=stop_year,
                                stop_mon=stop_month, geo=state_code, wait_time=sleep)
            df.to_csv(
                f'{folder}/{file_name}')
        except Exception as e:
            print("Empty data")
            continue
        time.sleep(sleep)


if __name__ == '__main__':
    scrape()
