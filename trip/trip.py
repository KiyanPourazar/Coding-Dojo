from User.User import User

class trip:
    user: User
    driver: User
    date: int
    price: int

    def __init__(self, user, date, price):
        self.user = user
        self.date = date
        self.price = price
