# google-trends-scraper
Script to scrape Google Trend data at city and hour level

## Usage

```
python trend_scraper.py [OPTIONS]

Options:
  --keyword TEXT     Keyword to search on Google Trends  [required]
  --time-frame TEXT  Time period to search for (include start date and end
                     date). Format: "YYYY-MM-DD YYYY-MM-DD"  [required]

  --sleep INTEGER    Time to sleep after a request to Google API

example: 
    python trend_scraper.py --keyword "global warming" --time-frame "2020-10-20 2020-10-21" --sleep 2
```