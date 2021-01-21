"""
100 days of Python course
DAY 9
"""

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

# write a function that will enable new countries to be added
def add_new_country(country_visited, times_visited, cities_visited ):
    """

    Parameters
    ----------
    country_visited : TYPE
        DESCRIPTION.
    times_visited : TYPE
        DESCRIPTION.
    cities_visited : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
