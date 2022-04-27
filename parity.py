

# Is the number even or odd?

"""

x = int(input("What is 'x' ? "))

if x %2 == 0:
    print("Even")

else:
    print("Odd")




### x / 2, with no remainder left ("zero") is considered even
### x / 2, with some remainder left ("more than zero") considered odd


"""


def main():

    x = int(input("What is 'x' ? "))

    if is_even(x):
        print("Even")
    
    else:
        print("Odd")


"""


def is_even(n):

    if n %2 == 0:
        return True
    
    else:
        return False

"""

### More concisely


def is_even(n):
    return n %2 == 0


main()


### Returning that n %2 == 0 will have the boolean "true" automatically
### It's not necesarry to include "false", as the sequence of main() is:
###
###  "figure out if x is even"
###
###     "Else = Odd"

