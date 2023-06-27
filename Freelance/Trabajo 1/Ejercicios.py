from datetime import date
from msilib import type_long
from operator import le
from re import L, T
import sys
import datetime
import os
from turtle import pen

#Funciones y Clases del Ejercicio 1 de la linea [10 al 148]( 

#Clase Persona
class Persona1:
    
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

#Funcion principal Ejercicio 1

def ejercicio1():
    #Defino la lista de personas
    lista_personas = []
    
    try:
        opcion = 0
        
        while opcion != 4:
            #Menu de opciones
            print("\n\nMENU PRINCIPAL:")
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
                lista_personas.append(Persona1(nombre, apellido, dni, fecha_nacimiento))
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


#Final de ejercicio 1)

#Funciones y Clases del Ejercicio 1 de la linea [150 al 978]( 

lista_medicos = []
lista_enfermeros = []
lista_pacientes = []

class Persona:
    #Constructor de Persona
    def __init__(self) -> None:
        pass

    def __init__(self, nombre, apellido, fecha_nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento

    
    #Imprimir datos Persona
    def imprimir_datos(self):
        print("-Nombre: ", self.nombre , " -Apellido: " , self.apellido , " -Fecha de Nacimiento: ", self.fecha_nacimiento)
        
    #Funcion que calcula la edad Persona
    def calcula_edad(self):
        hoy = date.today()
        return hoy.year - self.fecha_nacimiento.year - ((hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))

    #Gets de Persona
    def get_nombre(self):
        return self.nombre
    def get_apellido(self):
        return self.apellido
    def get_edad(self):
        return self.edad
    def get_fecha_nacimiento(self):
        return self.fecha_nacimiento
    
    #Sets de Persona
    def set_nombre(self, nombre):
        self.nombre = nombre
    def set_apellido(self, apellido):
        self.apellido = apellido
    def set_edad(self, edad):
        self.edad = edad
    def set_fecha_nacimiento(self, fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento

class Medico(Persona):
    #Constructor de Medico      
    def __init__(self, nombre, apellido, fecha_nacimiento, especialidad, celular, codigo_registro_profesional, sueldo_mensual):
        super().__init__(nombre, apellido, fecha_nacimiento)
        self.especialidad = especialidad
        self.celular = celular
        self.codigo_registro_profesional = codigo_registro_profesional
        self.sueldo_mensual = sueldo_mensual

    #Funcion que calcula el impuesto de Medico
    def calcula_pago_impuestos(self):
        sueldo_anual = self.sueldo_mensual * 12
        if sueldo_anual > 68000:
            impuestos = sueldo_anual * 0.15
        elif sueldo_anual >= 40000 and sueldo_anual <= 68000:
            impuestos = sueldo_anual * 0.085
        else:
            impuestos = sueldo_anual * 0.032
        return sueldo_anual, impuestos
    #Imprime datos Medico
    def mostrar_informacion(self):
        sueldo_anual , impuesto = self.calcula_pago_impuestos()
        super().imprimir_datos()
        print("-Especialidad: ", self.especialidad, " -Celular: ", self.celular, " -Codigo Registro Profesional: ", self.codigo_registro_profesional, " -Sueldo Mensual: ", self.sueldo_mensual, " -Sueldo Anual: ", sueldo_anual, " -Impuesto: ", impuesto)

    #Gets de Medico

    def get_especialidad(self):
        return self.especialidad
    def get_celular(self):
        return self.celular
    def get_codigo_registro_profesional(self):
        return self.codigo_registro_profesional
    def get_sueldo_mensual(self):
        return self.sueldo_mensual

    #Sets de Medico
    def set_especialidad(self, especialidad):
        self.especialidad = especialidad
    def set_celular(self, celular):
        self.celular = celular
    def set_codigo_registro_profesional(self, codigo_registro_profesional):
        self.codigo_registro_profesional = codigo_registro_profesional
    def set_sueldo_mensual(self, sueldo_mensual):
        self.sueldo_mensual = sueldo_mensual

class Enfermero(Persona):
    #Constructor de Enfermero
    def __init__(self, nombre, apellido, fecha_nacimiento, numero_vacunas, experiencia_profesional):
        super().__init__(nombre, apellido, fecha_nacimiento)
        self.numero_vacunas = numero_vacunas
        self.experiencia_profesional = experiencia_profesional
    #Imprimir datos Enfermero
    def mostrar_informacion(self):
        super().imprimir_datos()
        print("-Numero de Vacunas: ", self.numero_vacunas, " -Experiencia Profesional: ",self.experiencia_profesional)

    #Gets de Enfermero
    def get_numero_vacunas(self):
        return self.numero_vacunas
    def get_experiencia_profesional(self):
        return self.experiencia_profesional

    #Sets de Enfermero
    def set_numero_vacunas(self, numero_vacunas):
        self.numero_vacunas = numero_vacunas
    def set_experiencia_profesional(self, experiencia_profesional):
        self.experiencia_profesional = experiencia_profesional

class Paciente(Persona):
    #Constructor de Paciente
    def __init__(self, nombre, apellido, fecha_nacimiento, peso, talla, temperatura, tipo_sangre, motivo_consulta, sintomas):
        super().__init__(nombre, apellido, fecha_nacimiento)
        self.peso = peso
        self.talla = talla
        self.temperatura = temperatura
        self.tipo_sangre = tipo_sangre
        self.motivo_consulta = motivo_consulta
        self.sintomas = sintomas
    
    #Imprimir datos Paciente
    def mostrar_informacion(self):
        super().imprimir_datos()
        print("-Peso: ", self.peso, " -Talla: ",self.talla, " -Temperatura: ", self.temperatura, " -Tipo Sangre: ", self.tipo_sangre, " -Motivo Consulta: ", self.motivo_consulta, " -Sintomas: ", self.sintomas)

    #Gets de Paciente
    def get_peso(self):
        return self.peso
    def get_talla(self):
        return self.talla
    def get_temperatura(self):
        return self.temperatura
    def get_tipo_sangre(self):
        return self.tipo_sangre
    def get_motivo_consulta(self):
        return self.motivo_consulta
    def get_sintomas(self):
        return self.sintomas

    #Sets de Paciente
    def set_peso(self, peso):
        self.peso = peso
    def set_talla(self, talla):
        self.talla = talla
    def set_temperatura(self, temperatura):
        self.temperatura = temperatura
    def set_tipo_sangre(self, tipo_sangre):
        self.tipo_sangre = tipo_sangre
    def set_motivo_consulta(self, motivo_consulta):
        self.motivo_consulta = motivo_consulta
    def set_sintomas(self, sintomas):
        self.sintomas = sintomas

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

#Funciones Para Validar los Datos(

def validar_nombre(nombre):
    while (not len(nombre) > 2 or not nombre.isalpha()):
        print("\n (¡ATENCION!) El NOMBRE Ingresado Debe Tener solo letras y ser mas de 2 caracteres")
        nombre = input("\nIngrese el nombre: ")
    return nombre

def validar_apellido(apellido):
    while (not len(apellido) > 2 or not apellido.isalpha()):
        print("\n (¡ATENCION!) El APELLIDO Ingresado Debe Tener solo letras y ser mas de 2 caracteres")
        apellido = input("\nIngrese el apellido: ")
    return apellido

def validar_fehca1(fecha_nacimiento):
    while (len(fecha_nacimiento)>10 or len(fecha_nacimiento)<9):
        print("\n (¡ATENCION!) La FECHA DE NACIMIENTO Ingresado Debe Tener solo 10 caracteres y ser solo numeros")
        print("\n Tener en cuenta que el formato debe ser (DD/MM/AAAA)/(DD MM AA)/(DD-MM-AA)\n\n")
        fecha_nacimiento = input("\nIngrese la fecha de nacimiento (DD/MM/AAAA): ")
    return fecha_nacimiento

def validar_especialidad(especialidad):
    while(len(especialidad) < 5 or not especialidad.isalpha()):
        print("\n (¡ATENCION!) La ESPECIALIDAD Ingresada Debe Tener mas de 4 caracteres y ser solo letras")
        especialidad = input("\nIngrese Especialidad: ")
    return especialidad

def validar_celular(celular):    
    while(len(celular) < 6 or not celular.isdigit()):
        print("\n (¡ATENCION!) El CELULAR Ingresado Debe Tener mas de 5 caracteres y ser solo Numeros")
        celular = input("\nIngrese Celular: ")
    return celular

def validar_codigo_registro_profesional(codigo_registro_profesional):
    while(len(codigo_registro_profesional) < 5 or not codigo_registro_profesional.isalnum()):
        print("\n (¡ATENCION!) El CODIGO DE REGISTRO PROFESIONA Ingresado Debe Tener mas de 4 caracteres y ser Alfanumerico")
        codigo_registro_profesional = input("\nIngrese Codigo de Registro Profesional: ")
    return codigo_registro_profesional

def validar_sueldo_mensual(sueldo_mensual):
    while(len(sueldo_mensual) < 3 or not sueldo_mensual.isdigit()):
        print("\n (¡ATENCION!) El SUELDO MENSUAL Ingresado Debe Tener mas de 2 caracteres y debe ser solo Numeros")
        sueldo_mensual = input("Ingrese Sueldo Mensual: ")
    return sueldo_mensual

def validar_numero_vacunas(numero_vacunas):
    while(len(numero_vacunas) < 2 or not numero_vacunas.isdigit()):
        print("\n (¡ATENCION!) El NUMERO DE VACUNAS Debe Tener mas de 1 caracteres y debe ser solo Numeros")
        numero_vacunas = int(input("Ingrese Numero de Vacunas: "))
    return numero_vacunas

def validar_experiencia_profecional(experiencia_profecional):
    while(len(experiencia_profecional) < 2 or not experiencia_profecional.isdigit()):
        print("\n (¡ATENCION!) La EXPERIENCIA PROFESIONAL Debe Tener mas de 1 caracteres y debe ser solo Numeros")
        experiencia_profecional = int(input("Ingrese Experiencia profesional en años: "))
    return experiencia_profecional

def validar_peso(peso):
    while(len(peso) < 2 or len(peso) >3 or not peso.isdigit()):
        print("\n (¡ATENCION!) El PESO Debe Tener mas de 1 caracteres y menos de 3 caracteres y debe ser solo Numeros")
        peso = input("Ingrese el Peso: ")
    return peso

def validar_talla(talla):
    while(len(talla)<2 or len(talla) >3 or not talla.isdigit()):
        print("\n (¡ATENCION!) La TALLA Debe Tener mas de 1 caracteres y menos de 3 caracteres y debe ser solo Numeros")
        talla = input("Ingrese la Talla: ")
    return talla

def validar_temperatura(temperatura):
    while(len(temperatura) < 2 or len(temperatura) > 5 or not temperatura.isdigit()):
        print("\n (¡ATENCION!) La TEMPERATURA Debe Tener mas de 1 caracteres y menos de 6 caracteres y debe ser solo Numeros")
        temperatura = input("Ingrese la Temperatura ")
    return temperatura

def validar_tipo_sangre(tipo_sangre):
    while(tipo_sangre != 'A+' and tipo_sangre != 'B+' and tipo_sangre != 'B-' and tipo_sangre != 'O+' and tipo_sangre != 'O-' and tipo_sangre != 'AB+' and tipo_sangre != 'AB-'):
        print("\n (¡ATENCION!) El TIPO DE SANGRE Debe Tener mas de 2 caracteres y menos de 3 caracteres y debe ser solo Letras")
        tipo_sangre = input("Ingrese Tipo de Sangre (A+, O+, A-, O-, B+, B-, AB+, AB-): ")       
    return tipo_sangre

def validar_motivo_consulta(motivo_consulta):
    while(len(motivo_consulta) < 7):
        print("\n (¡ATENCION!) El MOTIVO DE CONSULTA Debe Tener mas de  7 caracteres y debe ser solo Letras")
        motivo_consulta = input("Ingrese Motivo de Consulta: ") 
    return motivo_consulta

def validar_sintomas(sintomas):
    while(len(sintomas) < 3):
        print("\n (¡ATENCION!) Los SINTOMAS Deben Tener mas de  3 caracteres y debe ser solo Letras")
        sintomas = input("Ingrese los Sintomas: ")    
    return sintomas

#Final funciones para validar Datos)

# Funciones del programa
def Ingresar_Datos ():
    op1 = 0
    while(op1 != 4):
        print("\n\n**** Ingresar Datos ****:")
        print("1 - Ingresar Medico")
        print("2 - Ingresar Enfermero")
        print("3 - Ingresar Paciente")
        print("4 - Regresar al Menu")
        #Insertar la Opcion del Menu Ingresar Datos
        op1 = input("\nEliga una opcion: ")
        #Valida la Opcion del Menu Ingresar Datos
        while(not op1.isdigit()):
            print("(¡ATENCION!) ELa opcion seleccionada debe ser un numero entre el 1 y 4")
            op1 = input("\nEliga una opcion: ")
        
        o = int(op1)

        if(o >=1 and o<=3):
            #Ingreso datos persona
            print("\n\n**** Ingresar Datos Persona: ****")
            #Ingreso nombre
            nombre = input("Ingrese Nombre: ")
            #Valido Nombre
            nombre = validar_nombre(nombre)
            #Ingreso Apellido
            apellido = input("Ingrese Apellido: ")
            #Valido Apellido
            apellido = validar_apellido(apellido)
            #Ingreso Fecha
            fecha_nacimiento = input("Ingrese Fecha de Nacimiento: ")
            #Valido Fecha
            fecha_nacimiento = validar_fehca1(fecha_nacimiento)
            #Valida Fecha respecto a la actual y a la mas antigua 1900 ademas valida los dias y meses para que sean correctos
            while not validar_fecha(fecha_nacimiento):
                fecha_nacimiento = input("\nLa fecha de nacimiento ingresada no es valida. Reingrese la fecha (DD/MM/AAAA): ")

        #Valida Que el dato sea un Numero 
        if(op1.isnumeric()):
            #Ingreso datos Medico
            if(op1 == '1'):
                print("\n\n**** Ingresar Datos Medico ****:")                
                #Ingresa Especialidad del Medico
                especialidad = input("Ingrese Especialidad: ")
                #Valida Especialidad del Medico
                especialidad = validar_especialidad(especialidad)
                #Ingresa Celular del Medico
                celular = input("Ingrese Celular: ")
                #Valido el Celular del Medico
                celular = validar_celular(celular)
                #Ingresa Codigo de Registro Profesional
                codigo_registro_profesional = input("Ingrese Codigo de Registro Profesional: ")
                #Valida Codigo de Registro Profesional
                codigo_registro_profesional = validar_codigo_registro_profesional(codigo_registro_profesional)                
                #Ingrese Sueldo Mensual
                sueldo_mensual = input("Ingrese Sueldo Mensual: ")
                #Valida Sueldo Mensual                
                sueldo_mensual = int(validar_sueldo_mensual(sueldo_mensual))
                #Muestra Datos Ingresados
                print("\n\n-------------------------------------------------------------------------------------------------------------------------------------------------------")
                print("**** Datos ingresados correctamente: ****\n")
                medico = Medico(nombre, apellido, fecha_nacimiento, especialidad, celular, codigo_registro_profesional, sueldo_mensual)
                medico.mostrar_informacion()
                #Enlista los datos ingresados de Medicos
                lista_medicos.append(medico)
                print("-------------------------------------------------------------------------------------------------------------------------------------------------------")

            #Ingreso datos Enfermero
            elif(op1 == '2'):
                print("\n\n**** Ingresar Datos Enfermero ****:")
                #Ingresar Numero de vacunas Enfermero                
                numero_vacunas = int(input("Ingrese Numero de Vacunas: "))
                #Validar Numero de vacunas Enfermero
                numero_vacunas = validar_numero_vacunas(numero_vacunas)
                #Ingresa Experiencia profesional en años
                experiencia_profecional = int(input("Ingrese Experiencia profesional en años: "))
                #Valida Experiencia profesional en años
                experiencia_profecional = validar_experiencia_profecional(experiencia_profecional)                

                print("\n\n-------------------------------------------------------------------------------------------------------------------------------------------------------")
                print("**** Datos ingresados correctamente: ****\n")
                #Envia los datos de enfermero al constructor
                enfermero = Enfermero(nombre, apellido, fecha_nacimiento, numero_vacunas, experiencia_profecional)
                #Muestra los Datos Ingresados de Enfermero
                enfermero.mostrar_informacion()
                #Lista los Datos Ingresados de Enfermetr
                lista_enfermeros.append(enfermero)
                print("-------------------------------------------------------------------------------------------------------------------------------------------------------")

            #Ingreso datos Paciente
            elif(op1 == '3'):
                print("\n\n**** Ingresar Datos Paciente ****:")                
                #Ingrese el Peso del Paciente
                peso = input("Ingrese el Peso: ")
                #Valida el Peso del Paciente
                peso = validar_peso(peso)
                #Ingrese la Talla del paciente
                talla = input("Ingrese la Talla: ")
                #Validar la Talla del Paciente
                talla = validar_talla(talla)
                #Ingresa la Temperatura del Paciente
                temperatura = input("Ingrese la Temperatura ")
                #Valida la Temperatura del Paciente
                temperatura = validar_temperatura(temperatura)
                #Ingresa Tipo de Sangre del Paciente
                tipo_sangre = input("Ingrese Tipo de Sangre (A+, 0+, A-, O-, B+, B-, AB+, AB-): ")
                #Valida Tipo de Sangre del Paciente
                tipo_sangre = validar_tipo_sangre(tipo_sangre)                         
                #Ingrese Motivo de Consulta de paciente
                motivo_consulta = input("Ingrese Motivo de Consulta: ")
                #Valida Motivo de Consulta de paciente
                motivo_consulta = validar_motivo_consulta(motivo_consulta)                   
                #Ingrese los Sintomasde paciente
                sintomas = input("Ingrese los Sintomas: ")
                #valida los Sintomas de pasiente
                sintomas = validar_sintomas(sintomas)            
                
                print("\n\n-------------------------------------------------------------------------------------------------------------------------------------------------------")
                print("**** Datos ingresados correctamente: ****\n")
                #Envia los datos de Paciente al constructor
                paciente = Paciente(nombre, apellido, fecha_nacimiento,peso, talla, temperatura, tipo_sangre, motivo_consulta, sintomas)
                #Muestra los Datos Ingresados de Paciente
                paciente.mostrar_informacion()
                #Lista los Datos Ingresados de Paciente
                lista_pacientes.append(paciente)
                print("-------------------------------------------------------------------------------------------------------------------------------------------------------")
            #Salir del while de datos
            elif op1 == '4':
                break
            #valida las opciones del menu datos
            else:
                print("\nLa opcion ingresada no esta en la lista. Reintente.") 
        else:
            print("\nERROR... El valor Ingresado debe ser un Numero... \n\n")
            os.system("pause")

def Editar_Datos():
    op2 = 0
    op3 = 0
    
    while(op2 != 4):
        print("\n\n**** Editar Datos ****:")                    
        print("1 - Editar Medico")
        print("2 - Editar Enfermero")
        print("3 - Editar Paciente")
        print("4 - Regresar al Menu")
        op2 = input("\nEliga una opcion: ")
        if(op2.isnumeric()):
            #Editar datos Medico
            if(op2 == '1'): 

                
                print("\n\n*********************************************************************************************************************************************************")
                print("**** Editar Datos Medico: ****:\n")
                for medico in lista_medicos:
                    medico.mostrar_informacion()
                    print("-----------------------------------------------------------------------------------------------------------------------------------------------------\n")                

                codigo_registro_profesional = input("Ingrese el Codigo de Registro Profesional del Medico a editar: ")
                if(len(lista_medicos) != 0):                    
                    for medico in lista_medicos:                        
                        if medico.get_codigo_registro_profesional() == codigo_registro_profesional:                                          
                            while(op3 != 8):
                                print("\n\n**** Que desea editar de los datos de este Medico ****")
                                print("1 - Nombre: ", medico.get_nombre())
                                print("2 - Apellido: ", medico.get_apellido())
                                print("3 - Fecha de Nacimiento: ", medico.get_fecha_nacimiento())
                                print("4 - Especialidad: ", medico.get_especialidad())
                                print("5 - Celular: ", medico.get_celular())
                                print("6 - Codigo de Registro Profesional: ", medico.get_codigo_registro_profesional())
                                print("7 - Sueldo Mensual: ", medico.get_sueldo_mensual())
                                print("8 - Todos los Datos")
                                print("9 - Regresar a Menu Editar Datos")
                                op3 = input("\nEliga una opcion: ")
                                if(op3.isnumeric()):
                                    if(op3 == '1'):
                                        nombre = input("Ingrese Nombre: ")                                        
                                        medico.set_nombre(validar_nombre(nombre))
                                        
                                    elif(op3 == '2'):
                                        apellido = input("Ingrese Apellido: ")                                        
                                        medico.set_apellido(validar_apellido(apellido))
                                    elif(op3 == '3'):
                                        fecha_nacimiento = input("Ingrese Fecha de Nacimiento: ")                                        
                                        medico.set_fecha_nacimiento(validar_fehca1(fecha_nacimiento))
                                    elif(op3 == '4'):
                                        especialidad = input("Ingrese Especialidad: ")                                        
                                        medico.set_especialidad(validar_especialidad(especialidad))
                                    elif(op3 == '5'):
                                        celular = input("Ingrese Celular: ")
                                        validar_celular(celular)
                                        medico.set_celular(celular)
                                    elif(op3 == '6'):
                                        codigo_registro_profesional = input("Ingrese Codigo de Registro Profesional: ")                                        
                                        medico.set_codigo_registro_profesional(validar_codigo_registro_profesional(codigo_registro_profesional))
                                    elif(op3 == '7'):
                                        sueldo_mensual = input("Ingrese Sueldo Mensual: ")                                        
                                        sueldo_mensual = int(validar_sueldo_mensual(sueldo_mensual))
                                        medico.set_sueldo_mensual(sueldo_mensual)
                                        
                                    elif(op3 == '8'):
                                        nombre = input("Ingrese Nombre: ")                                        
                                        medico.set_nombre(validar_nombre(nombre))

                                        apellido = input("Ingrese Apellido: ")                                        
                                        medico.set_apellido(validar_apellido(apellido))

                                        fecha_nacimiento = input("Ingrese Fecha de Nacimiento: ")                                        
                                        medico.set_fecha_nacimiento(validar_fehca1(fecha_nacimiento))

                                        especialidad = input("Ingrese Especialidad: ")                                        
                                        medico.set_especialidad(validar_especialidad(especialidad))

                                        celular = input("Ingrese Celular: ")                                        
                                        medico.set_celular(validar_celular(celular))

                                        codigo_registro_profesional = input("Ingrese Codigo de Registro Profesional: ")                                        
                                        medico.set_codigo_registro_profesional(validar_codigo_registro_profesional(codigo_registro_profesional))

                                        sueldo_mensual = input("Ingrese Sueldo Mensual: ")                                        
                                        sueldo_mensual = int(validar_sueldo_mensual(sueldo_mensual))
                                        medico.set_sueldo_mensual(sueldo_mensual)

                                    elif(op3 == '9'):
                                        break
                                    else:
                                        print("\nLa opcion ingresada no esta en la lista. Reintente.\n")
                                        os.system("pause")
                                else:
                                    print("\nERROR... El valor Ingresado debe ser un Numero... \n\n")
                                    os.system("pause")
                        else:
                            print("\nNo se encontro el codigo de registro profesional del medico ingresado\n")
                            os.system("pause")
                else:
                    print("\n Debe ingresar primero Datos de Medico \n")
                    os.system("pause")   
            
            #Editar Datos Enfermero
            if(op2 == '2'):
                print("\n\n*********************************************************************************************************************************************************")
                print("**** Editar Datos Enfermero: ****:\n")
                for enfermero in lista_enfermeros:
                    enfermero.mostrar_informacion()
                    print("-----------------------------------------------------------------------------------------------------------------------------------------------------\n")


                nombre = input("Ingrese el Nombre del Enfermero a editar: ")
                if( len(lista_enfermeros) != 0):
                    for enfermero in lista_enfermeros:
                        if enfermero.get_nombre() == nombre:
                            while(op3 != 7):
                                print("\n\n**** Que desea editar de los datos de este Enfermero ****")
                                print("1 - Nombre: ", enfermero.get_nombre())
                                print("2 - Apellido: ", enfermero.get_apellido())
                                print("3 - Fecha de Nacimiento: ", enfermero.get_fecha_nacimiento())
                                print("4 - Numero de Vacunas: ", enfermero.get_numero_vacunas())
                                print("5 - Experiencia Profesional: ", enfermero.get_experiencia_profesional())
                                print("6 - Editar Todos los Datos del Enfermero")
                                print("7 - Regresar al Menu Editar")
                                
                                print("\n")

                                op3 = input("\nEliga una opcion: ")
                                if(op3.isnumeric()):
                                    if(op3 == '1'):
                                        nombre = input("Ingrese Nombre: ")                                        
                                        enfermero.set_nombre(validar_nombre(nombre))                                    
                                    elif(op3 == '2'):
                                        apellido = input("Ingrese Apellido: ")                                        
                                        enfermero.set_apellido(validar_apellido(apellido))                                        
                                    elif(op3 == '3'):
                                        fecha_nacimiento = input("Ingrese Fecha de Nacimiento: ")                                        
                                        enfermero.set_fecha_nacimiento(validar_fehca1(fecha_nacimiento))
                                    elif(op3 == '4'):
                                        numero_vacunas = input("Ingrese Numero de Vacunas: ")                                        
                                        enfermero.set_numero_vacunas(validar_numero_vacunas(numero_vacunas))
                                    elif(op3 == '5'):
                                        experiencia_profesional = input("Ingrese Experencia profesional en numero de años: ")                                        
                                        enfermero.set_experiencia_profecional(validar_experiencia_profecional(experiencia_profesional))
                                    elif(op3 == '6'):
                                        nombre = input("Ingrese Nombre: ")                                        
                                        enfermero.set_nombre(validar_nombre(nombre))      

                                        apellido = input("Ingrese Apellido: ")                                        
                                        enfermero.set_apellido(validar_apellido(apellido))      

                                        fecha_nacimiento = input("Ingrese Fecha de Nacimiento: ")                                        
                                        enfermero.set_fecha_nacimiento(validar_fehca1(fecha_nacimiento))

                                        numero_vacunas = input("Ingrese Numero de Vacunas: ")                                        
                                        enfermero.set_numero_vacunas(validar_numero_vacunas(numero_vacunas))

                                        experiencia_profesional = input("Ingrese Experencia profesional en numero de años: ")                                        
                                        enfermero.set_experiencia_profecional(validar_experiencia_profecional(experiencia_profesional))

                                    elif(op3 == '7'):
                                        break
                                    else:
                                        print("\nLa opcion ingresada no esta en la lista. Reintente.\n")
                                        os.system("pause")
                                else:
                                    print("\nERROR... El valor Ingresado debe ser un Numero... \n\n")
                                    os.system("pause")
                        else:
                            print("\nNo se encontro el nombre del Enfermero ingresado\n")
                            os.system("pause")       
                else:
                    print("\n Debe ingresar primero Datos de Enfermero \n")
                    os.system("pause")       

            #Editar datos Paciente
            elif(op2 == '3'):
                print("\n\n*********************************************************************************************************************************************************")
                print("**** Editar Datos Paciente: ****:\n")                            
                for paciente in lista_pacientes:
                    paciente.mostrar_informacion()
                    print("-----------------------------------------------------------------------------------------------------------------------------------------------------\n")

                nombre = input("Ingrese el Nombre del Paciente a editar: ")
                if(len(lista_pacientes) != 0):
                    for paciente in lista_pacientes:
                        if paciente.get_nombre() == nombre:
                            while(op3 != 11):
                                print("1 - Nombre: ", paciente.get_nombre())
                                print("2 - Apellido: ", paciente.get_apellido())
                                print("3 - Fecha de Nacimiento: ", paciente.get_fecha_nacimiento())
                                print("4 - Peso: ", paciente.get_peso())
                                print("5 - Talla: ", paciente.get_talla())
                                print("6 - Temperatura: ", paciente.get_temperatura())
                                print("7 - Tipo de Sangre: ", paciente.get_tipo_sangre())
                                print("8 - Motivo de Consulta: ", paciente.get_motivo_consulta())
                                print("9 - Sintomas: ", paciente.get_sintomas())
                                print("10 - Editar Todos lo Datos de Paciente")
                                print("11 - Regresar al Menu Editar")
                                op3 = input("\nEliga una opcion: ")
                                if(op3.isnumeric()):
                                    if(op3 == '1'):
                                        nombre = input("Ingrese Nombre: ")                                        
                                        paciente.set_nombre(validar_nombre(nombre))
                                    elif(op3 == '2'):
                                        apellido = input("Ingrese Apellido: ")                                        
                                        paciente.set_apellido(validar_apellido(apellido))
                                    elif(op3 == '3'):
                                        fecha_nacimiento = input("Ingrese Fecha de Nacimiento: ")                                        
                                        paciente.set_fecha_nacimiento(validar_fehca1(fecha_nacimiento))
                                    elif(op3 == '4'):
                                        peso = input("Ingrese el Peso: ")                                        
                                        paciente.set_peso(validar_peso(peso))
                                    elif(op3 == '5'):
                                        talla = input("Ingrese la Talla: ")                                        
                                        paciente.set_talla(validar_talla(talla))
                                    elif(op3 == '6'):
                                        temperatura = input("Ingrese la Temperatura: ")                                        
                                        paciente.set_temperatura(validar_temperatura(temperatura))
                                    elif(op3 == '7'):
                                        tipo_sangre = input("Ingrese Tipo de Sangre: ")                                        
                                        paciente.set_tipo_sangre(validar_tipo_sangre(tipo_sangre))
                                    elif(op3 == '8'):
                                        motivo_consulta = input("Ingrese Motivo de Consulta: ")                                        
                                        paciente.set_motivo_consulta(validar_motivo_consulta(motivo_consulta))
                                    elif(op3 == '9'):
                                        sintomas = input("Ingrese los Sintomas: ")                                        
                                        paciente.set_sintomas(validar_sintomas(sintomas))

                                    elif(op3 == '10'):
                                        nombre = input("Ingrese Nombre: ")                                        
                                        paciente.set_nombre(validar_nombre(nombre))

                                        apellido = input("Ingrese Apellido: ")                                        
                                        paciente.set_apellido(validar_apellido(apellido))

                                        fecha_nacimiento = input("Ingrese Fecha de Nacimiento: ")                                        
                                        paciente.set_fecha_nacimiento(validar_fehca1(fecha_nacimiento))

                                        peso = input("Ingrese el Peso: ")                                        
                                        paciente.set_peso(validar_peso(peso))

                                        talla = input("Ingrese la Talla: ")                                        
                                        paciente.set_talla(validar_talla(talla))

                                        temperatura = input("Ingrese la Temperatura: ")                                        
                                        paciente.set_temperatura(validar_temperatura(temperatura))

                                        tipo_sangre = input("Ingrese Tipo de Sangre: ")                                        
                                        paciente.set_tipo_sangre(validar_tipo_sangre(tipo_sangre))

                                        motivo_consulta = input("Ingrese Motivo de Consulta: ")
                                        paciente.set_motivo_consulta(validar_motivo_consulta(motivo_consulta))

                                        sintomas = input("Ingrese los Sintomas: ")                                        
                                        paciente.set_sintomas(validar_sintomas(sintomas))


                                    elif(op3 == '11'):
                                        break
                                    else:
                                        print("\nLa opcion ingresada no esta en la lista. Reintente.\n")
                                        os.system("pause")
                                else:
                                    print("\nERROR... El valor Ingresado debe ser un Numero... \n\n")
                                    os.system("pause")
                        else:
                            print("\nNo se encontro el codigo de registro profesional del medico ingresado\n")
                            os.system("pause")      
                else:
                    print("\n Debe ingresar primero Datos de Paciente \n")
                    os.system("pause")       


            elif(op2 == '4'):
                break

            else:
                print("\nLa opcion ingresada no esta en la lista. Reintente.")  
        else:
            print("\nERROR... El valor Ingresado debe ser un Numero... \n\n")
            os.system("pause")

def Imprimir_Datos():
    op3 = 0
    while(op3 != 5):
        print("\n\n**** Imprimir Lista de Datos ****:")
        print("1 - Lista de Medicos")
        print("2 - Lista de Enfermeros")
        print("3 - Lista de Pacientes")
        print("4 - Todas las listas")
        print("5 - Regresar al Menu")
        op3 = input("Elija una Opcion: ")
        if(op3.isnumeric()):
            if(op3 == '1'):
                print("\n\n*********************************************************************************************************************************************************")
                print("**** Lista de Medicos ****\n")
                if(len(lista_medicos) != 0):
                    for medico in lista_medicos:
                        medico.mostrar_informacion()
                        print("------------------------------------------------------------------------------------------------------------------------------------------------\n")
                else:
                    print("\n No hay ningun Medico Registrado")

            elif(op3 == '2'):
                print("\n\n*********************************************************************************************************************************************************")
                print("**** Lista Enfermeros ****\n")
                if(len(lista_enfermeros) != 0):
                    for enfermero in lista_enfermeros:
                        enfermero.mostrar_informacion()
                        print("------------------------------------------------------------------------------------------------------------------------------------------------\n")
                else:
                    print("\n No hay ningun Enfermero Registrado")

            elif(op3 == '3'):
                print("\n\n*********************************************************************************************************************************************************")
                print("**** Lista de Pacientes ****\n")
                if(len(lista_pacientes) != 0):
                    for paciente in lista_pacientes:
                        paciente.mostrar_informacion()
                        print("------------------------------------------------------------------------------------------------------------------------------------------------\n")
                else:
                    print("\n No hay ningun Paciente Registrado")

            elif(op3 == '4'):
                if(len(lista_medicos) != 0 or len(lista_enfermeros) != 0 or len(lista_pacientes) !=0 ):
                    print("\n\n*********************************************************************************************************************************************************")
                    print("**** Lista de Medicos ****\n")                        
                    for medico in lista_medicos:
                        medico.mostrar_informacion()
                        print("------------------------------------------------------------------------------------------------------------------------------------------------\n")
                    if(len(lista_medicos == 0)):
                        print("\n No hay ningun Medico registrado ")

                    print("\n\n*********************************************************************************************************************************************************")
                    print("**** Lista Enfermeros ****\n")
                    for enfermero in lista_enfermeros:
                        enfermero.mostrar_informacion()
                        print("------------------------------------------------------------------------------------------------------------------------------------------------\n")
                    if(len(lista_enfermeros == 0)):
                        print("\n No hay ningun Enfermero registrado ")

                    print("\n\n*********************************************************************************************************************************************************")
                    print("**** Lista de Pacientes ****\n")
                    for paciente in lista_pacientes:
                        paciente.mostrar_informacion()
                        print("------------------------------------------------------------------------------------------------------------------------------------------------\n")
                    if(len(lista_pacientes == 0)):
                        print("\n No hay ningun Paciente registrado ")

                else:                    
                    print("\n No hay ningun Dato registrado aun")
                    
                

            elif(op3 == '5'):
                break
            else:
                print("\nLa opcion ingresada no esta en la lista. Reintente.")  
        else:
            print("\nERROR... El valor Ingresado debe ser un Numero Entero... \n\n")
            os.system("pause")

#Funcion principal ejercicio 2
def ejercicio2():
    try:
        opcion = 0
        #while de menu de opciones
        while opcion != 4:

            #Menu de opciones
            print("\n\nMENU:")
            print("1 - Ingresar datos")
            print("2 - Editar datos")
            print("3 - Imprimir listados")
            print("4 - Salir De la App")
            opcion = input("\nEliga una opcion: ")            

            if(opcion.isnumeric()):  
                #Ingreso de datos
                if opcion == '1': 
                    Ingresar_Datos()                                           
                #Editar los Datos Por Gets y Sets
                elif opcion == '2':
                    Editar_Datos()
                #Imprimo la lista Datos
                elif opcion == '3':
                    Imprimir_Datos()
                #Salir del while de menu y del programa
                elif opcion == '4':
                    print("\n\n*** Adios *** (Gracias por utilizar la App)")
                    os,os.system("pause")
                    break
                #Valida Las opciones del menu
                else:
                    print("\nLa opcion ingresada no esta en la lista. Reintente.")
            else:
                print("\nERROR... El valor Ingresado debe ser un Numero Entero... \n\n")
                os.system("pause")

    except ValueError:
        print("\nSe ingreso un valor incorrecto. El programa finalizara.")
    except:
        print(sys.exc_info()[1])
        print("\nError inesperado. El programa finalizara.")
    
#Final ejercicio 2)    

#Inicio del Ejercicio 3 de la linea [979 a la ](

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


def ejercicio3():
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

#Final del ejercicio 3

#Funcion Principal Main
def main():
    op = 0
    while(op != 4):
        #Menu de opciones
        print("\n\nMENU:")
        print("1 - Ejercicio 1")
        print("2 - Ejercicio 2")
        print("3 - Ejercicio 3")
        print("4 - Salir del programa")
        op = input("\nEliga una opcion: ")
        while(len(op) < 1 or not op.isnumeric()):
            print("\n(¡ALERTA!) La OPCION debe tener un caracter y debe ser un numero")
            op = input("\nEliga una opcion: ")
        if(op == '1'):
            print("\n************************************* Bienvenido Al Ejercicio (1) *************************************")
            ejercicio1()
        elif(op == '2'):
            print("\n************************************* Bienvenido Al Ejercicio (2) *************************************")
            ejercicio2()
        elif(op == '3'):
            print("\n************************************* Bienvenido Al Ejercicio (3) *************************************")
            ejercicio3()
        elif(op == '4'):
            print("\n\nHa salido Gracias por Usar la App")            
            break
        else:
            print("\nLa opcion ingresada no se encuentra en la Lista. Reintente.")
main()