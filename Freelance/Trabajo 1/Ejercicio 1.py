import datetime
import sys

#Clase Persona
class Persona:
    
    def __init__(self, nombre, apellido, dni, fecha_nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento
   
    #Metodo que calcula la edad de una persona a partir de su fecha de nacimiento
    def calcular_edad(self):
        hoy = datetime.date.today()
        return hoy.year - self.fecha_nacimiento.year - ((hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))


#Funcion que valida que la fecha ingresada sea valida
def validar_fecha(fecha):
    #Separo la fecha en dia, mes y anio
    anio = int(fecha[6:10])
    mes = int(fecha[3:5])
    dia = int(fecha[0:2])
    #Verifico que el anio sea valido
    if anio < 1900 or anio > datetime.date.today().year:
        return False
    #Verifico que el mes sea valido
    if mes < 1 or mes > 12:
        return False
    #Verifico que el dia sea valido
    if dia < 1 or dia > 31:
        return False
    #Verifico que el mes no tenga dias menores al dia ingresado
    if (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30:
        return False
    #Verifico si es anio bisiesto o no
    if mes == 2:
        if anio % 4 != 0:
            return False
        elif anio % 100 == 0:
            if anio % 400 != 0:
                return False
        if dia > 29:
            return False
    return True


#Funcion que ordena la lista de personas por edad de menor a mayor
def ordenar_por_edad(lista_personas):
    return sorted(lista_personas, key=lambda persona: persona.calcular_edad())


#Funcion que imprime la lista de personas
def imprimir_lista_personas(lista_personas):
    print("\nLista de personas ordenada por edad:")
    for persona in lista_personas:
        print(persona.nombre, persona.apellido, persona.dni, persona.fecha_nacimiento, persona.calcular_edad())
        

#Funcion que pide los datos de una persona
def ingresar_datos_persona():

    nombre = str(input("\nIngrese el nombre: "))
    
    while (not len(nombre) > 2 or not nombre.isalpha()):
        print("\n (¡ATENCION!) El NOMBRE Ingresado Debe Tener solo letras y ser mas de 2 caracteres")
        nombre = input("\nIngrese el nombre: ")
    
    apellido = input("\nIngrese el apellido: ")
    
    while (not len(apellido) > 2 or not apellido.isalpha()):
        print("\n (¡ATENCION!) El APELLIDO Ingresado Debe Tener solo letras y ser mas de 2 caracteres")
        apellido = input("\nIngrese el apellido: ")
    
    dni = input("\nIngrese el dni: ")
    
    while (len(dni) < 5 and not dni.isdigit()):
        print("\n (¡ATENCION!) El DNI Ingresado Debe Tener solo numeros y ser mas de 4")
        dni = input("\nIngrese el dni: ")

    fecha_nacimiento = input("\nIngrese la fecha de nacimiento (DD/MM/AAAA): ")

    while (len(fecha_nacimiento)>10 or len(fecha_nacimiento)<9):
        print("\n (¡ATENCION!) La FECHA DE NACIMIENTO Ingresado Debe Tener solo 10 caracteres 4 solo numeros")
        print("\n Tener en cuenta que el formato debe ser (DD/MM/AAAA)/(DD MM AA)/(DD-MM-AA)\n\n")
        fecha_nacimiento = input("\nIngrese la fecha de nacimiento (DD/MM/AAAA): ")
    #Verifico que la fecha de nacimiento sea valida
    while not validar_fecha(fecha_nacimiento):
        fecha_nacimiento = input("\nLa fecha de nacimiento ingresada no es valida. Reingrese la fecha (DD/MM/AAAA): ")
    #Separo el string en dia, mes y anio
    anio = int(fecha_nacimiento[6:10])
    mes = int(fecha_nacimiento[3:5])
    dia = int(fecha_nacimiento[0:2])
    #Creo la fecha de nacimiento
    fecha_nacimiento = datetime.date(anio, mes, dia)
    #Retorno los datos de la persona
    return nombre, apellido, dni, fecha_nacimiento


#Funcion main
def main():
    #Defino la lista de personas
    lista_personas = []
    
    try:
        opcion = 0
        
        while opcion != 4:
            #Menu de opciones
            print("\n\nMENU:")
            print("1 - Ingresar datos de persona")
            print("2 - Ordenar personas por edad")
            print("3 - Imprimir listado de personas")
            print("4 - Salir")
            opcion = input("\nEliga una opcion: ")
            while(len(opcion) < 1 or not opcion.isnumeric()):
                print("\n(¡ALERTA!) La OPCION debe tener un caracter y debe ser un numero")
                opcion = input("\nEliga una opcion: ")
            #Ingreso de datos de persona
            if opcion == '1':
                nombre, apellido, dni, fecha_nacimiento = ingresar_datos_persona()
                lista_personas.append(Persona(nombre, apellido, dni, fecha_nacimiento))
            #Ordeno las personas por edad
            elif opcion == '2':
                lista_personas = ordenar_por_edad(lista_personas)
            #Imprimo la lista de personas
            elif opcion == '3':
                imprimir_lista_personas(lista_personas)
            elif opcion == '4':
                break
            else:
                print("\nLa opcion ingresada no es valida. Reintente.")
    except ValueError:
        print("\nSe ingreso un valor incorrecto. El programa finalizara.")
    except:
        print(sys.exc_info()[1])
        print("\nError inesperado. El programa finalizara.")
    finally:
        input("\n\nFin")
main()