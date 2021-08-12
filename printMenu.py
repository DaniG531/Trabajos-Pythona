def printMenu():
    print("0. Mostrar la lista.")
    print("1. Añadir a la lista.")
    print("2. Buscar en la lista")
    print("3. Borrar de la lista.")
    print("4. Modificar la lista.")
    print("5. Limpiar la lista.")
    print("6. Organizar la lista.")
    print("7. Mostrar Tareas Terminadas.")
    print("8. Mostrar Tareas Incompletas.")
    print("9. Terminar Tarea.")
    print("10. Abrir Tarea.")
    print("11. Salir de la aplicación.")
    print("12. Limpiar Menu.")
    print("")
    
def validateMenu(option):
    if int(option) <0 or int(option) > 11:
        return False
    return True