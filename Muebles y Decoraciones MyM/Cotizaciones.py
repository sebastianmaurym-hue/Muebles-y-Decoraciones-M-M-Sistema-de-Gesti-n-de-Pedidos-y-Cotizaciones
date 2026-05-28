from colorama import init, Fore, Style
init()
class Cotizaciones:
    def __init__ (self, cliente, producto, madera, pintura, trabajadores, ID):
        self.__cliente = cliente
        self.__producto = producto
        self.__madera = madera
        self.__pintura = pintura
        self.__trabajadores = []
        self.__ID = ID

        self.__asignar_trabajadores(trabajadores)

    def __asignar_trabajadores(self, lista):
        carpintero = None
        pintor = None
        tapizador = None

        for t in lista:

            if t.get_rol() == "carpintero" and carpintero is None:
                carpintero = t

            elif t.get_rol() == "pintor" and pintor is None:
                pintor = t

            elif (t.get_rol() == "tapizador" and tapizador is None and self.__producto.necesita_tapizado()):
                tapizador = t

        if carpintero:
            self.__trabajadores.append(carpintero)

        if pintor:
            self.__trabajadores.append(pintor)

        if tapizador:
            self.__trabajadores.append(tapizador)
            
    def get_cliente(self):
        return self.__cliente
    
    def get_producto(self):
        return self.__producto
    
    def get_madera(self):
        return self.__madera
    
    def get_pintura(self):
        return self.__pintura
    
    def get_trabajadores(self):
        return self.__trabajadores
    
    def get_ID(self):
        return self.__ID
    
    def calcular_total(self):
        mano_obra = sum(t.get_sueldo() for t in self.__trabajadores)
        return (self.__producto.get_precio() + self.__madera.get_precio() + self.__pintura.get_precio() + mano_obra)
    
    def mostrar_cotizacion(self):
        print(Fore.LIGHTRED_EX + "\n====== COTIZACIÓN ======" + Style.RESET_ALL)
        print(f"Cliente: {self.__cliente.get_nombre()}")
        print(f"Correo: {self.__cliente.get_correo()}")
        print(f"Mueble: {self.__producto.get_nombre()}")
        print(f"Madera: {self.__madera.get_nombre()}")
        print(f"Pintura: {self.__pintura.get_nombre()}")
        print(f"ID Cotización: {self.__ID}")

        print(Fore.LIGHTCYAN_EX + "\n- - - - - - Trabajadores - - - - - -" + Style.RESET_ALL)
        for t in self.__trabajadores:
            print(f"- {t.get_nombre()} | {t.get_rol()}")
        
        print(f"Total: COP {self.calcular_total():,}".replace(",", "."))

class Pedido(Cotizaciones):
    def __init__ (self, cliente, producto, madera, pintura, trabajadores, ID):
        super().__init__ (cliente, producto, madera, pintura, trabajadores, ID)
        self.__estado = "pendiente"  # pendiente, en_proceso, completado
        self.__fecha_pedido = None
        self.__fecha_entrega = None
        self.__descripcion = ""
        self.__ID = ID
    
    def cambiar_estado(self, nuevo_estado):
        estados_validos = ["pendiente", "en proceso", "completado"]
        if nuevo_estado in estados_validos:
            self.__estado = nuevo_estado
            return True
        return False
    
    def get_estado(self):
        return self.__estado
    
    def set_fechas(self, fecha_pedido, fecha_entrega):
        self.__fecha_pedido = fecha_pedido
        self.__fecha_entrega = fecha_entrega
    
    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion
    
    def get_descripcion(self):
        return self.__descripcion
    

    def mostrar_pedido(self):
        print(Fore.LIGHTRED_EX + "\n====== PEDIDO ======" + Style.RESET_ALL)
        print(f"Cliente: {self.get_cliente().get_nombre()}")
        print(f"Mueble: {self.get_producto().get_nombre()}")
        print(f"Madera: {self.get_madera().get_nombre()}")
        print(f"Pintura: {self.get_pintura().get_nombre()}")
        print(f"Estado: {Fore.MAGENTA + self.__estado.upper() + Style.RESET_ALL}")
        print(f"ID Pedido: {self.__ID}")
        
        if self.__fecha_pedido:
            print(f"Fecha de Pedido: {self.__fecha_pedido}")
        if self.__fecha_entrega:
            print(f"Fecha de Entrega: {self.__fecha_entrega}")
        if self.__descripcion:
            print(f"Descripción: {self.__descripcion}")
        
        print(f"Total: COP {self.calcular_total():,}".replace(",", "."))