from colorama import init, Fore, Style
init()
class Catalogo:
    def __init__(self):
        self.__productos = []

    def guardar_producto(self, producto):
        self.__productos.append(producto)

    def mostrar_catalogo(self):
        print(Fore.LIGHTMAGENTA_EX + "====== CATALOGO ======" + Style.RESET_ALL)
        for producto in self.__productos:
            print(f"Producto: {producto.get_nombre()} - Base: COP {producto.get_precio():,}".replace(",", "."))