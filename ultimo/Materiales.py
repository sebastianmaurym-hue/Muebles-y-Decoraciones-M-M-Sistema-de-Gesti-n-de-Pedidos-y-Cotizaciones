class Material:
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = precio

    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio
    
class Madera(Material):
    pass

class Pintura(Material):
    pass

# Catálogos de materiales
maderas = {
    "roble": Madera("Roble", 500000),
    "pino": Madera("Pino", 300000),
    "cerezo": Madera("Cerezo", 700000),
    "caoba": Madera("Caoba", 900000)
}

pinturas = {
    "blanco": Pintura("Blanco", 100000),
    "negro": Pintura("Negro", 100000),
    "rojo": Pintura("Rojo", 120000),
    "azul": Pintura("Azul", 120000),
    "natural": Pintura("Natural", 80000)
}