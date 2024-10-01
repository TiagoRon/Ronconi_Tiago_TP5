def listar_villanos(nodo):
    if nodo:
        listar_villanos(nodo.izquierdo)
        if not nodo.es_heroe:
            print(nodo.nombre)
        listar_villanos(nodo.derecho)

def listar_heroes_con_c(nodo):
    if nodo:
        listar_heroes_con_c(nodo.izquierdo)
        if nodo.es_heroe and nodo.nombre.startswith('C'):
            print(nodo.nombre)
        listar_heroes_con_c(nodo.derecho)

def contar_superheroes(nodo):
    if nodo is None:
        return 0
    else:
        count = 1 if nodo.es_heroe else 0
        return count + contar_superheroes(nodo.izquierdo) + contar_superheroes(nodo.derecho)

def modificar_doctor_strange(nodo, nombre_incorrecto, nombre_correcto):
    if nodo is None:
        return
    if nombre_incorrecto in nodo.nombre:
        print(f"Modificando {nodo.nombre} a {nombre_correcto}")
        nodo.nombre = nombre_correcto
    modificar_doctor_strange(nodo.izquierdo, nombre_incorrecto, nombre_correcto)
    modificar_doctor_strange(nodo.derecho, nombre_incorrecto, nombre_correcto)

def listar_superheroes_descendente(nodo):
    if nodo:
        listar_superheroes_descendente(nodo.derecho)
        if nodo.es_heroe:
            print(nodo.nombre)
        listar_superheroes_descendente(nodo.izquierdo)

def generar_bosque(nodo, arbol_heroes, arbol_villanos):
    if nodo:
        if nodo.es_heroe:
            arbol_heroes.insertar(nodo.nombre, nodo.es_heroe)
        else:
            arbol_villanos.insertar(nodo.nombre, nodo.es_heroe)
        generar_bosque(nodo.izquierdo, arbol_heroes, arbol_villanos)
        generar_bosque(nodo.derecho, arbol_heroes, arbol_villanos)

def listar_nodos_ordenados(nodo):
    if nodo:
        listar_nodos_ordenados(nodo.izquierdo)
        print(nodo.nombre)
        listar_nodos_ordenados(nodo.derecho)

def contar_nodos(nodo):
    if nodo is None:
        return 0
    else:
        return 1 + contar_nodos(nodo.izquierdo) + contar_nodos(nodo.derecho)
