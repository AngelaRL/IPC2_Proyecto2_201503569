from logging import root
from select import select
from empresa import empresa
from escritorio import escritorio
from transaccion import transaccion
from nodoEmpresa import nodoEmpresa
import xml.etree.ElementTree as ET
from xml.dom import minidom

from puntoAtencion import puntoAtencion


class listaEmpresa:

    def __init__(self):
        
        self.primerNodo = None
        self.ultimoNodo = None
        self.tamaño = 0

    def insetar(self, empresa):

        nuevo = nodoEmpresa(empresa)
        self.tamaño +=1

        if self.primerNodo == None: # ciclo para validar si la lista esta vacia 
            self.primerNodo = nuevo
            self.ultimoNodo = nuevo
        else:
            self.ultimoNodo.siguiente = nuevo #indicamos que el siguiente del ultimo nodo sera el nuevo nodo 
            self.ultimoNodo = nuevo #para decir que el ultimo es el nuevo 

    def cargarEmpresas(self, rutaArchivo):
        print('Empezando a analizar el archivo...')

        #para los datos de la empresa
        idEmpresa = 0
        nombreEmpresa =''
        abreviaturaE = ''
        #para los datos de puntos de atencion 
        idPunto = 0
        nombrePunto = ''
        direccionPunto = ''
        #para los datos de los escritorios:
        idEscritorio = 0
        identifiacionEscritorio = ''
        nombreEncargado = ''
        #para los datos de transaccion:
        idTransaccion = 0
        nombreTransaccion = ''
        tiempoAtencion = ''

        #para la lectura del .xml
        leer = ET.parse(rutaArchivo)
        root = leer.getroot() #raiz

        #para extraer los elementos 

        print(rutaArchivo)

        for elementoArchivo in root:
            idEmpresa =''
            nombreEmpresa =''
            abreviaturaE = ''
            nombreEncargado = ''
            idEscritorio = ''
            identifiacionEscritorio = ''
            auxEmpresa = None
            auxPuntos = None
            auxEscritorio = None
            auxTransaccion = None
            print('-----------------------------------------------------------------------')
            if elementoArchivo.tag == 'empresa':

                print('Obteniendo Empresa...')
                print('Registrando los datos de la empresa...')

                idEmpresa = elementoArchivo.get('id')
                print('ID empresa: ',idEmpresa)

                for subElemento in elementoArchivo:

                    if subElemento.tag == 'nombre':

                        nombreEmpresa = subElemento.text
                        print('Nombre: ',nombreEmpresa)
                    
                    elif subElemento.tag == 'abreviatura':

                        abreviaturaE = subElemento.text
                        print('Abreviatura: ',abreviaturaE)

                        auxEmpresa = empresa(int(idEmpresa), nombreEmpresa, abreviaturaE) 

                    elif subElemento.tag == 'listaPuntosAtencion':
                        print('Cargando puntos de atencion... ')

                        for ssElemnto in subElemento:

                            if ssElemnto.tag == 'puntoAtencion':

                                idPunto = ssElemnto.get('id')
                                print('     ID punto de atencion: ', idPunto)

                                for sssElemento in ssElemnto:

                                    if sssElemento.tag == 'nombre':

                                        nombrePunto = sssElemento.text
                                        print('     nombre: ', nombrePunto)
                                    elif sssElemento.tag == 'direccion':

                                        direccionPunto = sssElemento.text
                                        print('     direccion: ', direccionPunto)

                                        auxPuntos = puntoAtencion(int(idPunto), nombrePunto, direccionPunto)
                                        
                                    elif sssElemento.tag == 'listaEscritorios':
                                        print('Cargando Escritorios...')

                                        for ssssElemento in sssElemento:

                                            if ssssElemento.tag == 'escritorio':

                                                idEscritorio = ssssElemento.get('id')
                                                print('     id escritorio: ',idEscritorio)

                                                for susubElemento in ssssElemento:


                                                    if susubElemento.tag == 'identificacion':

                                                        identifiacionEscritorio = susubElemento.text
                                                        print('     identificacion: ',identifiacionEscritorio)
                                                    elif susubElemento.tag == 'encargado':

                                                        nombreEncargado = susubElemento.text
                                                        print('     encargado: ',nombreEncargado)

                                                        auxEscritorio = escritorio(int(idEscritorio), identifiacionEscritorio, nombreEncargado)
                                            self.insetar(auxEscritorio)
                                   
                            self.insetar(auxPuntos)
                    
                    elif subElemento.tag == 'listaTransacciones':
                        print('Cargando transacciones... ')

                        for ssElemento in subElemento:

                            if ssElemento.tag == 'transaccion':

                                idTransaccion = ssElemento.get('id')
                                print('     ID: ',idTransaccion)

                                for sssElemento in ssElemento:

                                    if sssElemento.tag == 'nombre':
                                        nombreTransaccion = sssElemento.text
                                        print('     nombre: ',nombreTransaccion)
                                    elif sssElemento.tag == 'tiempoAtencion':
                                        tiempoAtencion = sssElemento.text
                                        print('     Tiempo Atencion: ', tiempoAtencion)

                                        auxTransaccion = transaccion(int(idTransaccion), nombreTransaccion,tiempoAtencion,0)
                    self.insetar(auxTransaccion)
                    
            self.insetar(auxEmpresa)

    def crearEmpresa(self):
        opcion = True

        auxEmpresa = None
        auxPuntos = None
        auxEscritorio = None
        auxTransaccion = None

        while opcion == True:

            print('Datos de la empresa:')

            print('Ingrese el ID de la empresa: ')
            idE = input('   ')
            print('Ingrese el nombre de la empresa: ')
            nombreE = input('   ')
            print('Ingrese la abreviatura de la empresa: ')
            abreviaturaE = input('   ')

            print('Datos puntos de atencion:  ')

            while opcion == True:
                print('Ingrese el ID del punto de atencion: ')
                idPunto = input('   ')
                print('Ingrese el nombre del punto de atencion: ')
                nombreP = input('   ')
                print('Ingrese la direccion del punto de atencion: ')
                direccionP = input('   ')

                auxPuntos = puntoAtencion(idPunto, nombreP,direccionP)
                self.insetar(auxPuntos)

                print('¿Desea agregar otro punto de atencion?')
                print('1. si')
                print('2. No')

                respuesta = int(input("ingrese el numero de la opcion que desea: "))

                if respuesta == 1:
                    opcion = True
                elif respuesta == 2:
                    opcion = False
                else:
                    print("opcion no valida")

            print('Datos puntos de los escritorios:  ')

            while opcion == True:
                print('Ingrese el ID del escritorio: ')
                idEscritori = input('   ')
                print('Ingrese el nombre del encargado del escritorio: ')
                nombreEncargado = input('   ')

                auxEscritorio = escritorio(idEscritori,nombreEncargado)
                self.insetar(auxEscritorio)

                print('¿Desea agregar otro escritorio?')
                print('1. si')
                print('2. No')

                respuesta = int(input("ingrese el numero de la opcion que desea: "))

                if respuesta == 1:
                    opcion = True
                elif respuesta == 2:
                    opcion = False
                else:
                    print("opcion no valida")
            
            print('Datos de las Transacciones: ')
        
            while opcion == True:
                print('Ingrese el ID de la transaccion: ')
                idT = input('   ')
                print('Ingrese el nombre de la transaccion: ')
                nombreT = input('   ')
                print('Ingrese el tiempo de atencion en minutos: ')
                tiempoA = input('   ')

                auxTransaccion = transaccion(idT,nombreT,tiempoA,0)
                self.insetar(auxTransaccion)

                print('¿Desea agregar otra transaccion?')
                print('1. si')
                print('2. No')

                respuesta = int(input("ingrese el numero de la opcion que desea: "))

                if respuesta == 1:
                    opcion = True
                elif respuesta == 2:
                    opcion = False
                else:
                    print("opcion no valida")


            auxEmpresa=empresa(idE, nombreE, abreviaturaE)
            self.insetar(auxEmpresa)

            print('¿Desea agregar otra empresa?')
            print('1. si')
            print('2. No')

            respuesta = int(input("ingrese el numero de la opcion que desea: "))

            if respuesta == 1:
                opcion = True
            elif respuesta == 2:
                opcion = False
            else:
                print("opcion no valida")
        

    def mostrarEmpresas(self):
        actual = self.primerNodo

        while actual != None: #mientras sea diferente de vacio
            print('Empresa: ',actual.empresa.nombre)
            actual = actual.siguiente #con esto indicamos que vamos a avanzar al siguiente nodo (recorre la lista)
        print('------------------------------------------------------')


    