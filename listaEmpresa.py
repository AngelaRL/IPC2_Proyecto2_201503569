from logging import root
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
        
                
                
          