from listaClientes import listaClientes
from listaEscritorio import listaEscritorio


class nodoInicial:

    def __init__(self, dato):
        self.dato = dato
        self.escritorios = listaEscritorio()
        self.clientes = listaClientes()
        self.siguiente = None

