
#1. Fibonacci
def fibonacci(n, a=0, b=1, serie=None):
    if serie is None:
        serie = [a]
    if n == 1:
        return serie
    serie.append(b)
    return fibonacci(n - 1, b, a + b, serie)
print(fibonacci(10))

#Sumar elementos de un arreglo
def suma_elementos(lista, n):
    if n == 0:
        return 0
    return lista[n - 1] + suma_elementos(lista, n - 1)
print(suma_elementos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))

#Realizar multiplicacion a base de sumas
def multiplicacion(a, b):
    if b == 1:
        return a
    print(f"{a} + {b-1}")
    return a + multiplicacion(a, b - 1)
print(multiplicacion(8, 5))

#realizar division a base de restas
def division(a, b):
    if a < b:
        return 0
    print(f"{a} + {b-1}")
    return 1 + division(a - b, b)
print(division(10, 2))


