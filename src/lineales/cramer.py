def determinante(matriz):
    n = len(matriz)
    if n == 1:
        return matriz[0][0]
    if n == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]

    det = 0
    for j in range(n):
        submatriz = [fila[:j] + fila[j+1:] for fila in matriz[1:]]
        signo = (-1) ** j
        det += signo * matriz[0][j] * determinante(submatriz)
    return det

def cramer(a, b):
    """
    Resuelve un sistema de ecuaciones lineales usando la Regla de Cramer.
    a: matriz de coeficientes
    b: vector de términos independientes
    """
    n = len(a)
    det_a = determinante(a)
    if det_a == 0:
        raise ValueError("El sistema no tiene solución única.")

    soluciones = []
    for i in range(n):
        matriz_i = [fila[:] for fila in a]
        for j in range(n):
            matriz_i[j][i] = b[j]
        det_i = determinante(matriz_i)
        soluciones.append(det_i / det_a)

    return soluciones