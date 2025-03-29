class Nodo:
    def __init__(self, animal):
        self.animal = animal
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_animal(self, animal):
        if self.cabeza is None:
            self.cabeza = Nodo(animal)
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                if actual.animal == animal:
                    print("El animal ya está en la lista.")
                    return
                actual = actual.siguiente
            if actual.animal == animal:
                print("El animal ya está en la lista.")
                return
            actual.siguiente = Nodo(animal)

    def mostrar_animales_iterativo(self):
        actual = self.cabeza
        while actual is not None:
            print(f"Nombre: {actual.animal.get_nombre()}, Edad: {actual.animal.get_edad()}, Tipo: {actual.animal.get_tipo()}")
            actual = actual.siguiente

    def mostrar_animales_recursivo(self):
        self._mostrar_animales_recursivo(self.cabeza)

    def _mostrar_animales_recursivo(self, nodo):
        if nodo is not None:
            print(f"Nombre: {nodo.animal.get_nombre()}, Edad: {nodo.animal.get_edad()}, Tipo: {nodo.animal.get_tipo()}")
            self._mostrar_animales_recursivo(nodo.siguiente)