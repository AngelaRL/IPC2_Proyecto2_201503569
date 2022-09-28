from re import A
from nodo import nodo
from cliente import cliente
import xml.etree.ElementTree as ET
from xml.dom import minidom

class listaInicial:

    def __init__(self):
        
        self.primerNodo = None
        self.ultimoNodo = None
        self.tamaño = 0

    def insetar(self, dato):

        nuevo = nodo(dato)
        self.tamaño +=1

        if self.primerNodo == None: # ciclo para validar si la lista esta vacia 
            self.primerNodo = nuevo
            self.ultimoNodo = nuevo
        else:
            self.ultimoNodo.siguiente = nuevo #indicamos que el siguiente del ultimo nodo sera el nuevo nodo 
            self.ultimoNodo = nuevo #para decir que el ultimo es el nuevo 

    def cargarEmpresas(self, rutaArchivo):
        print('Empezando a analizar el archivo...')

        #para los datos de la configuracion inicial 
        idConfiguracion = 0
        idEmpresa = 0
        idPunto = 0
        #para los datos de escritorios activos
        idEscritorio = 0
        #para los datos de los clientes:
        dpiCliente = 0
        nombreCliente = ''
        #para los datos de transaccion:
        idTransaccion = 0
        cantidad = 0

        #para la lectura del .xml
        leer = ET.parse(rutaArchivo)
        root = leer.getroot() #raiz

        #para extraer los elementos 

        print(rutaArchivo)

        for elementoArchivo in root:
            idConfiguracion = ''
            idEmpresa =''
            idPunto =''
            auxClientes = None
            auxTransacciones = None
            auxConfi = None
            auxEscritorio = None

            if elementoArchivo.tag == 'configInicial':

                idConfiguracion = elementoArchivo.get('id')
                idEmpresa = elementoArchivo.get('idEmpresa')
                idPunto = elementoArchivo.get('idPunto')

                for subElemento in elementoArchivo:

                    if subElemento.tag == 'escritoriosActivos':

                        for ssElemento in subElemento:

                            if ssElemento.tag == 'escritorio':

                                idEscritorio = ssElemento.get('idEscritorio')

                    elif subElemento.tag == 'listadoClientes':

                        for ssElemento in subElemento:

                            if ssElemento.tag == 'cliente':
                                dpiCliente = ssElemento.get('dpi')

                                for sssElemento in ssElemento:

                                    if sssElemento.tag == 'nombre':

                                        nombreCliente = ssElemento.text

                                        auxClientes = cliente(int(dpiCliente), nombreCliente)

                                    elif sssElemento.tag == 'listadoTransacciones':

                                        for ssssElemento in sssElemento:

                                            if ssssElemento.tag == 'transaccion':
                                                idTransaccion = ssssElemento.get('idTransaccion')
                                                cantidad = ssssElemento.get('cantidad')





                        