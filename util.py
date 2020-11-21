def get_time_range(param):
    start_date, end_date = param.split(" ")
    year_start, month_start, day_start = [int(item) for item in start_date.split("-")]
    year_end, month_end, day_end = [int(item) for item in end_date.split("-")]

    if year_start == year_end:
        return [{"year_start": year_start, "month_start": month_start, "day_start": day_start,
                 "year_end": year_end, "month_end": month_end, "day_end": day_end}]

    time_ranges = []
    time_range = {"year_start": year_start, "month_start": month_start, "day_start": day_start,
                  "year_end": year_start, "month_end": 12, "day_end": 31}
    time_ranges.append(time_range)
    year = year_start + 1
    while year < year_end:
        time_range = {"year_start": year, "month_start": 1, "day_start": 1,
                      "year_end": year, "month_end": 12, "day_end": 31}
        time_ranges.append(time_range)
        year += 1
    time_range = {"year_start": year_end, "month_start": 1, "day_start": 1,
                  "year_end": year_end, "month_end": month_end, "day_end": day_end}
    time_ranges.append(time_range)
    return time_ranges


def load_geocode():
    with open('data/us_city_codes.txt') as f:
        geocodes = f.readlines()
    geocodes = [tuple(geocode.strip().split(',', 1)) for geocode in geocodes]
    return geocodes
