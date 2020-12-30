#challenge 2

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(name,visits,cities):
    travel_log.append({"name":name,"visits":visits,"cities":cities})



add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)



