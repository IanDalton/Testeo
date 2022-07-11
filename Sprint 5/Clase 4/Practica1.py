class Pelicula:
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print('Se ha creado la pelicula:',self.titulo)
    def __str__(self):
        return'{} ({})'.format(self.titulo,self.lanzamiento)

class Catalogo:
    def __init__(self, nombre_catalogo, peliculas=[]):
        self.nombre_catalogo = nombre_catalogo
        self.peliculas = peliculas
    def agregar(self, pelicula):
        self.peliculas.append(pelicula)
    
    def mostrar_nombre_caralogo(self):
        print(self.nombre_catalogo)
    
    def mostrar(self):
        for pelicula in self.peliculas:
            print('\t {}'.format(pelicula))

p = Pelicula('El Padrino', 172, 1972)

c = Catalogo('Clasicos', [p])

c.mostrar_nombre_caralogo()
c.mostrar()
p2 = Pelicula('El Padrino: Parte 2', 202, 1974)

c.agregar(p2)
c.mostrar()

