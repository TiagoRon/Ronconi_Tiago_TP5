class NodoArbol:
    def __init__(self, nombre, es_heroe):
        self.nombre = nombre
        self.es_heroe = es_heroe
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, nombre, es_heroe):
        if self.raiz is None:
            self.raiz = NodoArbol(nombre, es_heroe)
        else:
            self._insertar(self.raiz, nombre, es_heroe)

    def _insertar(self, nodo, nombre, es_heroe):
        if nombre < nodo.nombre:
            if nodo.izquierdo is None:
                nodo.izquierdo = NodoArbol(nombre, es_heroe)
            else:
                self._insertar(nodo.izquierdo, nombre, es_heroe)
        else:
            if nodo.derecho is None:
                nodo.derecho = NodoArbol(nombre, es_heroe)
            else:
                self._insertar(nodo.derecho, nombre, es_heroe)
