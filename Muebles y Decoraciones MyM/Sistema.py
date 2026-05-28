from Persona import Administrador, CoordinadorServicioCliente, Persona, Cliente, Trabajador, Carpintero, Pintor, Tapizador
from Productos import catalogo1, Producto
from Cotizaciones import Pedido
from Compra import Compra
from Materiales import maderas, pinturas, Madera, Pintura
from Cotizaciones import Cotizaciones
from datetime import datetime
from colorama import init, Fore, Style
import json 
import os
init()

class Json:

    ARCHIVO = "datos.json"

    staticmethod
    def guardar(sistema):

        datos = {

            "clientes": [],
            "trabajadores": [],
            "administradores": [],
            "coordinadores": [],
            "productos": [],
            "pedidos": [],
            "contador_pedidos": sistema._Sistema_inicio__contador_pedidos
        }


        # Clientes
        for c in sistema._Sistema_inicio__clientes:

            datos["clientes"].append({

                "nombre": c.get_nombre(),
                "id": c.get_ID(),
                "domicilio": c.get_domicilio(),
                "correo": c.get_correo(),
                "telefono": c.get_numero_telefonico(),
                "usuario": c.get_usuario(),
                "contraseña": c._Cliente__contraseña
            })


        # Trabajadores
        for t in sistema._Sistema_inicio__trabajadores:

            datos["trabajadores"].append({

                "nombre": t.get_nombre(),
                "id": t.get_ID(),
                "sueldo": t.get_sueldo(),
                "usuario": t.get_usuario(),
                "contraseña": t._Trabajador__contraseña,
                "rol": t.get_rol()
            })


        # Administradores
        for a in sistema._Sistema_inicio__administradores:

            datos["administradores"].append({

                "nombre": a.get_nombre(),
                "id": a.get_ID(),
                "sueldo": a.get_sueldo(),
                "usuario": a.get_usuario(),
                "contraseña": a._Trabajador__contraseña
            })


        # Coordinadores
        for c in sistema._Sistema_inicio__coordinadores:

            datos["coordinadores"].append({

                "nombre": c.get_nombre(),
                "id": c.get_ID(),
                "sueldo": c.get_sueldo(),
                "usuario": c.get_usuario(),
                "contraseña": c._Trabajador__contraseña
            })


        # Productos
        for p in catalogo1._Catalogo__productos:

            datos["productos"].append({


                "nombre": p.get_nombre(),
                "precio": p.get_precio(),
                "tapizado": p.necesita_tapizado()


            })

        # Pedidos
        for p in sistema._Sistema_inicio__pedidos:

            datos["pedidos"].append({

                "cliente": p.get_cliente().get_usuario(),
                "producto": p.get_producto().get_nombre(),
                "madera": p.get_madera().get_nombre().lower(),
                "pintura": p.get_pintura().get_nombre().lower(),

                "estado": p.get_estado(),
                "descripcion": p.get_descripcion(),

                "id": p.get_ID()
            })


        with open(Json.ARCHIVO, "w", encoding = "utf-8") as archivo:

            json.dump(datos, archivo, indent = 4, ensure_ascii = False)


    staticmethod
    def cargar(sistema):

        if not os.path.exists(Json.ARCHIVO):

            return


        with open(Json.ARCHIVO, "r", encoding = "utf-8") as archivo:

            datos = json.load(archivo)


        # Clientes
        for c in datos["clientes"]:

            cliente = Cliente(

                c["nombre"],
                c["id"],
                c["domicilio"],
                c["correo"],
                c["telefono"],
                c["usuario"],
                c["contraseña"]
            )

            sistema.registrar_clientes(cliente)


        # Trabajadores
        for t in datos["trabajadores"]:

            if t["rol"] == "carpintero":

                trabajador = Carpintero(

                    t["nombre"],
                    t["id"],
                    t["sueldo"],
                    t["usuario"],
                    t["contraseña"]
                )


            elif t["rol"] == "pintor":

                trabajador = Pintor(

                    t["nombre"],
                    t["id"],
                    t["sueldo"],
                    t["usuario"],
                    t["contraseña"]
                )


            else:

                trabajador = Tapizador(

                    t["nombre"],
                    t["id"],
                    t["sueldo"],
                    t["usuario"],
                    t["contraseña"]
                )


            sistema.registrar_trabajadores(trabajador)


        # Administradores
        for a in datos["administradores"]:

            admin = Administrador(

                a["nombre"],
                a["id"],
                a["sueldo"],
                a["usuario"],
                a["contraseña"]
            )

            sistema.registrar_administrador(admin)


        # Coordinadores
        for c in datos["coordinadores"]:

            coordinador = CoordinadorServicioCliente(

                c["nombre"],
                c["id"],
                c["sueldo"],
                c["usuario"],
                c["contraseña"]
            )

            sistema.registrar_coordinador(coordinador)


        # Productos
        catalogo1._Catalogo__productos.clear()


        for p in datos["productos"]:

            producto = Producto(


                p["nombre"],
                p["precio"],
                p["tapizado"]


            )

            catalogo1.guardar_producto(producto)


        # Pedidos
        for p in datos["pedidos"]:

            cliente = None


            for c in sistema._Sistema_inicio__clientes:

                if c.get_usuario() == p["cliente"]:

                    cliente = c
                    break


            producto = None


            for prod in catalogo1._Catalogo__productos:

                if prod.get_nombre() == p["producto"]:

                    producto = prod
                    break


            pedido = Pedido(

                cliente,
                producto,
                maderas[p["madera"]],
                pinturas[p["pintura"]],
                sistema._Sistema_inicio__trabajadores,
                p["id"]
            )


            pedido.cambiar_estado(p["estado"])

            pedido.set_descripcion(p["descripcion"])

            sistema._Sistema_inicio__pedidos.append(pedido)


        sistema._Sistema_inicio__contador_pedidos = datos["contador_pedidos"]

