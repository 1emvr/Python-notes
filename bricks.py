

def main():
    print_row(4)

def print_row(length):
    print("#" * length)


main()

def main2():
    print_column(4)

def print_column(height):
    for _ in range(height):
        print("#")

main2()
print("", end = "\n")



#############################


def square():
    print_square(3)


def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)


square()





