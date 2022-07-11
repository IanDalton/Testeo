class Vehiculo:
    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas = ruedas
        lista.append(self)
    pass


class Coche(Vehiculo):
    def __init__(self, color, ruedas,velocidad,cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada


class Caminoneta(Coche):
    def __init__(self, color="", ruedas=0, velocidad=0, cilindrada=0, carga=0):
        Coche.__init__(self, color, ruedas, velocidad, cilindrada)
        self.carga = carga


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo


class Motocicleta(Bicicleta):
    def __init__(self, color="", ruedas=0, tipo="", velocidad=0, cilindrada=0):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada


def catalogar(lista,ruedas=-1):
    i = 0
    for item in lista:
        if ruedas >= 0 :
            if item.ruedas == ruedas:
                i += 1
        else:
            print(type(item).__name__ + ":")
            for atributo in dir(item):
                if atributo[:2] != "__":
                    print("\t" + atributo + ":",getattr(item,atributo))
    if ruedas >= 0:
        print("Se han encontrado {} vehículos con {} ruedas:".format(i,ruedas))
        for item in lista:
            if item.ruedas == ruedas:
                print("\t"+type(item).__name__)


lista = []
carlos = Caminoneta("Rojo",4,10,2,10)
juan = Motocicleta("Verde",2,"deportiva",100,2)
jose = Motocicleta("Negro",2,"urbana",20,2)
catalogar(lista,2)
