class Ubicacion:
    def __init__(self, piso, estante):
        self.piso = piso
        self.estante = estante
        print("Se creo una ubicacion")


class Pelicula:
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print('Se ha creado la pelicula:',self.titulo)

    def __str__(self):
        return'{} ({})'.format(self.titulo,self.lanzamiento)


class Catalogo:
    def __init__(self, nombre_catalogo, piso, estante, peliculas=[]):
        self.nombre_catalogo = nombre_catalogo
        self.peliculas = peliculas
        self.ubicacion = Ubicacion(piso, estante)

    def agregar(self, pelicula):
        self.peliculas.append(pelicula)

    def mostrar_nombre_caralogo(self):
        print(self.nombre_catalogo)

    def mostrar_ubicacion_del_catalogo(self):
        print("Ubicación:", self.ubicacion.piso, "piso", self.ubicacion.estante, "estante")

    def mostrar(self):
        for pelicula in self.peliculas:
            print('\t {}'.format(pelicula))


p = Pelicula('El Padrino', 172, 1972)
p2 = Pelicula('El Padrino: Parte 2', 202, 1974)

c = Catalogo('Clasicos', "3ro", "2do", [p, p2])

c.mostrar_nombre_caralogo()
c.mostrar_ubicacion_del_catalogo()
c.mostrar()
c.agregar(Pelicula("Shrek", 90, 2001))
c.mostrar_nombre_caralogo()
c.mostrar()


class Ejemplo:
    def __init__(self):
        self.__atributo_privado = "asdas"

    def __metodo_privado(self):
        print("culo")

    def get_atributo_privado(self):
        return self.__atributo_privado

    def set_atributo_privado(self, valor):
        self.__atributo_privado = valor
