

### While Loop ###
"""

i = 1

while i < 50:
    print("meow")
    i +=  1


### Meow...

"""

### a "for list" ###

"""

for i in [0, 1, 2]:
    print("meow")

"""

### a "for range" ###

"""

for _ in range(50):
    print("meow")

"""

### It's common practice to use an underscore (_) for throw-away variables

### Now, ask the user

"""

while True: ### Forever True
    n = int(input("How many times u want me to meow? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")

"""

### "While True: if n > 0" then the infinite loop will be broken and continue to the 
### next line. If it remains at 0 or less then the loop will continue until it's not.

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("How many times u want me to meow? "))
        if n > 0:
            return n


def meow(n):
    for _ in range(n):
        print("meow")

main()