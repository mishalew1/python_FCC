# we use int(eu_floor) because variables are stored as strings and not integers

eu_floor = input('What floor in Europe? ')
us_floor = int(eu_floor) + 1
print('US floor', us_floor)