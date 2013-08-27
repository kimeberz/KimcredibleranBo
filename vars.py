# heres a var with cars

cars = 100
seats_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers #heres a var for cars that havent been driven are the cars less drivers
cars_driven = drivers
carpool_capacity = cars_driven * seats_in_a_car #the amount of carpool sots = carsOTR times seatsavail
average_passengers_per_car = passengers / cars_driven

print "there are", cars, "cars available." # there are 100 cars available
print "There are only", drivers, "drivers available" #there are only a set amount of drivers available
print "We can transport", carpool_capacity, "people today." # we can take the carpool capacity on the road today
print "We have", passengers, "to carpool today." # there are a set amount of passengers to carpool today

