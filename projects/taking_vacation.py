def hotel_cost(nights):
  return 140 * nights

def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475
  else:
    return "Nope"
  
def rental_car_cost(days):
  rent_cost = 40
  if days >= 7:
    return rent_cost * days - 50
  elif days >= 3:
    return rent_cost * days - 20
  else:
    return rent_cost * days
  
def trip_cost(city,days, spending_money):
  return plane_ride_cost(city) + rental_car_cost(days) + hotel_cost(days - 1) + spending_money

print(trip_cost("Los Angeles", 5, 600))
