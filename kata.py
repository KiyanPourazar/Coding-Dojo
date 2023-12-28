import math


def price_calculater(x1, y1, x2, y2):
    distance = math.sqrt((int(x2) - int(x1)) ** 2 + (int(y2) - int(y1)) ** 2)

    price = distance * 10

    print(f"{price} Toman")
