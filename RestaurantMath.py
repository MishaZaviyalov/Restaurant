import random


def discountPrice(price: float, discount: float):
    price = price - ((price / 100) * discount)
    return price


def plusDiscountPrice(price: float):
    price = price + ((price / 100) * random.randrange(5, 200))
    return price
