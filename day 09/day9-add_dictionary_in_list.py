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

def add_new_country(name, visitcount, city):
    newcountry = {}
    newcountry["country"] = name
    newcountry["visits"] = visitcount
    newcountry["cities"] = city
    travel_log.append(newcountry)
  

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

print(travel_log)



