a = int(input("Altura: "))
b = int(input("Base: "))
i = 0

while i < a:
    if i == 0 or i == a - 1:
        for j in range(b):
            print("*", end=" ")
    else:
        for l in range(1, b):
            if l == 1:
                print("*", end=" ")
            print(" ", end=" ")
            if l == b - 2:
                print("*", end=" ")
    print("")
    i += 1

