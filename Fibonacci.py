def FindFibonacci(N):
    Fibonacci = []
    A = 0
    B = 1

    for i in range(N):
        C = A + B
        A = B
        B = C
        Fibonacci.append(B)
    return Fibonacci


X = int(input("Cantidad de Números:  "))
print(FindFibonacci(X))