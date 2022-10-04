from ast import Num
from turtle import st
import xml.etree.ElementTree as AE
import os

from listaEmpresa import listaEmpresa
from listaInicial import listaInicial 

salir = False
ruta1 = None
ruta2 = None

def menuprincipal():
    global salir, ruta
    opcion = 0
    subopcion =0
    while not salir:
        print("::::::::::::::::::::::::::::::::::: MENU :::::::::::::::::::::::::::::::::::")
        print("")
        print("Ingrese el numero de la opcion que desea:")
        print("")
        print("")
        print("")
        print("1. Configuracion de empresas ")
        print("2. Seleccion de empresa y punto de atencion ") 
        print("3. Manejo de puntos de atencion ")
        print("4. Salir ")
        print("")
        print("")
        print("")
    

        opcion = int(input("ingrese el numero:    "))

        if opcion == 1:

            menuConfiguracion()          
            
        elif opcion == 2:
            print('')

        elif opcion == 3:
            print('')
            
        elif opcion == 4:
            salir = True
            print("Cerrando programa")
        else:
            print("Opcion invalida")

def menuConfiguracion():
    global salir, ruta
    
    while not salir:
        print("")
        print("")
        print('::::::::::::::: CONFIGURACION DE EMPRESAS :::::::::::::::::')
        print("")
        print("")
        print("1. Limpiar sistema ")
        print("2. Cargar Archivo de configruacion del sistema ")
        print("3. Crear nueva empresa ")
        print("4. cargar archivo con configuracion incial")
        print("5. regresar al menu principal")
        print("")
        print("")
        print("")
        print("")

        subopcion = int(input("ingrese el numero de la opcion que desea: "))

        if subopcion == 1:
            print("Empezando a analizar Automaticamente:  ")
           
        elif subopcion == 2:
            ruta1 = listaEmpresa()

            print("Ingrese la ruta del archivo: ")
            
            rutaArchivo = input('  ') 
            print("")

            if os.path.exists(rutaArchivo):
                ruta1.cargarEmpresas(rutaArchivo)
            else:
                print('Verifique el nombre del archivo  ')
        
        elif subopcion == 3:
            print('')
            print(':::::::::::::::::::::::: NUEVA EMPRESA ::::::::::::::::::::::::')
            
            listaEmpresa.crearEmpresa()

        elif subopcion == 4:
            print('sdfsdf')

            ruta2 = listaInicial()

            print("Ingrese la ruta del archivo: ")
            rutaArchivo2 = input('  ')

            
            if os.path.exists(rutaArchivo2):
                ruta2.cargarConfiguracion(rutaArchivo2)
            else:
                print('Verifique el nombre del archivo  ')

        elif subopcion == 5: 
            menuprincipal()       
        else:
            print("opcion no valida")

if __name__ == "__main__":
    menuprincipal()