import json

with open('data/cities.txt') as f:
    content = f.read()
countries = json.loads(content)
us_states = countries.get('children')[238]

with open('data/us_city_codes.txt', 'w') as f:
    for us_state in us_states.get('children'):
        print(f'{us_state.get("name")}')
        cities = us_state.get('children')
        if cities is None:
            code = f"US-{us_state.get('id')}, {us_state.get('name')}"
            f.write(f"{code}\n")
            continue
        for city in cities:
            code = f"US-{us_state.get('id')}-{city.get('id')}"
            f.write(f"{code}, {city.get('name')}\n")
