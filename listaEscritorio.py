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
        contador = 1

        print('Escritorios: ')
        while temp:
            print(str(contador)+') ','ID: '+str(temp.escritorio.idescritorio))
            temp = temp.siguiente
            contador +=1

    def mostrarActivos(self):

        temp = self.primerNodo
        contador = 0 
        print('Escritorios: ')
        while temp: 
            if temp.escritorio.estado:
                contador +=1
                print(str(contador)+') ','ID: '+str(temp.escritorio.idescritorio),' Identificacion: '+str(temp.escritorio.identifiacionescritorio),' Nombre Encargado: '+str(temp.escritorio.encargado))
            
            temp = temp.siguiente
        return contador

    def mostrarDesactivo(self):

        temp = self.primerNodo
        contador = 0 
        print('Escritorios: ')
        while temp: 
            if temp.escritorio.estado == False:
                contador +=1
                print(str(contador)+') ','ID: '+str(temp.escritorio.idescritorio),' Identificacion: '+str(temp.escritorio.identifiacionescritorio),' Nombre Encargado: '+str(temp.escritorio.encargado))
            
            temp = temp.siguiente
        return contador

    def mostrarCantidad(self):

        temp = self.primerNodo
        contador = 0 
        print('Cantidad de escritorios: ')
        while temp: 

            if temp.escritorio.estado:
                contador +=1
            temp = temp.siguiente
        print('Activos: '+str(contador))

        temp = self.primerNodo
        contador = 0 
        while temp: 

            if temp.escritorio.estado==False:
                contador +=1
            temp = temp.siguiente
        print('Inactivos: '+str(contador))

    def cambiarEstado(self,opcion,estado):
        cambiar = None
        busqueda = None

        if estado == 'activar':
            cambiar = True
            busqueda = False
        else:
            cambiar = False
            busqueda = True
        temp = self.primerNodo
        contador = 1 
        while temp: 
            if temp.escritorio.estado == busqueda:
                if contador==opcion:
                    temp.escritorio.estado = cambiar
                contador +=1
            temp = temp.siguiente 