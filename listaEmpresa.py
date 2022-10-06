
from empresa import empresa
from escritorio import escritorio
from nodoPunto import nodoPunto
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

    def insetar(self, nuevo):
        if self.repetidos(nuevo.empresa.idempresa):

            self.tamaño +=1

            if self.primerNodo == None: # ciclo para validar si la lista esta vacia 
                self.primerNodo = nuevo
                self.ultimoNodo = nuevo
            else:
                self.ultimoNodo.siguiente = nuevo #indicamos que el siguiente del ultimo nodo sera el nuevo nodo 
                self.ultimoNodo = nuevo #para decir que el ultimo es el nuevo 

    def mostrar(self):

        temp = self.primerNodo
        contador = 1 
        print('EMPRESAS: ')
        while contador<= self.tamaño: 

            print(str(contador)+') ','ID: '+str(temp.empresa.idempresa),' Nombre: '+temp.empresa.nombre,' Abreviatura: '+temp.empresa.abreviatura)
 
            temp = temp.siguiente
            contador+=1

    def obtenerEmpresa(self,seleccion):
        temp = self.primerNodo
        contador = 1 
        
        while contador<= self.tamaño: 

            if contador == seleccion:
                return temp

            temp = temp.siguiente
            contador+=1

    def repetidos(self, id):
        temp = self.primerNodo
         
        print('EMPRESAS: ')
        while temp: 
            if temp.empresa.idempresa == id:
                return False
            temp = temp.siguiente
        return True
            

    def cargarEmpresas(self, rutaArchivo):
        print('Empezando a analizar el archivo...')

        #para los datos de la empresa
        idEmpresa = ''
        nombreEmpresa =''
        abreviaturaE = ''
        #para los datos de puntos de atencion 
        idPunto = ''
        nombrePunto = ''
        direccionPunto = ''
        #para los datos de los escritorios:
        idEscritorio = ''
        identifiacionEscritorio = ''
        nombreEncargado = ''
        #para los datos de transaccion:
        idTransaccion = ''
        nombreTransaccion = ''
        tiempoAtencion = 0

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

                        auxEmpresa = nodoEmpresa(empresa(idEmpresa, nombreEmpresa, abreviaturaE)) 

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

                                        auxPuntos = nodoPunto(puntoAtencion(idPunto, nombrePunto, direccionPunto))
                                                                                
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

                                                        auxEscritorio = escritorio(idEscritorio, identifiacionEscritorio, nombreEncargado)
                                                        print(auxPuntos.punto.nombre)
                                                        auxPuntos.listaEs.insetar(auxEscritorio)

                                                        del auxEscritorio 
                                   
                                        auxEmpresa.listaPuntos.insetar(auxPuntos)
                                        auxPuntos = None
                    
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

                                        auxTransaccion = transaccion(idTransaccion, nombreTransaccion,int(tiempoAtencion),0)
                                        auxEmpresa.listaTrans.insetar(auxTransaccion)
                                        auxTransaccion = None
                    
                self.insetar(auxEmpresa)
                auxEmpresa = None
        

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
            auxEmpresa = nodoEmpresa(empresa(idE,nombreE,abreviaturaE))

            print('Datos puntos de atencion:  ')

            while opcion == True:
                print('Ingrese el ID del punto de atencion: ')
                idPunto = input('   ')
                print('Ingrese el nombre del punto de atencion: ')
                nombreP = input('   ')
                print('Ingrese la direccion del punto de atencion: ')
                direccionP = input('   ')

                auxPuntos = nodoPunto(puntoAtencion(idPunto, nombreP,direccionP))

                print('Datos puntos de los escritorios:  ')

                while opcion == True:
                        print('Ingrese el ID del escritorio: ')
                        idEscritori = input('   ')
                        print('Ingrese la identificacion del escritorio:')
                        identifiEs = input('   ')
                        print('Ingrese el nombre del encargado del escritorio: ')
                        nombreEncargado = input('   ')

                        auxEscritorio = escritorio(idEscritori,identifiEs,nombreEncargado)
                        auxPuntos.listaEs.insetar(auxEscritorio)
                        auxEscritorio = None
                        

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
                auxEmpresa.listaPuntos.insetar(auxPuntos)
                auxPuntos = None

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
                    
                        
            print('Datos de las Transacciones: ')
            opcion = True
            while opcion == True:
                print('Ingrese el ID de la transaccion: ')
                idT = input('   ')
                print('Ingrese el nombre de la transaccion: ')
                nombreT = input('   ')
                print('Ingrese el tiempo de atencion en minutos: ')
                tiempoA = input('   ')

                auxTransaccion = transaccion(idT,nombreT,tiempoA,0)
                auxEmpresa.listaTrans.insetar(auxTransaccion)
                auxTransaccion = None
                

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
                        

            self.insetar(auxEmpresa)
            auxEmpresa = None

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
        

    

    