class Sistema_inicio:
    def __init__ (self):
        self.__clientes = []
        self.__trabajadores = []
        self.__administradores = []
        self.__coordinadores = []
        self.__pedidos = []
        self.__contador_pedidos = 1

    #Registro
    def registrar_clientes(self, cliente):
        self.__clientes.append(cliente)

    def registrar_trabajadores(self, trabajador):
        self.__trabajadores.append(trabajador)

    def registrar_administrador(self, administrador):
        self.__administradores.append(administrador)

    def registrar_coordinador(self, coordinador):
        self.__coordinadores.append(coordinador)

    #Inicio
    def inicio_sesion(self, usuario, contraseña):
        for c in self.__clientes:
            if c.get_usuario() == usuario and c.verificar_contraseña(contraseña):
                return c
        
        for t in self.__trabajadores:
            if t.get_usuario() == usuario and t.verificar_contraseña(contraseña):
                return t
        
        for a in self.__administradores:
            if a.get_usuario() == usuario and a.verificar_contraseña(contraseña):
                return a
        
        for o in self.__coordinadores:
            if o.get_usuario() == usuario and o.verificar_contraseña(contraseña):
                return o

        return None 
    
    def metodo_cliente(self, cliente):
        O = ["1", "2"]
        L = ["0", "1", "2", "3", "4", "5"]
        maderas_lista = list(maderas.keys())
        pinturas_lista = list(pinturas.keys())
        while True:

            print(Fore.GREEN + "\n====== MENU CLIENTE ======" + Style.RESET_ALL)

            print("Ingrese el número de la opción que desee: ")
            print("0. Ver mi información")
            print("1. Ver catalogo")
            print("2. Realizar un pedido")
            print("3. Ver mis pedidos")
            print("4. Volver al menu principal")
            print("5. Salir")

            
            opcion = pedir_dato("- Opción: ")


            while opcion not in L:

                opcion = error()
            
            if opcion == "0":

                print(Fore.CYAN + "\n====== MIS DATOS ======" + Style.RESET_ALL)
                print(f"Nombre: {cliente.get_nombre()}")
                print(f"ID: {cliente.get_ID()}")
                print(f"Usuario: {cliente.get_usuario()}")
                print(f"Correo: {cliente.get_correo()}")
                print(f"Domicilio: {cliente.get_domicilio()}")
                print(f"Número telefónico: {cliente.get_numero_telefonico()}")


                print(Fore.GREEN + "\n====== MENU ======" + Style.RESET_ALL)
                print("Ingrese el número de la opción que desee: ")
                print("1. Volver")
                print("2. Salir")


                opcion = pedir_dato("- Opción: ")


                while opcion != "1" and opcion != "2":
                    opcion = error()


                if opcion == "1":
                    continue


                else:
                    return "salir"
            
            if opcion == "1":

                catalogo1.mostrar_catalogo()


                print(Fore.GREEN + "\n====== MENU ======" + Style.RESET_ALL)
                print("Ingrese el número de la opción que desee: ")
                print("1. Volver")
                print("2. Salir")

                opcion = pedir_dato("- Opción: ")


                while opcion != "1" and opcion != "2":
                    opcion = error()


                if opcion == "1":
                    continue


                else:
                    return "salir"


            elif opcion == "2":

                print("\n- Realizar Pedido:")
                print("\nMuebles disponibles:")


                catalogo1.mostrar_catalogo()
                

                nombre_producto = pedir_dato("\nIngrese el nombre del mueble: ").lower().strip()
                

                producto = None
                while not producto:
                    for p in catalogo1._Catalogo__productos:

                        if p.get_nombre().lower() == nombre_producto:
                            producto = p
                            break


                    if not producto:
                        print("❌ Mueble no disponible")
                        nombre_producto = error()
                        producto = None

                
                print("\nMaderas disponibles: " + ", ".join(maderas_lista))
                nombre_madera = pedir_dato("Ingrese el tipo de madera: ").lower().strip()

                
                while nombre_madera not in maderas_lista:
                    print("❌ Madera no disponible")

                    nombre_madera = error()

                
                print("\nColores disponibles: " + ", ".join(pinturas_lista))
                nombre_pintura = pedir_dato("Ingrese el color: ").lower().strip()

                
                while nombre_pintura not in pinturas_lista:
                    print("❌ Color no disponible")

                    nombre_pintura = error()
                
                madera = maderas[nombre_madera]
                pintura = pinturas[nombre_pintura]

                compra = Compra(cliente)


                while True:


                    ID = self.__contador_pedidos

                    self.__contador_pedidos += 1

                    pedido = Pedido(cliente, producto, madera, pintura, self.__trabajadores, ID)

                    pedido.set_fechas(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), None)

                    self.__pedidos.append(pedido)

                    Json.guardar(self)

                    compra.agregar_pedido(pedido)

                    cotizacion = Cotizaciones(cliente, producto, madera, pintura, self.__trabajadores, ID)

                    opcion = pedir_dato("\n¿Desea agregar otro pedido? (si/no): ").lower().strip()

                    while opcion != "si" and opcion != "no":
                        opcion = pedir_dato("Ingrese 'si' o 'no': ").lower().strip()


                    if opcion == "si":
                        print("\nAgregue otro mueble al pedido:")
                        catalogo1.mostrar_catalogo()
                        nombre_producto = pedir_dato("\nIngrese el nombre del mueble: ").lower().strip()


                        producto = None


                        while not producto:

                            for p in catalogo1._Catalogo__productos:


                                if p.get_nombre().lower() == nombre_producto:
                                    producto = p

                                    break


                            if not producto:


                                print("❌ Mueble no disponible")
                                nombre_producto = error()
                                producto = None


                        print("\nMaderas disponibles: " + ", ".join(maderas_lista))
                        nombre_madera = pedir_dato("Ingrese el tipo de madera: ").lower().strip()


                        while nombre_madera not in maderas_lista:
                            print("❌ Madera no disponible")
                            nombre_madera = error()


                        print("\nColores disponibles: " + ", ".join(pinturas_lista))
                        nombre_pintura = pedir_dato("Ingrese el color: ").lower().strip()


                        while nombre_pintura not in pinturas_lista:
                            print("❌ Color no disponible")
                            nombre_pintura = error()


                        madera = maderas[nombre_madera]
                        pintura = pinturas[nombre_pintura]

                        continue


                    else:
                        break


                opcion = pedir_dato("\n¿Desea ver el pedido? (si/no): ").lower().strip()

                while opcion != "si" and opcion != "no":
                    opcion = pedir_dato("Ingrese 'si' o 'no': ").lower().strip()

                if opcion == "si":
                    compra.mostrar_compra()


                    print(Fore.GREEN + "\n====== MENU ======" + Style.RESET_ALL)
                    print("Ingrese el número de la opción que desee: ")
                    print("1. Volver")
                    print("2. Salir")

                    opcion = pedir_dato("- Opción: ")


                    while opcion != "1" and opcion != "2":
                        opcion = error()


                    if opcion == "1":
                        continue


                    else:
                        return "salir"


            elif opcion == "3":
                pedidos_cliente = [p for p in self.__pedidos if p.get_cliente() == cliente]


                if pedidos_cliente:
                    print(Fore.CYAN + "\n====== MIS PEDIDOS ======" + Style.RESET_ALL)

                    for p in pedidos_cliente:
                        p.mostrar_pedido()


                else:
                    print("\nNo tienes pedidos registrados aún.")

                    print(Fore.GREEN + "\n====== MENU ======" + Style.RESET_ALL)
                    print("Ingrese el número de la opción que desee: ")
                    print("1. Volver")
                    print("2. Salir")

                    opcion = pedir_dato("- Opción: ")


                    while opcion != "1" and opcion != "2":
                        opcion = error()


                    if opcion == "1":
                        continue


                    else:
                        return "salir"


            elif opcion == "4":
                break


            else:
                return "salir"
            

    def metodo_trabajador(self, trabajador):
        opciones = ["1", "2", "3", "4"]


        while True:

            print(Fore.GREEN + "\n====== MENÚ TRABAJADOR ======" + Style.RESET_ALL)
            print("1. Ver mi información")
            print("2. Ver pedidos asignados")
            print("3. Volver al menú principal")
            print("4. Salir")


            opcion = pedir_dato("- Opción: ")


            while opcion not in opciones:
                opcion = error()


            if opcion == "1":

                print(Fore.CYAN + "\n====== MIS DATOS ======" + Style.RESET_ALL)
                print(f"Nombre: {trabajador.get_nombre()}")
                print(f"ID: {trabajador.get_ID()}")
                print(f"Usuario: {trabajador.get_usuario()}")
                print(f"Sueldo: COP {trabajador.get_sueldo():,}".replace(",", "."))
                print(f"Rol: {trabajador.get_rol()}")


                print(Fore.GREEN + "\n====== MENU ======" + Style.RESET_ALL)
                print("Ingrese el número de la opción que desee: ")
                print("1. Volver")
                print("2. Salir")

                opcion = pedir_dato("- Opción: ")


                while opcion != "1" and opcion != "2":
                    opcion = error()

                if opcion == "1":
                    continue

                else:
                    return "salir"

            elif opcion == "2":
                pedidos_asignados = [p for p in self.__pedidos if trabajador in p.get_trabajadores()]


                if pedidos_asignados:

                    print(Fore.LIGHTMAGENTA_EX + "\n====== PEDIDOS ASIGNADOS ======" + Style.RESET_ALL)


                    for pedido in pedidos_asignados:
                        pedido.mostrar_pedido()


                    print(Fore.GREEN + "\n====== MENU ======" + Style.RESET_ALL)
                    print("Ingrese el número de la opción que desee: ")
                    print("1. Volver")
                    print("2. Salir")


                    opcion = pedir_dato("- Opción: ")


                    while opcion != "1" and opcion != "2":
                        opcion = error()


                    if opcion == "1":
                        continue


                    else:
                        return "salir"
  

                else:
                    print("\nNo tienes pedidos asignados aún.")

                    print(Fore.GREEN + "\n====== MENU ======" + Style.RESET_ALL)
                    print("Ingrese el número de la opción que desee: ")
                    print("1. Volver")
                    print("2. Salir")

                    opcion = pedir_dato("- Opción: ")


                    while opcion != "1" and opcion != "2":
                        opcion = error()

                    if opcion == "1":
                        continue

                    else:
                        return "salir"


            elif opcion == "3":
                break


            else:
                return "salir"     
    def metodo_administrador(self, administrador):

        opciones = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

        while True:

            print(Fore.GREEN + "\n====== MENÚ ADMINISTRADOR ======" + Style.RESET_ALL)
            print("Ingrese el número de la opción que desee: ")
            print("1. Ver mi información")
            print("2. Ver todos los pedidos")
            print("3. Ver todas las cotizaciones")
            print("4. Ver datos de los trabajadores")
            print("5. Cambiar salario de trabajador")
            print("6. Crear nueva cuenta de trabajador")
            print("7. Agregar nueva mercancía al catálogo")
            print("8. Ver datos de los clientes")   
            print("9. Volver al menú principal")
            print("10. Salir")    


            opcion = pedir_dato("- Opción: ")


            while opcion not in opciones:
                opcion = error()
            

            if opcion == "1":


                print(Fore.CYAN + "\n====== MIS DATOS ======" + Style.RESET_ALL)
                print(f"Nombre: {administrador.get_nombre()}")
                print(f"ID: {administrador.get_ID()}")
                print(f"Usuario: {administrador.get_usuario()}")
                print(f"Sueldo: COP {administrador.get_sueldo():,}".replace(",", "."))
                print(f"Rol: {administrador.get_rol()}")


                print(Fore.GREEN + "\n====== MENU ======" + Style.RESET_ALL)
                print("Ingrese el número de la opción que desee: ")
                print("1. Volver")
                print("2. Salir")


                opcion = pedir_dato("- Opción: ")


                while opcion != "1" and opcion != "2":
                    opcion = error()


                if opcion == "1":
                    continue


                else:
                    return "salir"
            
            elif opcion == "2":

                if self.__pedidos:
                    print(Fore.LIGHTMAGENTA_EX + "\n====== TODOS LOS PEDIDOS ======" + Style.RESET_ALL)
                    for pedido in self.__pedidos:
                        pedido.mostrar_pedido()


                else:
                    print("\nNo hay pedidos registrados aún.")

                print(Fore.GREEN + "\n====== MENU ======" + Style.RESET_ALL)
                print("Ingrese el número de la opción que desee: ")
                print("1. Volver")
                print("2. Salir")

                opcion = pedir_dato("- Opción: ")


                while opcion != "1" and opcion != "2":
                    opcion = error()

                if opcion == "1":
                    continue

                else:
                    return "salir"
                
            elif opcion == "3":

                if self.__pedidos:
                    print(Fore.LIGHTMAGENTA_EX + "\n====== TODAS LAS COTIZACIONES ======" + Style.RESET_ALL)
                    for pedido in self.__pedidos:
                        pedido.mostrar_cotizacion()


                else:
                    print("\nNo hay cotizaciones registradas aún.")

                print(Fore.GREEN + "\n====== MENU ======" + Style.RESET_ALL)
                print("Ingrese el número de la opción que desee: ")
                print("1. Volver")
                print("2. Salir")

                opcion = pedir_dato("- Opción: ")


                while opcion != "1" and opcion != "2":
                    opcion = error()

                if opcion == "1":
                    continue

                else:
                    return "salir"
                
            elif opcion == "4":

                if self.__trabajadores:
                    print(Fore.LIGHTMAGENTA_EX + "\n====== DATOS DE LOS TRABAJADORES ======" + Style.RESET_ALL)
                    for trabajador in self.__trabajadores:
                        print(f"Nombre: {trabajador.get_nombre()}")
                        print(f"ID: {trabajador.get_ID()}")
                        print(f"Usuario: {trabajador.get_usuario()}")
                        print(f"Sueldo: COP {trabajador.get_sueldo():,}".replace(",", "."))
                        print(f"Rol: {trabajador.get_rol()}")
                        print("-" * 30)


                else:
                    print("\nNo hay trabajadores registrados aún.")

                print(Fore.GREEN + "\n====== MENU ======" + Style.RESET_ALL)
                print("Ingrese el número de la opción que desee: ")
                print("1. Volver")
                print("2. Salir")

                opcion = pedir_dato("- Opción: ")


                while opcion != "1" and opcion != "2":
                    opcion = error()

                if opcion == "1":
                    continue

                else:
                    return "salir"
                
            elif opcion == "5":
              
              while True:

                if self.__trabajadores:
                    print(Fore.LIGHTMAGENTA_EX + "\n====== CAMBIAR SALARIO DE TRABAJADOR ======" + Style.RESET_ALL)
                    for trabajador in self.__trabajadores:
                        print(f"Nombre: {trabajador.get_nombre()} - ID: {trabajador.get_ID()} - Sueldo actual: COP {trabajador.get_sueldo():,}".replace(",", "."))

                    id_trabajador = pedir_dato("\nIngrese el ID del trabajador cuyo salario desea cambiar: ")
                    trabajador_encontrado = None

                    for trabajador in self.__trabajadores:
                        if trabajador.get_ID() == id_trabajador:
                            trabajador_encontrado = trabajador
                            break

                    if trabajador_encontrado:
                            while True:

                                nuevo_sueldo = pedir_dato("Ingrese el nuevo salario: ")

                                try:

                                    nuevo_sueldo = int(nuevo_sueldo)

                                    if nuevo_sueldo > 0:

                                        trabajador_encontrado.set_sueldo(nuevo_sueldo)

                                        Json.guardar(self)

                                        print(f"Sueldo actualizado correctamente a COP {trabajador_encontrado.get_sueldo():,}".replace(",", "."))

                                        break

                                    else:

                                        print("❌ El sueldo debe ser mayor que 0")

                                except:

                                    print("❌ Ingrese solo números")
                                    break


                    else:

                        print("No se encontró ningún trabajador con ese ID.")

                        
                        print(Fore.GREEN + "\n====== MENU ======" + Style.RESET_ALL)
                        print("Ingrese el número de la opción que desee: ")
                        print("1. Volver a intentar")
                        print("2. Volver al menú")
                        print("3. Salir")


                        opcion = pedir_dato("- Opción: ")

                        while opcion not in ["1", "2", "3"]:
                            opcion = error()


                        if opcion == "1":
                            continue

                        elif opcion == "2":
                            break

                        else:
                            return "salir"
                                

                else:
                    print("\nNo hay trabajadores registrados aún.")

                print(Fore.GREEN + "\n====== MENU ======" + Style.RESET_ALL)
                print("Ingrese el número de la opción que desee: ")
                print("1. Volver")
                print("2. Salir")

                opcion = pedir_dato("- Opción: ")


                while opcion != "1" and opcion != "2":
                    opcion = error()

                if opcion == "1":
                    continue

                else:
                    return "salir"
                
            elif opcion == "6":

                print(Fore.CYAN + "\n====== CREAR NUEVA CUENTA DE TRABAJADOR ======" + Style.RESET_ALL)
                nombre = pedir_dato("Nombre: ")
                id_trabajador = pedir_dato("ID: ")
                sueldo = pedir_dato("Sueldo: ")
                usuario = pedir_dato("Usuario: ")
                contraseña = pedir_dato("Contraseña: ")

                print("Seleccione el rol del trabajador:")
                print("1. Carpintero")
                print("2. Pintor")
                print("3. Tapizador")

                rol_opcion = pedir_dato("- Opción: ")
                while rol_opcion not in ["1", "2", "3"]:
                    rol_opcion = error()

                if sueldo.isdigit() and int(sueldo) > 0:
                    sueldo_int = int(sueldo)
                else:
                    print("Por favor ingrese un sueldo numérico válido.")
                    continue

                if rol_opcion == "1":
                    nuevo_trabajador = Carpintero(nombre, id_trabajador, sueldo_int, usuario, contraseña)
                elif rol_opcion == "2":
                    nuevo_trabajador = Pintor(nombre, id_trabajador, sueldo_int, usuario, contraseña)
                else:
                    nuevo_trabajador = Tapizador(nombre, id_trabajador, sueldo_int, usuario, contraseña)

                self.registrar_trabajadores(nuevo_trabajador)
                Json.guardar(self)
                print(f"Cuenta creada para {nuevo_trabajador.get_rol()} {nuevo_trabajador.get_nombre()} con usuario {nuevo_trabajador.get_usuario()}")

                print(Fore.GREEN + "\n====== MENU ======" + Style.RESET_ALL)
                print("Ingrese el número de la opción que desee: ")
                print("1. Volver")
                print("2. Salir")

                opcion = pedir_dato("- Opción: ")

                while opcion != "1" and opcion != "2":
                    opcion = error()

                if opcion == "1":
                    continue

                else:
                    return "salir"
                
            elif opcion == "7":

                while True:
                    print(Fore.CYAN + "\n====== AGREGAR NUEVA MERCANCÍA ======" + Style.RESET_ALL)
                    print("Seleccione el tipo de elemento que desea agregar:")
                    print("1. Producto")
                    print("2. Madera")
                    print("3. Pintura")
                    print("4. Volver al menú administrador")

                    tipo_agregar = pedir_dato("- Opción: ")
                    while tipo_agregar not in ["1", "2", "3", "4"]:
                        tipo_agregar = error()

                    if tipo_agregar == "4":
                        break

                    if tipo_agregar == "1":
                        nombre_producto = pedir_dato("Nombre del producto: ")
                        precio = pedir_dato("Precio base (solo números): ")

                        if not precio.isdigit() or int(precio) <= 0:
                            print("Por favor ingrese un precio numérico válido.")
                        else:
                            tapizado = pedir_dato("¿El producto necesita tapizado? (si/no): ").lower()
                            while tapizado not in ["si", "no"]:
                                tapizado = error()

                            necesita_tapizado = tapizado == "si"

                            nuevo_prod = Producto(nombre_producto, int(precio), necesita_tapizado)
                            catalogo1.guardar_producto(nuevo_prod)
                            Json.guardar(self)
                            print(f"Producto '{nuevo_prod.get_nombre()}' agregado al catálogo con precio COP {nuevo_prod.get_precio():,}".replace(",", "."))

                    elif tipo_agregar == "2":
                        nombre_madera = pedir_dato("Nombre de la madera: ").lower().strip()

                        if nombre_madera in maderas:
                            print("❌ Esta madera ya existe en el catálogo.")
                        else:
                            precio_madera = pedir_dato("Precio de la madera (solo números): ")
                            if not precio_madera.isdigit() or int(precio_madera) <= 0:
                                print("Por favor ingrese un precio numérico válido.")
                            else:
                                maderas[nombre_madera] = Madera(nombre_madera.title(), int(precio_madera))
                                Json.guardar(self)
                                print(f"Madera '{maderas[nombre_madera].get_nombre()}' agregada al catálogo con precio COP {maderas[nombre_madera].get_precio():,}".replace(",", "."))

                    else:
                        nombre_pintura = pedir_dato("Nombre de la pintura: ").lower().strip()

                        if nombre_pintura in pinturas:
                            print("❌ Esta pintura ya existe en el catálogo.")
                        else:
                            precio_pintura = pedir_dato("Precio de la pintura (solo números): ")
                            if not precio_pintura.isdigit() or int(precio_pintura) <= 0:
                                print("Por favor ingrese un precio numérico válido.")
                            else:
                                pinturas[nombre_pintura] = Pintura(nombre_pintura.title(), int(precio_pintura))
                                Json.guardar(self)
                                print(f"Pintura '{pinturas[nombre_pintura].get_nombre()}' agregada al catálogo con precio COP {pinturas[nombre_pintura].get_precio():,}".replace(",", "."))

                    print(Fore.GREEN + "\n====== MENU ======" + Style.RESET_ALL)
                    print("Ingrese el número de la opción que desee: ")
                    print("1. Volver")
                    print("2. Salir")

                    opcion = pedir_dato("- Opción: ")
                    while opcion != "1" and opcion != "2":
                        opcion = error()

                    if opcion == "2":
                        return "salir"
                    elif opcion == "1":
                        continue

                continue
                
            elif opcion == "8":

                if self.__clientes:
                    print(Fore.LIGHTMAGENTA_EX + "\n====== DATOS DE LOS CLIENTES ======" + Style.RESET_ALL)
                    for cliente in self.__clientes:
                        print(Fore.CYAN + "\n------ CLIENTE ------" + Style.RESET_ALL)
                        print(f"Nombre: {cliente.get_nombre()}")
                        print(f"ID: {cliente.get_ID()}")
                        print(f"Usuario: {cliente.get_usuario()}")
                        print(f"Correo: {cliente.get_correo()}")
                        print(f"Domicilio: {cliente.get_domicilio()}")
                        print(f"Número telefónico: {cliente.get_numero_telefonico()}")


                else:
                    print("\nNo hay clientes registrados aún.")

                print(Fore.GREEN + "\n====== MENU ======" + Style.RESET_ALL)
                print("Ingrese el número de la opción que desee: ")
                print("1. Volver")
                print("2. Salir")

                opcion = pedir_dato("- Opción: ")


                while opcion != "1" and opcion != "2":
                    opcion = error()

                if opcion == "1":
                    continue

                else:
                    return "salir"

            elif opcion == "9":
                break

            elif opcion == "10":
                return "salir"

            else:
                return "salir"
            
    def metodo_coordinador(self, coordinador):

        opciones = ["1", "2", "3", "4", "5"]

        while True:
        
            print(Fore.GREEN + "\n====== MENÚ COORDINADOR DE SERVICIO AL CLIENTE ======" + Style.RESET_ALL)
            print("1. Ver mi información")
            print("2. Ver pedidos")
            print("3. Ver datos de los clientes")
            print("4. Volver al menú principal")
            print("5. Salir")

            opcion = pedir_dato("- Opción: ")

            while opcion not in opciones:
                opcion = error()
            
            if opcion == "1":
                print(Fore.CYAN + "\n====== MIS DATOS ======" + Style.RESET_ALL)
                print(f"Nombre: {coordinador.get_nombre()}")
                print(f"ID: {coordinador.get_ID()}")
                print(f"Usuario: {coordinador.get_usuario()}")
                print(f"Sueldo: COP {coordinador.get_sueldo():,}".replace(",", "."))
                print(f"Rol: {coordinador.get_rol()}")


                print(Fore.GREEN + "\n====== MENU ======" + Style.RESET_ALL)
                print("Ingrese el número de la opción que desee: ")
                print("1. Volver")
                print("2. Salir")

                opcion = pedir_dato("- Opción: ")


                while opcion != "1" and opcion != "2":
                    opcion = error()

                if opcion == "1":
                    continue

                else:
                    return "salir"
            
            elif opcion == "2":

                if self.__pedidos:
                    print(Fore.LIGHTMAGENTA_EX + "\n====== TODOS LOS PEDIDOS ======" + Style.RESET_ALL)
                    for pedido in self.__pedidos:
                        pedido.mostrar_pedido()


                else:
                    print("\nNo hay pedidos registrados aún.")

                print(Fore.GREEN + "\n====== MENU ======" + Style.RESET_ALL)
                print("Ingrese el número de la opción que desee: ")
                print("1. Cambiar el estado de un pedido")
                print("2. Volver")
                print("3. Salir")

                opcion = pedir_dato("- Opción: ")


                while opcion != "1" and opcion != "2" and opcion != "3":
                    opcion = error()

                if opcion == "1":
                    print(Fore.MAGENTA + "\n====== CAMBIAR ESTADO DE PEDIDO ======" + Style.RESET_ALL)
                    id_pedido = pedir_dato("Ingrese el ID del pedido: ").strip()

                    pedido_encontrado = None
                    for pedido in self.__pedidos:
                        if str(pedido.get_ID()) == id_pedido:
                            pedido_encontrado = pedido
                            break

                    if pedido_encontrado:
                        print(f"Estado actual: {pedido_encontrado.get_estado()}")
                        print("Estados disponibles: pendiente, en proceso, completado")
                        nuevo_estado = pedir_dato("Ingrese el nuevo estado: ").lower().strip()

                        while nuevo_estado not in ["pendiente", "en proceso", "completado"]:
                            print("❌ Estado no válido")
                            nuevo_estado = error()

                        pedido_encontrado.cambiar_estado(nuevo_estado)
                        Json.guardar(self)
                        print("✅ Estado actualizado correctamente")

                    else:
                        print("❌ Pedido no encontrado")

                    print(Fore.GREEN + "\n====== MENU ======" + Style.RESET_ALL)
                    print("Ingrese el número de la opción que desee: ")
                    print("1. Volver")
                    print("2. Salir")


                    opcion = pedir_dato("- Opción: ")


                    while opcion != "1" and opcion != "2":
                        opcion = error()

                    if opcion == "1":
                        continue
                    else:
                        return "salir"

                elif opcion == "2":
                    continue

                else:
                    return "salir"
            
            elif opcion == "3":

                if self.__clientes:
                    print(Fore.LIGHTMAGENTA_EX + "\n====== DATOS DE LOS CLIENTES ======" + Style.RESET_ALL)
                    for cliente in self.__clientes:
                        print(Fore.CYAN + "\n------ CLIENTE ------" + Style.RESET_ALL)
                        print(f"Nombre: {cliente.get_nombre()}")
                        print(f"ID: {cliente.get_ID()}")
                        print(f"Usuario: {cliente.get_usuario()}")
                        print(f"Correo: {cliente.get_correo()}")
                        print(f"Domicilio: {cliente.get_domicilio()}")
                        print(f"Número telefónico: {cliente.get_numero_telefonico()}")


                else:
                    print("\nNo hay clientes registrados aún.")

                print(Fore.GREEN + "\n====== MENU ======" + Style.RESET_ALL)
                print("Ingrese el número de la opción que desee: ")
                print("1. Volver")
                print("2. Salir")

                opcion = pedir_dato("- Opción: ")


                while opcion != "1" and opcion != "2":
                    opcion = error()

                if opcion == "1":
                    continue

                else:
                    return "salir"
            
            elif opcion == "4":
                break

            else:
                return "salir"
            

        

def pedir_dato(mensaje):

    while True:
      dato = input(mensaje).strip()

      if dato == "":
          print("❌ Este campo no puede estar vacío")

      else:
            return dato
def error():
      return input("La opción ingresada es incorrecta, por favor ingresela nuevamente: ").lower()


# Instancia global del sistema
sistema = Sistema_inicio()