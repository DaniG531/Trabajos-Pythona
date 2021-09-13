def Menu():
    print("~~~~~~~~~~~~~~~~")
    print("1. Nuevo Juego.")
    print("2. Continuar.")
    print("3. Opciones")
    print("4. Salir.")
    MenuMenu()

def NewGame():
    print("Juego Iniciado.")

def Continue():
    print("~~~~~~~~~~~~~~~~")
    print("1. Partida 1.")
    print("2. Partida 2.")
    print("3. Partida 3.")
    print("4. Volver.")
    MenuContinue()

def Settings():
    print("~~~~~~~~~~~~~~~~~")
    print("1. Video Y Audio.")
    print("2. Controles.")
    print("3. Juego.")
    print("4. Créditos.")
    print("5. Volver.")
    MenuSettings()

def VideoAudio():
    print("~~~~~~~~~~~~~~~~~~~~~")
    print("Display = Fullscreen.")
    print("FPS = 60.")
    print("Sound Volume = 100%.")
    print("Music Volume = 80%.")
    print("1. Volver.")
    SettingsVideoAud()

def Controls():
    print("~~~~~~~~~~~~~~~~~~~~")
    print("Mostrar Mouse = OFF.")
    print("Vibración = ON.")
    print("Config. Teclado.")
    print("Config. Mando..")
    print("1. Volver.")
    SettingsControls()

def Game():
    print("~~~~~~~~~~~~~~~~~~~~~~")
    print("Idioma.")
    print("Modo Asistencia = OFF.")
    print("Borrar Datos de Juego.")
    print("1. Volver.")
    SettingsGame()

def Credits():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Juego hecho por DaniDumb.")
    print("1. Volver.")
    SettingsCredits()

def MenuMenu():
    bucle = True
    while bucle:
        print("~~~~~~~~~~~~~~~~~~~~~~~")
        option = int(input("Selecciona una opción: "))
        print("~~~~~~~~~~~~~~~~~~~~~~~")
        if option <= 0 or option > 4:
            print("Opción no valida.")
            MenuMenu()
        if option == 1:
            NewGame()
            bucle = False
        if option == 2:
            Continue()
            bucle = False
        if option == 3:
            Settings()
        if option == 4:
            print("Saliendo del Juego.")
            bucle = False

def MenuContinue():
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    option = int(input("Selecciona una opción: "))
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    if option <= 0 or option > 4:
        print("Opción no valida.")
        MenuContinue()
    if option == 1:
        print("Partina Continuada.")
    if option == 2:
        print("Partina Continuada.")
    if option == 3:
        print("Partina Continuada.")
    if option == 4:
        Menu()

def MenuSettings():
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    option = int(input("Selecciona una opción: "))
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    if option <= 0 or option > 5:
        print("Opción no valida.")
        MenuSettings()
    if option == 1:
        VideoAudio()
    if option == 2:
        Controls()
    if option == 3:
        Game()
    if option == 4:
        Credits()
    if option == 5:
        Menu()

def SettingsVideoAud():
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    option = int(input("Selecciona una opción: "))
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    if option <= 0 or option > 1:
        print("Opción no valida.")
        MenuSettings()
    if option == 1:
        Settings()

def SettingsControls():
    print("~~~~~~~~~~~~~~~~~~~~")
    option = int(input("Selecciona una opción: "))
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    if option <= 0 or option > 1:
        print("Opción no valida.")
        SettingsControls()
    if option == 1:
        Settings()

def SettingsGame():
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    option = int(input("Selecciona una opción: "))
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    if option <= 0 or option > 1:
        print("Opción no valida.")
        SettingsGame()
    if option == 1:
        Settings()

def SettingsCredits():
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    option = int(input("Selecciona una opción: "))
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    if option <= 0 or option > 1:
        print("Opción no valida.")
        SettingsCredits()
    if option == 1:
        Settings()

Menu()