class Kettle(object):
    def __init__(myName, make, price):
        myName.make = make
        myName.price = price
        myName.on = False


kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.45
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)
print(f"Models: {kenwood.make} = {kenwood.price}, {hamilton.make} = {hamilton.price}")
