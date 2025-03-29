from animal import Animal
from lista_enlazada import ListaEnlazada

def main():
    lista = ListaEnlazada()

    while True:
        nombre = input("Ingrese el nombre del animal: ")
        edad = int(input("Ingrese la edad del animal: "))
        tipo = input("Ingrese el tipo de animal: ")

        animal = Animal(nombre, edad, tipo)
        lista.agregar_animal(animal)

        continuar = input("¿Desea agregar otro animal? (s/n): ")
        if continuar.lower() != 's':
            break

    print("\nAnimales en la lista (iterativo):")
    lista.mostrar_animales_iterativo()

    print("\nAnimales en la lista (recursivo):")
    lista.mostrar_animales_recursivo()

    nombre_buscar = input("\nIngrese el nombre del animal que desea comprar: ")
    tipo_buscar = input("Ingrese el tipo del animal que desea comprar: ")
    animal_buscar = Animal(nombre_buscar, 0, tipo_buscar)  # La edad no importa para la búsqueda

    actual = lista.cabeza
    encontrado = False
    while actual is not None:
        if actual.animal == animal_buscar:
            encontrado = True
            break
        actual = actual.siguiente

    if encontrado:
        print("¡Sí, puedes comprar ese animal!")
    else:
        print("Lo siento, ese animal no está disponible.")

if __name__ == "__main__":
    main()