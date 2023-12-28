from Driver.Options import Options
class User:
    first_name: str
    last_name: str
    phone_number: str
    x: int
    y: int
    dist_x: int
    dist_y: int
    options: Options
    requests: int


    def __init__(self, first_name, last_name, phone_number, x, y, dist_x, dist_y):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.x = x
        self.y = y
        self.dist_x = dist_x
        self.dist_y = dist_y
        self.request = 1


    def GetUserTrips(self, trips):
        myTrips = []
        for trip in trips:
            if (trip.user.phone_number == self.phone_number):
                myTrips.append(trip)
        return myTrips

    def request(self):
        time, pm_am = input().split()
        x1, y1 = input().split()
        x2, y2 = input().split()

        user_options = [int(option) for option in input("music, ac, int_license, wheelChair_space: ").split()] # 0 = musuic, 1: ac, 2, int_license, 3: wheelChair_space







