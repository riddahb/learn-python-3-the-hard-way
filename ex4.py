# This is a variable which stores the amount of cars i.e. 100 cars
cars = 100
# This is the amount of space in a car, the number is a float number so it is a decimal number.
space_in_a_car = 4.0
# This is a variable that stores the amount drivers = 30
drivers = 30
# This is a variable that stores the amount of passengers which is 90 
passengers = 90
# this is a variable which stores the calculation of the amount of cars that have not been driven 
cars_not_driven = cars - drivers
# This variable stores the amount of drivers which is 30 inside cars driven variable.
cars_driven = drivers
# The carpool capacity shows the capacity which shows the calculation 
carpool_capacity = cars_driven * space_in_a_car
# This shows the average passenger per car this shows the division .. calculation
average_passenger_per_car = passengers / cars_driven
# This presents these words alongside the variables. for example it will show "There are 100 cars available."
print ("There are", cars, "car's available.")
print ("There are only", drivers, "drivers available")
print ("There will be", cars_not_driven, "empty cars today.")
print ("We can transport", carpool_capacity, "people today.")
print ("We have", passengers, "to carpool today")
print ("We need to put about", average_passenger_per_car, "in each car")