import matplotlib.pyplot as plt
import sympy as sp

# Función para dibujar la cuerda con la masa
def dibujar_cuerda_masa(masa):
    fig, ax = plt.subplots()
    ax.plot([0, 0], [0, -1], 'k-', lw=2)  # Dibuja la cuerda
    ax.plot(0, -1, 'ro', markersize=20)  # Dibuja la masa
    ax.text(0.1, -1, f'Masa: {masa} kg', fontsize=12, verticalalignment='center')
    ax.set_xlim(-1, 1)
    ax.set_ylim(-2, 1)
    ax.set_aspect('equal')
    plt.title('Cuerda con Masa')
    plt.show()

# Función para calcular la fricción y comprobar la segunda ley de Newton
def calcular_friccion_y_segunda_ley(masa, coef_friccion):
    g = 9.81  # Aceleración debida a la gravedad en m/s^2
    T = sp.Symbol('T')  # Tensión en la cuerda
    F_friccion = coef_friccion * masa * g  # Fuerza de fricción
    F_net = masa * g - F_friccion  # Fuerza neta
    eq = sp.Eq(T, F_net)  # Segunda ley de Newton: T = F_net
    tension = sp.solve(eq, T)[0]
    return F_friccion, tension

# Solicitar al usuario el peso de la masa y el coeficiente de fricción
masa = float(input("Introduce el peso de la masa en kg: "))
coef_friccion = float(input("Introduce el coeficiente de fricción: "))

# Dibujar la cuerda con la masa
dibujar_cuerda_masa(masa)

# Calcular la fricción y la tensión en la cuerda
friccion, tension = calcular_friccion_y_segunda_ley(masa, coef_friccion)

# Mostrar los resultados
print(f"Fuerza de fricción: {friccion:.2f} N")
print(f"Tensión en la cuerda: {tension:.2f} N")
