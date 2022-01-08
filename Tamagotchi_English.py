MatrizDeEmociones = [
#    B C D E F G H I J K
    [1,4,0,5,8,1,6,7,8,9], #Jugar      0                        #B 0 = Neutro
    [0,1,0,3,4,5,1,7,8,9], #Alimentar  1                        #C 1 = Feliz
    [0,0,3,1,5,5,6,7,8,9], #Dormir     2                        #D 2 = Triste
    [1,4,6,6,3,0,3,7,8,9], #Pasear     3                        #E 3 = Cansado
    [2,0,3,3,2,5,2,7,8,9], #Ignorar    4                        #F 4 = Emocionado
    [0,1,3,6,1,0,6,7,0,9], #Bañar      5                        #G 5 = Aburrido
    [0,1,3,3,5,5,6,0,8,9], #Despertar  6                        #H 6 = Hambriento
    [5,0,8,8,1,2,7,9,6,9], #Golpear    7                        #I 7 = Dormido
    [1,4,0,5,4,0,6,7,8,9], #Pisto      8                        #J 8 = Sucio
    [1,1,0,3,1,0,6,7,8,9]  #Acariciar  9                        #K 9 = Muerto
]

def Menu():
    print("Options:")
    print("    - Play")
    print("    - Feed")
    print("    - Sleep")
    print("    - Walk")
    print("    - Ignore")
    print("    - Take a Shower")
    print("    - Wake Up")
    print("    - Hit")
    print("    - Drink Alcohol")
    print("    - Pet")

estado = 0
estadoFinal = 9
listaestados = ["Neutral", "Happy", "Sad", "Tired", "Exited", "Bored", "Hungry", "Asleep", "Dirty", "Dead"]
aristas=["Play", "Feed", "Sleep", "Walk", "Ignore", "Take a Shower", "Wake Up", "Hit", "Drink Alcohol", "Pet"]
while estado != estadoFinal:
    print("")
    print(f"Your Tamagotchi is {listaestados[estado]}.")
    Menu()
    print("What do you want to do?")
    elem = input(" - ")
    print("")
    if elem in aristas:
        key = aristas.index(elem)
        estado = MatrizDeEmociones[key][estado]
    else:
        print("Invalid Option.")


print("Tamagotchi Made By Dani.")
print("UwU")

print(input(""))