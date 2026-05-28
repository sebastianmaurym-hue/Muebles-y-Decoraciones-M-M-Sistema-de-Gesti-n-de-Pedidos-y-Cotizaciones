from Catalogo import Catalogo

class Producto:
    def __init__(self, nombre, precio, necesita_tapizado):
        self.__nombre = nombre
        self.__precio = precio
        self.__necesita_tapizado = necesita_tapizado

    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def necesita_tapizado(self):
        return self.__necesita_tapizado


d = Producto("Mesa de comedor", 3490000, False)
e = Producto("Juego de mesas", 2490000, False)
f = Producto("Silla decorativa", 1400000, True)
g = Producto("Banca", 350000, True)
h = Producto("Mueble de tv sencillo", 2100000, False)
i = Producto("Mecedora", 2000000, True)
j = Producto("Mesita de noche", 400000, False)

catalogo1 = Catalogo()

catalogo1.guardar_producto(d)
catalogo1.guardar_producto(e)
catalogo1.guardar_producto(f)
catalogo1.guardar_producto(g)
catalogo1.guardar_producto(h)
catalogo1.guardar_producto(i)
catalogo1.guardar_producto(j)