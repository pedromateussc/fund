nights=raw_input("Enter nights:")
city=raw_input("Enter city:")
days=raw_input("Enter days of car rental:")
spending_money=raw_input("Enter money:")

def hotel_cost(nights):
    return 140*nights

def plane_ride_cost(city):
    if city=="Charlotte":
        return 183
    elif city=="Tampa":
        return 220
    elif city=="Pittsburgh":
        return 222
    elif city=="Los Angeles":
        return 475


def rental_car_cost(days):
    cost=days*40
    if days >= 7:
        cost -= 50
    elif days>=3:
        cost-=20
    return cost

def trip_cost(city,days,spending_money):
    print rental_car_cost(days)+hotel_cost(days)+plane_ride_cost(city)+spending_money

trip_cost(city,days,spending_money)
