print("Star Pattern \n")
for i in range(1,50):
    for j in range(i):
        print("*", end="")
    print('\n')

print("Inverted Star Pattern \n")
for i in range(50, 1, -1):
    for j in range(i, 1, -1):
        print("*", end="")
    print('\n')