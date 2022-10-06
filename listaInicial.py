from cliente import cliente
from escritorio import escritorio
from inicial import inicial
from nodoCliente import nodoCliente
from nodoInicial import nodoInicial
import xml.etree.ElementTree as ET
from xml.dom import minidom

from transaccion import transaccion

class listaInicial:

    def __init__(self):
        
        self.primerNodo = None
        self.ultimoNodo = None
        self.tamaño = 0

    def insetar(self, nuevo):

        self.tamaño +=1

        if self.primerNodo == None: # ciclo para validar si la lista esta vacia 
            self.primerNodo = nuevo
            self.ultimoNodo = nuevo
        else:
            self.ultimoNodo.siguiente = nuevo #indicamos que el siguiente del ultimo nodo sera el nuevo nodo 
            self.ultimoNodo = nuevo #para decir que el ultimo es el nuevo 

    def mostrar(self):

        temp = self.primerNodo

        while temp: 

            print('ID: '+str(temp.dato.id),' ID empresa: '+str(temp.dato.idEmpresa),' ID P.A.: '+str(temp.dato.idPunto))
            temp.escritorios.mostrar()
            temp.clientes.mostrar()
            print('--------------------------------------------------------------')
            temp = temp.siguiente

    def cargarConfiguracion(self, rutaArchivo):
        print('Empezando a analizar el archivo...')

        #para los datos de la configuracion inicial 
        idConfiguracion = ''
        idEmpresa = ''
        idPunto = ''
        #para los datos de escritorios activos
        idEscritorio = ''
        #para los datos de los clientes:
        dpiCliente = 0
        nombreCliente = ''
        #para los datos de transaccion:
        idTransaccion = ''
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
            nombreCliente= ''
            auxClientes = None
            auxTransacciones = None
            auxConfi = None
            auxEscritorio = None

            if elementoArchivo.tag == 'configInicial':
                print('Cargando configuracion...')
                idConfiguracion = elementoArchivo.get('id')
                idEmpresa = elementoArchivo.get('idEmpresa')
                idPunto = elementoArchivo.get('idPunto')

                print('ID: ',idConfiguracion)
                print('ID empresa: ',idEmpresa)
                print('ID punto de atencion:',idPunto)

                auxConfi = nodoInicial(inicial(idConfiguracion,idEmpresa,idPunto))

                for subElemento in elementoArchivo:

                    if subElemento.tag == 'escritoriosActivos':
                        print('Cargando escritorios activos...')

                        for ssElemento in subElemento:

                            if ssElemento.tag == 'escritorio':

                                idEscritorio = ssElemento.get('idEscritorio')
                                print('ID escritorio: ', idEscritorio)

                                auxEscritorio = escritorio(idEscritorio, None, None)
                                auxConfi.escritorios.insetar(auxEscritorio)
                                auxEscritorio= None

                    elif subElemento.tag == 'listadoClientes':
                        print('Cargando clientes....')

                        for ssElemento in subElemento:

                            if ssElemento.tag == 'cliente':
                                dpiCliente = ssElemento.get('dpi')
                                print('DPI: ', dpiCliente)

                                for sssElemento in ssElemento:

                                    if sssElemento.tag == 'nombre':

                                        nombreCliente = sssElemento.text
                                        print('Nombre: ',nombreCliente)

                                        auxClientes = nodoCliente(cliente(int(dpiCliente), nombreCliente))
                    
                                    elif sssElemento.tag == 'listadoTransacciones':
                                        print('Cargando Transacciones....')

                                        for ssssElemento in sssElemento:

                                            if ssssElemento.tag == 'transaccion':
                                                idTransaccion = ssssElemento.get('idTransaccion')
                                                cantidad = ssssElemento.get('cantidad')

                                                print('ID transaccion: ', idTransaccion)
                                                print('cantidad: ',cantidad)

                                                auxTransacciones = transaccion(idTransaccion,None,None,int(cantidad))
                                                auxClientes.transacciones.insetar(auxTransacciones)
                                                auxTransacciones = None
                                        auxConfi.clientes.insetar(auxClientes)
                                        auxClientes = None
                        self.insetar(auxConfi)
                        
                                
        self.mostrar()




                        