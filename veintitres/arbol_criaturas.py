class NodoArbol:
    def __init__(self, nombre, derrotado_por=None, capturada_por=None, descripcion=""):
        self.nombre = nombre
        self.derrotado_por = derrotado_por
        self.capturada_por = capturada_por
        self.descripcion = descripcion
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, nombre, derrotado_por=None):
        if self.raiz is None:
            self.raiz = NodoArbol(nombre, derrotado_por)
        else:
            self._insertar(self.raiz, nombre, derrotado_por)

    def _insertar(self, nodo, nombre, derrotado_por):
        if nombre < nodo.nombre:
            if nodo.izquierdo is None:
                nodo.izquierdo = NodoArbol(nombre, derrotado_por)
            else:
                self._insertar(nodo.izquierdo, nombre, derrotado_por)
        else:
            if nodo.derecho is None:
                nodo.derecho = NodoArbol(nombre, derrotado_por)
            else:
                self._insertar(nodo.derecho, nombre, derrotado_por)

    def inorden(self, nodo):
        if nodo:
            self.inorden(nodo.izquierdo)
            print(f"Criatura: {nodo.nombre}, Derrotado por: {nodo.derrotado_por}, Capturada por: {nodo.capturada_por}")
            self.inorden(nodo.derecho)

    def agregar_descripcion(self, nombre, descripcion):
        nodo = self.buscar(self.raiz, nombre)
        if nodo:
            nodo.descripcion = descripcion

    def buscar(self, nodo, nombre):
        if nodo is None or nodo.nombre == nombre:
            return nodo
        if nombre < nodo.nombre:
            return self.buscar(nodo.izquierdo, nombre)
        return self.buscar(nodo.derecho, nombre)

    def mostrar_info(self, nombre):
        nodo = self.buscar(self.raiz, nombre)
        if nodo:
            print(f"Criatura: {nodo.nombre}, Derrotado por: {nodo.derrotado_por}, Capturada por: {nodo.capturada_por}, Descripcion: {nodo.descripcion}")
        else:
            print(f"{nombre} no encontrado")

    def contar_derrotas(self):
        derrotas = {}
        self._contar_derrotas(self.raiz, derrotas)
        return derrotas

    def _contar_derrotas(self, nodo, derrotas):
        if nodo:
            if nodo.derrotado_por:
                if nodo.derrotado_por in derrotas:
                    derrotas[nodo.derrotado_por] += 1
                else:
                    derrotas[nodo.derrotado_por] = 1
            self._contar_derrotas(nodo.izquierdo, derrotas)
            self._contar_derrotas(nodo.derecho, derrotas)

    def listar_criaturas_derrotadas_por(self, heroe):
        print(f"Criaturas derrotadas por {heroe}:")
        self._listar_criaturas_derrotadas_por(self.raiz, heroe)

    def _listar_criaturas_derrotadas_por(self, nodo, heroe):
        if nodo:
            self._listar_criaturas_derrotadas_por(nodo.izquierdo, heroe)
            if nodo.derrotado_por == heroe:
                print(nodo.nombre)
            self._listar_criaturas_derrotadas_por(nodo.derecho, heroe)

    def criaturas_no_derrotadas(self):
        print("Criaturas no derrotadas:")
        self._criaturas_no_derrotadas(self.raiz)

    def _criaturas_no_derrotadas(self, nodo):
        if nodo:
            self._criaturas_no_derrotadas(nodo.izquierdo)
            if nodo.derrotado_por is None:
                print(nodo.nombre)
            self._criaturas_no_derrotadas(nodo.derecho)

    def capturar(self, nombre, heroe):
        nodo = self.buscar(self.raiz, nombre)
        if nodo:
            nodo.capturada_por = heroe

    def eliminar(self, nombre):
        self.raiz = self._eliminar(self.raiz, nombre)

    def _eliminar(self, nodo, nombre):
        if nodo is None:
            return nodo
        if nombre < nodo.nombre:
            nodo.izquierdo = self._eliminar(nodo.izquierdo, nombre)
        elif nombre > nodo.nombre:
            nodo.derecho = self._eliminar(nodo.derecho, nombre)
        else:
            if nodo.izquierdo is None:
                return nodo.derecho
            elif nodo.derecho is None:
                return nodo.izquierdo
            temp = self._minimo_valor(nodo.derecho)
            nodo.nombre = temp.nombre
            nodo.derrotado_por = temp.derrotado_por
            nodo.derecho = self._eliminar(nodo.derecho, temp.nombre)
        return nodo

    def _minimo_valor(self, nodo):
        actual = nodo
        while actual.izquierdo:
            actual = actual.izquierdo
        return actual

    def modificar_nombre(self, nombre_antiguo, nombre_nuevo):
        nodo = self.buscar(self.raiz, nombre_antiguo)
        if nodo:
            nodo.nombre = nombre_nuevo
