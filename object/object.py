class Perro:
    name = 'Toby'
    def ladrar(self,mood):
        print(f"{self.name} waf waf {mood}")


ElObjeto = Perro()
ElObjeto2 = Perro()
ElObjeto.name = "Jimmy"

ElObjeto.ladrar("angry")
ElObjeto2.ladrar("Happy")
print(type(ElObjeto))
print(type(ElObjeto2))