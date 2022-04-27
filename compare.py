"""

def compare():

    x = int(input("What is 'x' ? "))
    y = int(input("What is 'y' ? "))

    if x < y:
        print("x is less than y")

    if x > y:
        print("x is greater than y")

    if x == y:
        print("x is equal to y")


compare()

###

This enumerates too much. The program will run through all 3 options (or more, if you give it more), even if it's found the answer to the question. It will continue all the way till the end. We can make this more concise, so that when it's found a "correct" option, it automatically stops checking through the rest...

Imagine if you had 30 of these if statements and the program had to run through all 30 before giving you a response, even if only 1 answer is true.

"""

def compare():

    x = int(input("What is 'x' ? "))
    y = int(input("What is 'y' ? "))

    if x < y:
        print(f"{x} is less than {y}")

    elif x > y:
        print(f"{x} is greater than {y}")

    elif x == y:
        print(f"{x} is equal to {y}")


compare()

### Rem3mbr, you can append "or" statements to be more concise, if the situation permits

