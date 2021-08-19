class MueblesMadera:
    material = "madera" 
    name = "mueble"
    AlmacenajeInterno = True
    patas = 0

class Objeto1(MueblesMadera):
    name = "escritorio"
    patas = 2

class Objeto2(MueblesMadera):
    material = "madera y metal"
    name = "closet"

class Objeto3(MueblesMadera):
    name = "mesa"
    patas = 4
    AlmacenajeInterno = False

class Objeto4(MueblesMadera):
    material = "madera y tela"
    name = "cama"
    patas = 4
    AlmacenajeInterno = False

class Objeto5(MueblesMadera):
    name = "perchero"
    patas = 2

class Objeto6(MueblesMadera):
    name = "buró"

class Objeto7(Objeto4):
    name = "litera"
    material = "madera, metal y tela"

class Objeto8(MueblesMadera):
    name = "estantería"

class Objeto9(MueblesMadera):
    name = "espejo"
    material = "madera y cristal"
    AlmacenajeInterno = False

class Objeto10(Objeto9):
    name = "espejo de pie"
    patas = 2

class Objeto11(MueblesMadera):
    name = "repiza"
    AlmacenajeInterno = False

class Objeto12(MueblesMadera):
    name = "Cuadro"
    material = "madera, tela y cristal"
    AlmacenajeInterno = False


