persona = dict()
continuar: bool = True

def agregar_valor (clave:str, valor:str) -> None:
    persona.update({clave:valor})

agregar_valor('Nombre', 'Juan')
print (persona)

def eliminar_valor (clave:str) -> None:
    persona.pop(clave)
    print(persona)
    

while continuar:
    print("Seleccie una opcion")
    print("Inserte 1 para agregar")
    print("Inserte 2 para eliminar")
    print("Inserte 3 para salir")

    opcion = int(input())

    if opcion == 1:
        clave = input("ingrese una clave:")
        valor = input("ingrese un valor:")
        agregar_valor(clave, valor)
        print(persona)
    elif opcion == 2:
        clave = input("ingrese una clave:")
        eliminar_valor(clave)
        print(persona)
    elif opcion == 3:
        continuar = False
        print("Espero ayudarlo en otra ocacion")
    else:
        print ("Opcion no disponible")
        continuar = False
        print("Espero ayudarlo pronto")

