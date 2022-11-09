#create a list of cities names taken from user
city_names=input("Enter city names separated by comma(,)=")
print([e for e in city_names.split(',')])