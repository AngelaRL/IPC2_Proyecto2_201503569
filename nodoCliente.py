from listaTransaccion import listaTransaccion

class nodoCliente: 

    def __init__(self, cliente) -> None:
        self.cliente = cliente
        self.transacciones = listaTransaccion()
        self.siguiente = None