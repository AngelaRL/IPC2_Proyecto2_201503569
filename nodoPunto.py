from listaEscritorio import listaEscritorio


class nodoPunto:
    def __init__(self, punto):
        self.punto = punto
        self.listaEs = listaEscritorio()
        self.siguiente = None