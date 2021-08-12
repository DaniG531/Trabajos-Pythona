Examen1 = int(input("Calificación del Exámen: "))
if Examen1 >= 90:
    print("Ocupas realizar hacer otro exámen.")
    Examen2 = int(input("Calificación del segundo Exámen: "))
    if Examen2 >= 90:
        print("Tu grupo asignado es Matematicas 103.")
    else:
        print("Tu grupo asignado es Matematicas 102.")
else:
    print("Ocupas realizar hacer otro exámen.")
    Examen3 = int(input("Calificación del segundo Exámen: "))
    if Examen3 >= 90:
        print("Tu grupo asignado es Matematicas 102.")
    else:
        print("Tu grupo asignado es Matematicas 101.")

