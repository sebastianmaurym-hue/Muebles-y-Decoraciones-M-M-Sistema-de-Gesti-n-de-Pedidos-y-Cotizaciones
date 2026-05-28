class Persona:
    def __init__(self, nombre, ID):
        self.__nombre = nombre
        self.__ID = ID

    def get_nombre(self):
        return self.__nombre

    def get_ID(self):
        return self.__ID
    

class Cliente(Persona):
    def __init__(self, nombre, ID, domicilio, correo, numero_telefonico, usuario, contraseña):
        super().__init__(nombre, ID)
        self.__domicilio = domicilio
        self.__correo = correo
        self.__numero_telefonico = numero_telefonico
        self.__usuario = usuario
        self.__contraseña = contraseña

    def get_correo(self):
        return self.__correo
    
    def get_usuario(self):
        return self.__usuario
    
    def get_domicilio(self):
        return self.__domicilio
    
    def get_numero_telefonico(self):
        return self.__numero_telefonico
    
    def verificar_contraseña(self, contraseña):
        return self.__contraseña == contraseña 


class Trabajador(Persona):
    def __init__ (self, nombre, ID, sueldo, usuario, contraseña):
        super().__init__ (nombre, ID)
        self.__sueldo = sueldo
        self.__usuario = usuario
        self.__contraseña = contraseña
    
    def get_sueldo(self):
        return self.__sueldo

    def set_sueldo(self, nuevo_sueldo):
        self.__sueldo = nuevo_sueldo
    
    def get_usuario(self):
        return self.__usuario
    
    def verificar_contraseña(self, contraseña):
        return self.__contraseña == contraseña 

class Carpintero(Trabajador):
   def __init__ (self, nombre, ID, sueldo, usuario, contraseña):
       super().__init__ (nombre, ID, sueldo, usuario, contraseña)

   def get_rol(self):
       return "carpintero"


class Pintor(Trabajador):
   def __init__ (self, nombre, ID, sueldo, usuario, contraseña):
       super().__init__ (nombre, ID, sueldo, usuario, contraseña)

   def get_rol(self):
       return "pintor"
   
class Tapizador(Trabajador):
   def __init__ (self, nombre, ID, sueldo, usuario, contraseña):
       super().__init__ (nombre, ID, sueldo, usuario, contraseña)

   def get_rol(self):
       return "tapizador"

class CoordinadorServicioCliente(Trabajador):
   def __init__ (self, nombre, ID, sueldo, usuario, contraseña):
       super().__init__ (nombre, ID, sueldo, usuario, contraseña)

   def get_rol(self):
       return "coordinador de servicio al cliente"

class Administrador(Trabajador):
   def __init__ (self, nombre, ID, sueldo, usuario, contraseña):
       super().__init__ (nombre, ID, sueldo, usuario, contraseña)

   def get_rol(self):
       return "administrador"