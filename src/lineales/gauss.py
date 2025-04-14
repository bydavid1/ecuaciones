
def gauss_elimination(a, b):
    """
    Resuelve un sistema de ecuaciones lineales usando el método de eliminación de Gauss.
    a: matriz de coeficientes
    b: vector de términos independientes
    """
    n = len(b)
    for i in range(n):
        # Pivoteo
        max_row = max(range(i, n), key=lambda r: abs(a[r][i]))
        if i != max_row:
            a[i], a[max_row] = a[max_row], a[i]
            b[i], b[max_row] = b[max_row], b[i]

        # Eliminación
        for j in range(i + 1, n):
            factor = a[j][i] / a[i][i]
            for k in range(i, n):
                a[j][k] -= factor * a[i][k]
            b[j] -= factor * b[i]

    # Sustitución hacia atrás
    x = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - sum(a[i][j] * x[j] for j in range(i + 1, n))) / a[i][i]
    return x
