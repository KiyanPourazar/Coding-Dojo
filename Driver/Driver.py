import Options


class Driver:
    first_name: str
    last_name: str
    phone_number: str
    car_model: str
    plate_number: str
    options: Options
    availiblity: int


    def __init__(self, first_name, last_name, phone_number, car_model, plate_number, options):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.car_model = car_model
        self.plate_number = plate_number
        self.options = options
        self.availiblity = 0

    def GetDriverTrips(self, trips):
        myTrips = []
        for trip in trips:
            if (trip.driver.plate_number == self.plate_number):
                myTrips.append(trip)
        return myTrips


    def calculate_score(self, options: Options):
        score = 1 / self.availiblity
        score += self.options.music & options[0]
        score += self.options.ac & options[1]
        score += self.options.int_license & options[2]
        score += self.options.wheelChair_space & options[3]
        return score