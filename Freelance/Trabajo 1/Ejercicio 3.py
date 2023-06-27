from ast import main

#clase estudiante con constructor, gets y sets, funcion que imprime el estudiante, funcion que calcula el promedi
class Estudiante(object):
    """Clase estudiante"""

    def __init__(self):
        """ Constructor de la clase, se inicializan los atributos
            cedula, nombres, apellidos, asignatura, notas
        """
        self.cedula = None
        self.nombres = None
        self.apellidos = None
        self.asignatura = None
        self.notas = []

    def set_cedula(self, cedula):
        """ setter de cedula, permite modificar el valor del atributo cedula"""
        self.cedula = cedula

    def get_cedula(self):
        """getter de cedula, permite obtener el valor del atributo cedula"""
        return self.cedula

    def set_nombres(self, nombres):
        """ setter de nombres, permite modificar el valor del atributo nombres"""
        self.nombres = nombres

    def get_nombres(self):
        """getter de nombres, permite obtener el valor del atributo nombres"""
        return self.nombres

    def set_apellidos(self, apellidos):
        """ setter de apellidos, permite modificar el valor del atributo apellidos"""
        self.apellidos = apellidos

    def get_apellidos(self):
        """getter de apellidos, permite obtener el valor del atributo apellidos"""
        return self.apellidos

    def set_asignatura(self, asignatura):
        """ setter de asignatura, permite modificar el valor del atributo asignatura"""
        self.asignatura = asignatura

    def get_asignatura(self):
        """getter de asignatura, permite obtener el valor del atributo asignatura"""
        return self.asignatura

    def set_notas(self, notas):
        """ setter de notas, permite modificar el valor del atributo notas"""
        self.notas = notas

    def get_notas(self):
        """getter de notas, permite obtener el valor del atributo notas"""
        return self.notas

    def calcular_promedio(self):
        """ Método, que permite calcular el promedio de las notas de un estudiante
            Nota: el promedio es la suma de todas las notas divido entre la cantidad de notas
        """
        suma = 0
        for nota in self.notas:
            suma = suma + nota

        promedio = float(suma) / float(len(self.notas))

        return promedio

    def imprimir_datos(self):
        """ Método que imprime en pantalla los datos de un estudiante
            incluyendo el promedio
        """
        cadena = "**** Información del estudiante: ****\n"
        cadena = "%sCédula: %s\n" % (cadena, self.cedula)
        cadena = "%sNombres: %s\n" % (cadena, self.nombres)
        cadena = "%sApellidos: %s\n" % (cadena, self.apellidos)
        cadena = "%sAsignatura: %s\n" % (cadena, self.asignatura)
        cadena = "%sPromedio: %s\n" % (cadena, self.calcular_promedio())
        promedio = self.calcular_promedio()
        if(promedio >= 69.5 and promedio <= 100):
            estado = "Aprobado"
        elif(promedio >= 39.50 and promedio < 69.50):
            estado = "Suspenso"
        else:
            estado = "Reprobado"

        cadena = "%sEstado: %s\n" % (cadena, estado)

        print(cadena)

#valida cantidad de notas
def validar_numero(numero):
    """ valida que el valor recibido sea numerico, de lo contrario solicita de nuevo el dato
    """
    if numero.isdigit():
        return int(numero)
    else:
        print("El valor ingresado debe ser numerico")
        return validar_numero(input("Ingrese la nota: "))

#valida que la nota este ente 0 y 100
def validar_rango(numero, rango_min, rango_max):
    """ valida que el valor recibido esté dentro del rango especificado, de lo contrario solicita de nuevo el dato
    """
    if numero >= rango_min and numero <= rango_max:
        return numero
    else:
        print("El valor ingresado debe estar dentro del rango permitido")
        return validar_rango(validar_numero(input("Ingrese la nota: ")), rango_min, rango_max)

#funcion que ingresa la cantidad de notas
def ingresar_notas(cantidad):
    """ Método que permite ingresar las notas del estudiante
    """
    notas = []

    for n in range(0, cantidad):
        nota = validar_rango(validar_numero(input("Ingrese la nota: ")), 0, 100)
        notas.append(nota)

    return notas


#Valida los datos Ingresados(
def validar_cedula(cedula):
    while(len(cedula) < 7 or not cedula.isnumeric()):
        print("(\n\n¡ATENCION!) La CEDULA debe tener mas de 6 caracteres y debe ser solo numeros\n")
        cedula = input("\nIngrese la cedula: ")                
    return cedula

def validar_nombre(nombres):
    while(len(nombres) < 4 or not nombres.isalpha()):
        print("(\n\n¡ATENCION!) El NOMBRE debe tener mas de 3 caracteres y debe ser solo letras\n")
        nombres = input("Ingrese los nombre: ")
    return nombres

