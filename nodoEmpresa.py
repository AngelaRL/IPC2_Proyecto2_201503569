from listaPunto import listaPunto
from listaTransaccion import listaTransaccion


class nodoEmpresa:

    def __init__(self, empresa):
        self.empresa = empresa
        self.listaPuntos = listaPunto()
        self.listaTrans = listaTransaccion()
        self.siguiente = None