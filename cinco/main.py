from arbol_mcu import ArbolBinario
from funciones import (
    listar_villanos,
    listar_heroes_con_c,
    contar_superheroes,
    modificar_doctor_strange,
    listar_superheroes_descendente,
    generar_bosque,
    listar_nodos_ordenados,
    contar_nodos
)

def main():
    arbol = ArbolBinario()
    personajes = [
        ("Iron Man", True), ("Thanos", False), ("Captain America", True),
        ("Doctor Strange", True), ("Loki", False), ("Black Widow", True),
        ("Red Skull", False), ("Captain Marvel", True), ("Ultron", False)
    ]
    for nombre, es_heroe in personajes:
        arbol.insertar(nombre, es_heroe)
    
    print("Villanos ordenados alfabeticamente:")
    listar_villanos(arbol.raiz)
    
    print("\nSuperheroes que empiezan con 'C':")
    listar_heroes_con_c(arbol.raiz)
    
    total_superheroes = contar_superheroes(arbol.raiz)
    print(f"\nNumero total de superheroes: {total_superheroes}")
    
    modificar_doctor_strange(arbol.raiz, "Doctor Strange", "Dr. Strange")
    
    print("\nVerificando modificacion de 'Doctor Strange':")
    listar_nodos_ordenados(arbol.raiz)
    
    print("\nSuperheroes ordenados de manera descendente:")
    listar_superheroes_descendente(arbol.raiz)
    
    arbol_heroes = ArbolBinario()
    arbol_villanos = ArbolBinario()
    generar_bosque(arbol.raiz, arbol_heroes, arbol_villanos)
    
    total_heroes = contar_superheroes(arbol_heroes.raiz)
    total_villanos = contar_nodos(arbol_villanos.raiz)
    
    print(f"\nNumero total de superheroes en el arbol de heroes: {total_heroes}")
    print(f"Numero total de villanos en el arbol de villanos: {total_villanos}")
    
    print("\nBarrido ordenado alfabeticamente del arbol de superheroes:")
    listar_nodos_ordenados(arbol_heroes.raiz)
    
    print("\nBarrido ordenado alfabeticamente del arbol de villanos:")
    listar_nodos_ordenados(arbol_villanos.raiz)

if __name__ == "__main__":
    main()
