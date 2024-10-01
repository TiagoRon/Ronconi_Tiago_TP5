from veintitres.arbol_criaturas import ArbolBinario

def main():
    arbol = ArbolBinario()

    criaturas = [
        ("Ceto", None), ("Tifon", "Zeus"), ("Equidna", "Argos Panoptes"),
        ("Dino", None), ("Pefredo", None), ("Enio", None),
        ("Escila", None), ("Caribdis", None), ("Euriale", None),
        ("Esteno", None), ("Medusa", "Perseo"), ("Ladon", "Heracles"),
        ("Aguila del Caucaso", None), ("Quimera", "Belerofonte"),
        ("Hidra de Lerna", "Heracles"), ("Leon de Nemea", "Heracles"),
        ("Esfinge", "Edipo"), ("Dragon de la Colquida", None),
        ("Cerbero", None), ("Toro de Creta", "Teseo"),
        ("Jabali de Erimanto", None), ("Gerion", "Heracles"),
        ("Ortro", "Heracles"), ("Minotauro de Creta", "Teseo"),
        ("Harpias", None), ("Talos", "Medea"), ("Aves del Estinfalo", None),
        ("Sirenas", None), ("Basilisco", None), ("Piton", "Apolo"),
        ("Cierva de Cerinea", None)
    ]

    for criatura, derrotado_por in criaturas:
        arbol.insertar(criatura, derrotado_por)

    print("Listado inorden de criaturas y sus derrotadores:")
    arbol.inorden(arbol.raiz)

    arbol.agregar_descripcion("Talos", "Gigante de bronce que protegia a Creta")
    arbol.mostrar_info("Talos")

    print("\nTop 3 heroes o dioses con mas criaturas derrotadas:")
    derrotas = arbol.contar_derrotas()
    top_derrotadores = sorted(derrotas.items(), key=lambda x: x[1], reverse=True)[:3]
    for heroe, cantidad in top_derrotadores:
        print(f"{heroe}: {cantidad} criaturas")

    arbol.listar_criaturas_derrotadas_por("Heracles")

    arbol.criaturas_no_derrotadas()

    arbol.capturar("Cerbero", "Heracles")
    arbol.capturar("Toro de Creta", "Heracles")
    arbol.capturar("Cierva de Cerinea", "Heracles")
    arbol.capturar("Jabali de Erimanto", "Heracles")

    arbol.eliminar("Basilisco")
    arbol.eliminar("Sirenas")

    arbol.modificar_nombre("Ladon", "Dragon Ladon")

    print("\nListado inorden modificado:")
    arbol.inorden(arbol.raiz)

if __name__ == "__main__":
    main()
