vehicles = {
            'dream': 'Honda 250T',
            'er5': 'Kawasaki ER5',
            'can-am': 'Bombardier Can-Am 250',
            'virago': 'Yamaha XV250',
            "virago1": "Yamaha XV535",
            'tenere': 'Yamaha XT650',
            'jimny': 'Suzuki Jimny 1.5',
            'fiesta': 'Ford Fiesta Ghia 1.4',
            'roadster': 'Triumph Street Triple',
            "starfighter": "Lockheed F-104",
            "learjet": "Bombardier Learjet 75",
            "toy": "glider",
            }

# Upgrade the Virago

del vehicles["starfighter"]
# del vehicles["f1"]
result = vehicles.pop("f1", "You wish! Sell the Learjet and you might afford a racing car.")
print(result)
plane = vehicles.pop("learjet")
print(plane)

bike = vehicles.pop("tenere", "not present")
print(bike)
print()

# for key in vehicles:
#     print(key, vehicles[key], sep=", ")
for key, value in vehicles.items():
    print(key, value, sep=", ")
