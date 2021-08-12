import sys,os
from printMenu import printMenu,validateMenu
print("")

def main(args):
    tareas_terminadas = set()
    tareas_pendientes = set()
    condicion = True
    while condicion:
        
        printMenu()
        opcion = input("Selecciona una opción.")
        if not validateMenu(opcion):
            print("Opción no valida.")

        if int(opcion)==0:
            print(tareas_pendientes)

        if int(opcion)==1:
            tareas_pendientes.add(input("¿Qué quieres añadir?"))

        if int(opcion)==2:
            if input("Introduce lo que quieres buscar?") in tareas_pendientes:
                print("Si se encontro")
            else:
                print("No se encontro")

        if int(opcion)==3:
            elementoparaborrar= input("Introduce lo que quieres borrar.")
            if elementoparaborrar in tareas_pendientes:
                tareas_pendientes.remove(elementoparaborrar)
                print("Se borro")
            else:
                print("No se encontro")

        if int(opcion) == 4:
            elementoparamodificar= input("Introduce lo que quieres Modificar.")
            if elementoparamodificar in tareas_pendientes:
                tareas_pendientes.remove(elementoparamodificar)
                tareas_pendientes.add(input("Introduce nuevo nombre:"))
                print("Se modificó.")
            else:
                print("No se encontro.")

        if int(opcion) == 5:
            tareas_pendientes.clear()

        if int(opcion) == 6:
            tareas_pendientes = list(tareas_pendientes)
            tareas_pendientes.sort()
            print("")
            print(tareas_pendientes)
            print("")
            tareas_pendientes = set(tareas_pendientes)
            
        if int(opcion) == 7:
            print(tareas_terminadas)

        if int(opcion) == 8:
            print(tareas_pendientes)

        if int(opcion) == 9:
            tareaaterminar= input("Introduce la Tarea a terminar.")
            if tareaaterminar in tareas_pendientes:
                tareas_pendientes.remove(tareaaterminar)
                tareas_pendientes.clear()
                tareas_pendientes.remove(tareaaterminar)
                tareas_terminadas.add(tareaaterminar)
                print("Tarea Terminada.")
            else:
                print("No se encontro.")

        if int(opcion) == 10:
            tareaabuscar= input("Introduce la Tarea.")
            if tareaabuscar in tareas_pendientes:
                print(tareaabuscar)

        if int(opcion) == 11:
            condicion = False

        if int(opcion) == 12:
            
        

            os.system('cls' if os.name=="nt" else "clear")


if __name__=='__main__':
    main(sys.argv)
