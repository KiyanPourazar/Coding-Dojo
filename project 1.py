from Driver.Driver import Driver as dv
from Driver.Options import Options as op
from User.User import User as user
from trip.trip import trip

# d1_op = op(0,1,0,1)
# d1 = dv("mmd","mmdi","0912","l90","5",d1_op)
drivers = []
for i in range(3):
    first_name ,last_name , phone_number , car_model , plate_number = input("please give us the driver information with this format: (first name, lastname, phone number, car plate)").split()
    driver_options = op(map(int(a) for a in input("give us the driver options as : 0 and 1, music, ac, car license, wheel chair space").split()))
    driver = dv(first_name, last_name, phone_number, car_model, plate_number, driver_options)
    drivers.append(driver)

users = []
for i in range(3):
    first_name, last_name, phone_number, x, y = input("Please give us the users input as this format ( first name, last name, phone number, x, y )").split()
    dist_x, dist_y = input("Please give us the distanation of user").split()
    user_options = op(map(int(a) for a in input("give us the user options as : 0 and 1, music, ac, car license, wheel chair space").split()))
    users.append(user(first_name, last_name, phone_number, x, y, dist_x, dist_y, user_options))
    #calculate user request


trips_list = []



