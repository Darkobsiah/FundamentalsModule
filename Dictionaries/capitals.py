countries = [name for name in input().split(', ')]
capitals = [city for city in input().split(', ')]

countries_info_dict = dict(zip(countries, capitals))

for key, value in countries_info_dict.items():
    print(f'{key} -> {value}')