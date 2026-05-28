from Persona import Cliente, Trabajador, Carpintero, Pintor, Tapizador, CoordinadorServicioCliente, Administrador
from Sistema import Sistema_inicio, pedir_dato, error, sistema
from Sistema import Json
from Productos import catalogo1
from colorama import init, Fore, Style
init()

Json.cargar(sistema)

# Datos iniciales para pruebas
if len(sistema._Sistema_inicio__clientes) == 0:


    cliente1 = Cliente("Sebastian Muñoz", "1789000000", "cra 5", "sebas@gmail.com", "302", "Smau", "1234")
    sistema.registrar_clientes(cliente1)


    t1 = Carpintero("Pedro Gomez", "1900000000", 170000, "Pgomez", "1234")
    sistema.registrar_trabajadores(t1)


    t2 = Pintor("Juan Torres", "1800000000", 130000, "Jtorres", "1234")
    sistema.registrar_trabajadores(t2)


    t3 = Tapizador("Sebastian Maury", "1700000000", 140000, "Smaury", "1234")
    sistema.registrar_trabajadores(t3)


    t4 = CoordinadorServicioCliente("Sebastian Martinez", "1600000000", 200000, "Smartinez", "1234")
    sistema.registrar_coordinador(t4)


    t5 = Administrador("Camilo Mercado", "1500000000", 250000, "Cmercado", "1234")
    sistema.registrar_administrador(t5)


    Json.guardar(sistema)


L = ["1", "2", "3", "4", "5"]
O = ["1", "2"]

print("\nBienvenido a Muebles y Decoraciones M&M")

while True:


    print(Fore.GREEN + "\n====== MENU PRINCIPAL ======" + Style.RESET_ALL)
    print("Ingrese el número de la opción que desee.")
    print("1. Registrarse como cliente")
    print("2. Iniciar sesión como cliente")
    print("3. Iniciar sesión como trabajador")
    print("4. Salir")

    opcion = pedir_dato("\n- Opción: ")

    while opcion not in L: 
        opcion = input("La opción ingresada es incorrecta, por favor ingresela nuevamente: ")


    
    #Registro Cliente
    if opcion == "1":
        

        print(Fore.CYAN + "\n====== REGISTRO CLIENTE ======" + Style.RESET_ALL)
        nombre = pedir_dato("Nombre: ")
        id = pedir_dato("ID: ")


        while not id.isdigit() or len(id) < 6 or len(id) > 10:
            print("❌ La cédula debe contener solo números y tener entre 6 y 10 dígitos")
            id = pedir_dato("ID: ")


        domicilio = pedir_dato("Domicilio: ")
        correo = pedir_dato("Correo: ")
        telefono = pedir_dato("Telefono: ")


        while not telefono.isdigit() or len(telefono) < 6:
            print("❌ El teléfono debe contener solo números y tener al menos 6 dígitos")


            telefono = pedir_dato("Telefono: ")


        usuario = pedir_dato("Usuario: ")
        contraseña = pedir_dato("Contraseña: ")


        while not contraseña.isdigit() or len(contraseña) > 6:
            print("❌ La contraseña debe tener hasta 6 dígitos numéricos")


            contraseña = pedir_dato("Contraseña: ")

        confirmar_contraseña = pedir_dato("Confirmar contraseña: ")


        while contraseña != confirmar_contraseña:
            confirmar_contraseña = pedir_dato("\nContraseña incorrecta, por favor ingresela nuevamente: ")


        cliente = Cliente(nombre, id, domicilio, correo, telefono, usuario, contraseña)


        sistema.registrar_clientes(cliente)
        Json.guardar(sistema)


        print("Cliente registrado correctamente.")

        salida = sistema.metodo_cliente(cliente)

        if salida == "salir":
            break




    #Login Cliente
    elif opcion == "2":

        print(Fore.CYAN + "\n====== INICIO DE SESIÓN | CLIENTE ======" + Style.RESET_ALL)

        while True:
        
            usuario = pedir_dato("Usuario: ")
            contraseña = pedir_dato("Contraseña: ")

            cliente = sistema.inicio_sesion(usuario, contraseña)

            if cliente in sistema._Sistema_inicio__clientes:
                print(f"Bienvenido cliente {cliente.get_nombre()}")
                salida = sistema.metodo_cliente(cliente)

                if salida == "salir":
                    salida = "salir"
                    break

                break

            else: 

                print("\nUsuario o contraseña incorrectos")
                print("Ingrese el número de la opción que desea: ")
                print("1. Intentar de nuevo")
                print("2. Volver al menú principal")

                op = pedir_dato("Opción: ")

                while op not in O:
                    op = input("La opción ingresada es incorrecta, por favor ingresela nuevamente: ")

                if op == "2":

                    break

        if salida == "salir":
            break
        



    #Login Trabajador
    elif opcion == "3":

        print(Fore.CYAN + "====== INICIO DE SESIÓN | TRABAJADOR ======" + Style.RESET_ALL)

        while True:

            usuario = pedir_dato("Usuario: ")
            contraseña = pedir_dato("Contraseña: ")

            trabajador = sistema.inicio_sesion(usuario, contraseña)

            if trabajador in sistema._Sistema_inicio__trabajadores:
                print(f"Bienvenido trabajador {trabajador.get_nombre()}")
                salida = sistema.metodo_trabajador(trabajador)

                if salida == "salir":
                    salida = "salir"
                    break

                break
                
            
            elif trabajador in sistema._Sistema_inicio__administradores:
                print(f"Bienvenido administrador {trabajador.get_nombre()}")
                salida = sistema.metodo_administrador(trabajador)

                if salida == "salir":
                    salida = "salir"
                    break

                break
            
            elif trabajador in sistema._Sistema_inicio__coordinadores:
                print(f"Bienvenido coordinador de servicio al cliente {trabajador.get_nombre()}")
                salida = sistema.metodo_coordinador(trabajador)

                if salida == "salir":
                    salida = "salir"
                    break

                break

            else: 

                print("\nUsuario o contraseña incorrectos")
                print("Ingrese el número de la opción que desea:")
                print("1. Intentar de nuevo")
                print("2. Volver al menú principal")

                op = pedir_dato("Opción: ")

                while op not in O:
                    op = input("La opción ingresada es incorrecta, por favor ingresela nuevamente: ")

                if op == "2":
                    break


        if salida == "salir":
            break
        
    

    #Salida
    else:

        break

print("\nGracias por visitarnos")