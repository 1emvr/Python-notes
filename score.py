
"""

score = int(input("Score: "))

if score >= 96 and score <= 100:
    print("A+")

elif score >= 90 and score <= 95:
    print("A")

elif score >= 86 and score <= 89:
    print("B+")

elif score >= 80 and score <= 85:
    print("B")

elif score >= 76 and score <= 79:
    print("C+")

elif score >= 70 and score <= 75:
    print("C")

else:
    print("try harder")
    
    
 """

### more concisely...


score = int(input("Score: "))

if 96 <= score <= 100:
    print("A+")

elif 90 <= score <= 95:
    print("A")

elif 86 <= score <= 89:
    print("B+")

elif 80 <= score <= 85:
    print("B")

elif 76 <= score <= 79:
    print("C+")

elif 70 <= score <= 75:
    print("C")

else:
    print("try harder")
