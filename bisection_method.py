import numpy as np
import matplotlib.pyplot as plt
import math

def f(x):
    return x**3 + 2*x - 13

def bisection(a, b, tolerance):
    xl = a # Límite izquierdo
    xr = b # Límite derecho
    i = 0
    if f(xl)*f(xr) < 0:
        while (np.abs(xl-xr) >= tolerance):
            i += 1
            c = (xl + xr) / 2.0
            product = f(xl)*f(c)
            if product > tolerance:
                xl = c
            else:
                if product < tolerance:
                    xr = c
        return c, i
    else:
        print("Los límites son incorrectos")

answer = bisection(-5, 5, 1e-5)
print(f"El método de la bisección me da una raíz x = {answer[0]} con {answer[1]} iteraciones")

## Confirmación con gráfico
x = np.linspace(-5, 5, 100)
plt.plot(x, f(x))
plt.plot(answer[0], f(answer[0]), "or")
plt.grid()
plt.show()