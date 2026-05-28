from colorama import init, Fore, Style
init()
class Compra:
    def __init__(self, cliente):
        self.__cliente = cliente
        self.__pedidos = []

    def agregar_pedido(self, pedido):
        self.__pedidos.append(pedido)

    def total_compra(self):
        return sum(p.calcular_total() for p in self.__pedidos)

    def mostrar_compra(self):
        print(Fore.LIGHTRED_EX + "\n====== COMPRA ======" + Style.RESET_ALL)
        print(f"Cliente: {self.__cliente.get_nombre()}")
        print(f"Correo: {self.__cliente.get_correo()}")

        for p in self.__pedidos:
            p.mostrar_pedido()

        print(f"Total Compra: COP {self.total_compra():,}".replace(",", "."))