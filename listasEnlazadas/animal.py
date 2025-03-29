class Animal:
    def __init__(self, nombre, edad, tipo):
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_edad(self):
        return self.edad

    def set_edad(self, edad):
        self.edad = edad

    def get_tipo(self):
        return self.tipo

    def set_tipo(self, tipo):
        self.tipo = tipo

    def __eq__(self, other):
        if isinstance(other, Animal):
            return self.nombre == other.nombre and self.tipo == other.tipo
        return False

    def __hash__(self):
        return hash((self.nombre, self.tipo))