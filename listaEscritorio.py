from nodoEscritorio import nodoEscritorio


class listaEscritorio:

    def __init__(self):
        
        self.primerNodo = None
        self.ultimoNodo = None
        self.tamaño = 0

    def insetar(self, escritorio):

        nuevo = nodoEscritorio(escritorio)
        self.tamaño +=1

        print('entra')
        if self.primerNodo == None: # ciclo para validar si la lista esta vacia 
            self.primerNodo = nuevo
            self.ultimoNodo = nuevo
        else:
            self.ultimoNodo.siguiente = nuevo #indicamos que el siguiente del ultimo nodo sera el nuevo nodo 
            self.ultimoNodo = nuevo #para decir que el ultimo es el nuevo 


    def mostrar(self):

        temp = self.primerNodo
        print('Escritorios: ')
        while temp: 

            print('ID: '+str(temp.escritorio.idescritorio),' Identificacion: '+str(temp.escritorio.identifiacionescritorio),' Nombre Encargado: '+str(temp.escritorio.encargado))
            temp = temp.siguiente