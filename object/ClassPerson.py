def ladrar(mood):                                      #Aquí se establece una función que requiere un parametro "Mood".
    print(f"guaf guaf esto es una funcion {mood}")     #Aquí se imprime un string ligado a la función "ladrar" el cual está formateado para poder utilizar el parametro "Mood" dentro de el string que se imprimirá cuando se llame a la función.

  
class Person:              #Aqui se establece la clase "Person".
    name = 'Stalin'        #Aquí se establecen los parametros o "caracteristicas" que tendrán los objetos dentro de la clase, en este caso el default de "name" dentro de la clase "Person" será "Stalin".
    edad = 18              #Aquí se establecen los parametros o "caracteristicas" que tendrán los objetos dentro de la clase, en este caso el default de "edad" dentro de la clase "Person" será "18".
    pertenencias = ["Manzanas","Peras"]    #Aquí se establece un arreglo dentro de la clase "Person" que contiene "Manzanas" y "Peras" dentro.    
    def comunicar(self,mood):              #Dentro de la clase se establece una función "comunicar", que utiliza el "self", refiriendose a el objeto dentro de la clase y el "mood" que es un parametro que se ocupa especificar cuando se llame la función
        print(f"el id desde el metodo de la clase perro:{id(self)}")  #Aquí se imprime un texto que adjunta el {id(self)} donde self se refiere al objeto y id a la id de este, por lo que imprimiría la ID del objeto señalado. la f dentro de lo que se imprime, formatea el string lo que hace posible lo anterior.
        print(f'{self.name}: guaf guaf {mood}')                       #Aquí se imprime un texto, donde {self.name} imprimirá el nombre indicado del objeto, lo que se establece en la linea 6, y despues de el texto el {mood} establecido cuando se mande a llamar la función "Comunicar". la f dentro de lo que se imprime, formatea el string lo que hace posible lo anterior.


elobjeto = Person()            #Aquí se establece que a "elobjeto" como objeto al igualarlo con la clase "Person" lo que lo vuelve un objeto que está dentro de la clase "Person".
elobjeto_2 = Person()          #Aquí se establece que a "elobjeto2" como objeto al igualarlo con la clase "Person" lo que lo vuelve un objeto que está dentro de la clase "Person".
elobjeto.name = "Toby"         #Aquí se establece el modulo .name de "elobjeto" a "Toby", cambiando el default de la clase "Person", que originalmente es "Stalin".
elobjeto_2.name = "Pepe"       ##Aquí se establece el modulo .name de "elobjeto2" a "Pepe", cambiando el default de la clase "Person", que originalmente es "Stalin".

print(elobjeto.name)           #Aquí se manda a imprimir el nombre establecido a "elobjeto" por medio del modulo ".name" el cual se estableció en la linea 16.
print(elobjeto_2.name)         #Aquí se manda a imprimir el nombre establecido a "elobjeto2" por medio del modulo ".name" el cual se estableció en la linea 17.

print(id(elobjeto))            #Aquí se manda a imprimir la id actual del objeto "elobjeto".
elobjeto.comunicar("happy")    #Aquí usando el objeto "elobjeto" se puede mandar a llamar a la función "comunicar" ya que "elobjeto" está dentro de la clase "Person" la cual contiene dicha función. Se dicta el parámetro "happy"  el cual se utilizará como el parámetro "Mood" dentro de la función "comunicar".

print(id(elobjeto_2))          #Aquí se manda a imprimir la id actual del objeto "elobjeto2".
elobjeto_2.comunicar("angry")  #Aquí usando el objeto "elobjeto2" se puede mandar a llamar a la función "comunicar" ya que "elobjeto2" está dentro de la clase "Person" la cual contiene dicha función. Se dicta el parámetro "angry"  el cual se utilizará como el parámetro "Mood" dentro de la función "comunicar".

ladrar("angry")                #Aquí se manda a llamar a la función "Ladrar" establecida en la primera y segunda linea, donde se utiliza el parámetro establecido "angry" como "Mood" dentro de la función.
print(type(elobjeto))          #Aquí se manda a imprimir el tipo de variable que es "elobjeto", lo cual imprimirá que es un objeto dentro de la clase "Person".