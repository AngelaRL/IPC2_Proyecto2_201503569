from nodoTransaccion import nodoTransaccion


class listaTransaccion:

    def __init__(self):
        
        self.primerNodo = None
        self.ultimoNodo = None
        self.tamaño = 0

    def insetar(self, transaccion):

        nuevo = nodoTransaccion(transaccion)
        self.tamaño +=1

        if self.primerNodo == None: # ciclo para validar si la lista esta vacia 
            self.primerNodo = nuevo
            self.ultimoNodo = nuevo
        else:
            self.ultimoNodo.siguiente = nuevo #indicamos que el siguiente del ultimo nodo sera el nuevo nodo 
            self.ultimoNodo = nuevo #para decir que el ultimo es el nuevo 


    def mostrar(self):

        temp = self.primerNodo

        print('Transacciones: ')

        while temp: 

            print('ID: '+str(temp.transaccion.idtransaccion),' Nombre: '+str(temp.transaccion.nombretransaccion),' Tiempo de Atencion: '+str(temp.transaccion.tiempoatencion),' Cantidad: '+str(temp.transaccion.cantidad))
            temp = temp.siguiente

    def mostrar2(self):

        temp = self.primerNodo

        print('Transacciones: ')

        while temp: 

            print('ID: '+str(temp.transaccion.idtransaccion),' Cantidad: '+str(temp.transaccion.cantidad))
            temp = temp.siguiente