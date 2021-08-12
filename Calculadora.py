Operacion = True
while Operacion == True:
    NumeroA = float(input("Ingresa un Número:  "))
    Otra = "Si"
    while Otra == "Si":
        NumeroB = float(input("Ingresa otro Número:  "))
        print("")
        print("¿Qué Quieres hacer?")
        print("")
        print("0. Suma.")
        print("1. Resta.")
        print("2. Multiplicación.")
        print("3. División.")
        print("")
        Accion = int(input(""))
        print("")
         
        if Accion == 0:
            Resultado = NumeroA + NumeroB
            print(NumeroA, "+", NumeroB, "=", Resultado)
            print("")

        if Accion == 1:
            Resultado = NumeroA - NumeroB
            print(NumeroA, "-", NumeroB, "=", Resultado)
            print("")

        if Accion == 2:
            Resultado = NumeroA * NumeroB
            print(NumeroA, "*", NumeroB, "=", Resultado)
            print("")

        if Accion == 3:
            Resultado = NumeroA / NumeroB
            print(NumeroA, "/", NumeroB, "=", Resultado)
            print("")

        OtraOp = input("Hacer alguna Operación más? [Si-No] :")
        if OtraOp == "Si":
            UsarRes = input("¿Utilizar resultado como primer factor? [Si-No] :")
            if UsarRes == "Si":
                NumeroA = Resultado
            if UsarRes == "No":
                Otra = "No"
        if OtraOp == "No":
            Otra = "No"
            Operacion = False

            
    
    
            