def validar_apellido(apellidos):
    while(len(apellidos) < 4 or not apellidos.isalpha()):
        print("\n\n(¡ATENCION!) El APELLIDO debe tener mas de 3 caracteres y debe ser solo letras\n")
        apellidos = input("Ingrese los apellido: ") 
    return apellidos

def validar_asignatura(asignatura):
    while(len(asignatura) < 4 or not asignatura.isalpha()):        
        print("\n\n(¡ATENCION!) La ASIGNATURA debe tener mas de 3 caracteres y debe ser solo letras\n")
        asignatura = input("Ingrese la asignatura: ")
    return asignatura
#)

#funcion Principal
def main():
    estudiante = Estudiante()
    opcion = 0
    while opcion != 3:
        #Menu de opciones
        print("\n\nMENU:")
        print("1 - Ingresar datos de Estudiante")
        print("2 - Editar datos de Estudiante")        
        print("3 - Salir del Programa")
        opcion = input("\nEliga una opcion: ")
        while(len(opcion) < 1 or not opcion.isnumeric()):
                print("\n(¡ALERTA!) La OPCION debe tener un caracter y debe ser un numero")
                opcion = input("\nEliga una opcion: ")
        if(opcion == '1'):
            print("\n**** Ingrese datos de Estudiante ****\n")
            cedula = input("Ingrese la cedula: ")            
            estudiante.set_cedula(validar_cedula(cedula))

            nombres = input("Ingrese los nombre: ")              
            estudiante.set_nombres(validar_nombre(nombres)          )

            apellidos = input("Ingrese los apellido: ")              
            estudiante.set_apellidos(validar_apellido(apellidos)                         )

            asignatura = input("Ingrese la asignatura: ")            
            estudiante.set_asignatura(validar_asignatura(asignatura)            )

            print("\n**** Ingreso de notas: ****\n")
            cantidad = validar_numero(input("Ingrese la cantidad de notas: "))

            estudiante.set_notas(ingresar_notas(cantidad))

            print("\n\n")

            estudiante.imprimir_datos()
        elif(opcion == '2'):
            opcion2 = 0
            if(estudiante.get_nombres() != None):
                while(opcion2 != 6):
                    print("\n**** Editar datos de Estudiante ****\n")            
                    print("Elija los datos que desea Modificar del Estudiante:\n")
                    print("1 - Cedula: ", estudiante.get_cedula())
                    print("2 - Nombre: ", estudiante.get_nombres())
                    print("3 - Apellido:", estudiante.get_apellidos())
                    print("4 - Asignatura:", estudiante.get_asignatura())
                    print("5 - Cantidad de Notas", cantidad)
                    print("6 - Notas:", estudiante.get_notas())
                    print("7 - Regresar al Menu:")
                    opcion2 = input("\nEliga una opcion:")
                    while(len(opcion2) < 1 or not opcion2.isnumeric()):
                        print("\n(¡ALERTA!) La OPCION debe tener un caracter y debe ser un numero")
                        opcion2 = input("\nEliga una opcion: ")

                    if(opcion2 == '1'):
                        cedula = input("Ingrese la cedula: ")                        
                        estudiante.set_cedula(validar_cedula(cedula))
                    elif(opcion2 == '2'):
                        nombres = input("Ingrese los nombre: ")                          
                        estudiante.set_nombres(validar_nombre(nombres))
                    elif(opcion2 == '3'):                    
                        apellidos = input("Ingrese los apellido: ")                          
                        estudiante.set_apellidos(validar_apellido(apellidos))
                    elif(opcion2 == '4'):
                        asignatura = input("Ingrese la asignatura: ")                                    
                        estudiante.set_asignatura(validar_asignatura(asignatura))
                    elif(opcion2 == '5'):
                        cantidad = validar_numero(input("Ingrese la cantidad de notas: "))
                        estudiante.set_notas(ingresar_notas(cantidad))
                    elif(opcion2 == '6'):
                        estudiante.set_notas(ingresar_notas(cantidad))

                    elif(opcion2 == '7'):
                        break

                    else:
                        print("\n(¡Atencion!)La opcion ingresada no se encuentra. Reintente\n\n")   

                    if(opcion2 >= 1 and opcion2 <=6):
                        estudiante.imprimir_datos()

            else:
                print("\n(¡ATENCION!) Debe Ingresar primero un estudiante para poder Editarlo")

        elif(opcion == '3'):
            print("\n\nHa salido Gracias por Usar la App")            
            break

        else: 
            print("\n(¡ATENCION!)La opcion ingresada no se encuentra. Reintente")

main()