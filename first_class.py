#Selecciona variable de numero  utilizar

numeros = list()
continuar: bool = True
#Agregar titulo

print('Lista')


#Agregar Numero

def agregar (numero : int ) : 

    numeros.append(numero)


#Eliminar Numero

def eliminar (numero : int) -> None:

    numero.pop()


#Llamar agregar o eliminar numero

while continuar:
    print("Seleccie una opcion")
    print("Inserte 1 para agregar")
    print("Inserte 2 para eliminar")
    print("Inserte 3 para salir")

    opcion = int(input())

    if opcion == 1:
        numero = int(input("Ingrese un numero: "))
        agregar(numero)
        print(numeros)
    elif opcion == 2:
        numero = int(input("Ingrese un numero:"))
        eliminar(numero)
        print(numeros)
    elif opcion == 3:
        continuar = False
        print("Espero ayudarlo en otra ocacion")
    else:
        print("Opcion no disponible")
        continuar = False
        print("Espero ayudarlo pronto")
