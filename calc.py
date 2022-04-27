"""

x = int(input("what is \"x\" ? "))
y = int(input("what is \"y\" ? "))

print(x + y)

"""

# Floating point values

def main():
    x = float(input("give me a decimal... "))
    y = float(input("give me another decimal... "))
    z = round(x * y, 4) 

        ### v f-string, with :, to add commas... ###
    print(f"{z:,}") 

main()
main()   #<<< used the function 3 times in a row
main()   # It will work 3 times before ending

