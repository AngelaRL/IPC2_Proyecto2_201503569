from ast import Num
from turtle import st
import xml.etree.ElementTree as AE
import os

from listaEmpresa import listaEmpresa
from listaInicial import listaInicial 

salir = False
ruta1 = listaEmpresa()
ruta2 = listaInicial()

def menuprincipal():
    global salir
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
        print("3. Salir ")
        print("")
        print("")
        print("")
    

        opcion = int(input("ingrese el numero:    "))

        if opcion == 1:

            menuConfiguracion()          
            
        elif opcion == 2:
            print('::::::::::::::: SELECCION DE EMPRESA Y PUNTO DE ATENCION :::::::::::::::::')



            menuPuntos()
            
        elif opcion == 3:
            salir = True
            print("Cerrando programa")
        else:
            print("Opcion invalida")

def menuConfiguracion():
    global salir, ruta1, ruta2
    
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
            ruta1 = listaEmpresa()
            ruta2 = listaInicial()
            print("Limpiando el sistema...  ")
           
        elif subopcion == 2:
            print(':::::::::::::::::::::::: CONFIGURACION DEL SISTEMA ::::::::::::::::::::::::')
            op = True
            

            while op == True:

                print("Ingrese la ruta del archivo: ")
            
                rutaArchivo = input('  ') 
                print("")

                if os.path.exists(rutaArchivo):
                    ruta1.cargarEmpresas(rutaArchivo)
                else:
                    print('Verifique el nombre del archivo  ')

                print('¿Desea cargar otro archivo?')
                print('1. si')
                print('2. No')

                respuesta = int(input("ingrese el numero de la opcion que desea: "))

                if respuesta == 1:
                    op = True
                elif respuesta == 2:
                    op = False
                else:
                    print("opcion no valida")
        
        elif subopcion == 3:
            print('')
            print(':::::::::::::::::::::::: NUEVA EMPRESA ::::::::::::::::::::::::')
            
            ruta1.crearEmpresa()

        elif subopcion == 4:
            print(':::::::::::::::::::::::: CONFIGURACION INICIAL ::::::::::::::::::::::::')
            op = True

            while op == True:

                print("Ingrese la ruta del archivo: ")
                rutaArchivo2 = input('  ')

                
                if os.path.exists(rutaArchivo2):
                    ruta2.cargarConfiguracion(rutaArchivo2)
                else:
                    print('Verifique el nombre del archivo  ')

                print('¿Desea cargar otro archivo?')
                print('1. si')
                print('2. No')

                respuesta = int(input("ingrese el numero de la opcion que desea: "))

                if respuesta == 1:
                    op = True
                elif respuesta == 2:
                    op = False
                else:
                    print("opcion no valida")

        elif subopcion == 5: 
            menuprincipal()       
        else:
            print("opcion no valida")

def menuPuntos():
    global salir, ruta
    
    while not salir:
        print("")
        print("")
        print('::::::::::::::: MANEJO DE PUNTOS DE ATENCION :::::::::::::::::')
        print("")
        print("")
        print("1. Estado de puntos de atencion ")
        print("2. Activar escritorio de servicio ")
        print("3. Desactivar Escritorio de servicio ")
        print("4. Atender Cliente")
        print("5. Solicitud de Atencion")
        print("6. Simular Actividad")
        print("7. Regresar a menu principal")
        print("")
        print("")
        print("")
        print("")

        subopcion = int(input("ingrese el numero de la opcion que desea: "))

        if subopcion == 1:
            print("Limpiando el sistema...  ")
           
        elif subopcion == 2:
            print(':::::::::::::::::::::::: CONFIGURACION DEL SISTEMA ::::::::::::::::::::::::')
           
        
        elif subopcion == 3:
            print('')
            print(':::::::::::::::::::::::: NUEVA EMPRESA ::::::::::::::::::::::::')
            
            listaEmpresa.crearEmpresa()

        elif subopcion == 4:
            print(':::::::::::::::::::::::: CONFIGURACION INICIAL ::::::::::::::::::::::::')
            
        elif subopcion == 5:
            print('')

        elif subopcion == 6:
            print('')

        elif subopcion == 7: 
            menuprincipal()       
        else:
            print("opcion no valida")

if __name__ == "__main__":
    menuprincipal()