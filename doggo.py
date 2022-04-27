
"""

animals = ["lemurs", "fossa", "jellyfish"]

print(animals[0])

    ### print th3 numbered ###



animals = ["lemurs", "fossa", "jellyfish"]

for creature in animals:
    print(creature)

    ### print them all ###

"""

def animals():

    creatures = ["lemurs", "fossa", "jellyfish"]

    selection = str(input("What kind of animals do you like? [ pls use lowercase ]: "))


    if selection in creatures:
        print(f"Great choice! I love {selection}")

    else:
        print(f"What... what kind of choice is that? {selection}... pfff")

    """ 
    
       <3


    """

def list():

    print("A list of canines: ")
    print("", "\n")

    canines = ["wolves", "labradors", "collies"]
    

    for i in range(len(canines)): # get the length (#) of animals in "canines" list
        print(canines[i])


animals()
print("", end = "\n")
list()
print("", end = "\n")


def dictionary():

    print("A list of canines and their species: ")
    print("", end = "\n")

    canines = {
        "Foxes": "Vulpes",
        "GSheperd": "Domestic Dog",  # a dictionary "Keys": "Values"
        "Coyote": "C. Latrans",
    }

    for animal in canines:
        print(animal, canines[animal]) ## print "canines" and index[value]

dictionary()


