from ast import Num
from turtle import st
import xml.etree.ElementTree as AE
import os 

salir = False
ruta = None

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
        print("")
        print("")
        print("")
    

        opcion = int(input("ingrese el numero:    "))

        if opcion == 1:

            #ruta = listaPaciente()

            print("ingrese la ruta del archivo")
            #rutaArchivo = input('  ') 
            print("")
            print("")
            
          
            
        elif opcion == 2:
            while not salir:
                print('::::::::::::::: Seccion de Pacientes :::::::::::::::::')
               

                print("")
            salir = False
        elif opcion == 3:
            print('Generando archivo de salida...')
            
        elif opcion == 4:
            salir = True
            print("Cerrando programa")
        else:
            print("Opcion invalida")

def menuPaciente(pacienteE):
    global salir, ruta
    contador = 1
    while not salir:
        print("")
        print("")
        print(":::::::::::  PACIENTE: "+pacienteE.paciente.nombre +" ::::::::::::")
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