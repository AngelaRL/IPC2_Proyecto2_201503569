from nodoPunto import nodoPunto


class listaPunto:

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

        print('Puntos de atencion: ')

        while temp: 

            print('ID: '+str(temp.punto.idpunto),' Nombre: '+temp.punto.nombre,' Direccion: '+temp.punto.direccion)
            temp.listaEs.mostrar()
            
            temp = temp.siguiente