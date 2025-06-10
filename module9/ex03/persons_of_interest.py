#!/usr/bin/env python3

women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

def famous_births():
    sorted_dict = dict(sorted(women_scientists.items(), key=lambda item: item[1]["date_of_birth"]))
    for scientist in sorted_dict.values():
        print(f"{scientist['name']} was born in {scientist['date_of_birth']}.")

famous_births()