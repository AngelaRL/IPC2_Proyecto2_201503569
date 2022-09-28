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
        print("1. Cargar datos ")
        print("2. Configuracion de empresas ")
        print("3. Seleccion de empresa y punto de atencion ") 
        print("4. Manejo de puntos de atencion ")
        print("5. Salir ")
        print("")
        print("")
        print("")
    

        opcion = int(input("ingrese el numero:    "))

        if opcion == 1:

            ruta1 = listaEmpresa()
            ruta2 = listaInicial()

            print("Ingrese la ruta del primer archivo: ")
            rutaArchivo = input('  ') 
            print("")
            print("Ingrese la ruta del segundo archivo: ")
            rutaArchivo2 = input('  ')
            
          
            
        elif opcion == 2:
            while not salir:
                print('::::::::::::::: CONFIGURACION DE EMPRESAS :::::::::::::::::')
               

                print("")
            salir = False
        elif opcion == 3:
            print('Generando archivo de salida...')

        elif opcion == 4:
            print('')
            
        elif opcion == 5:
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
        print("1. Analizar Muestra Automaticamente")
        print("2. Analizar Muestra por Periodo ")
        print("3. Regresar al menu principal ")
        print("")
        print("")
        print("")
        print("")
        print("")

        subopcion = int(input("ingrese el numero de la opcion que desea: "))

        if subopcion == 1:
            print("Empezando a analizar Automaticamente:  ")
           
        elif subopcion == 2:
            print('')
        
                    
        elif subopcion == 3: 
            salir=True
        else:
            print("opcion no valida")

if __name__ == "__main__":
    menuprincipal()