def gauss_seidel(a, b, tolerancia=1e-10, max_iter=100):
    n = len(a)
    x = [0.0 for _ in range(n)]  # Valor inicial

    for _ in range(max_iter):
        x_nuevo = x.copy()
        for i in range(n):
            suma1 = sum(a[i][j] * x_nuevo[j] for j in range(i))       # ya actualizados
            suma2 = sum(a[i][j] * x[j] for j in range(i + 1, n))      # aún no actualizados
            x_nuevo[i] = (b[i] - (suma1 + suma2)) / a[i][i]

        # Verificar convergencia
        if all(abs(x_nuevo[i] - x[i]) < tolerancia for i in range(n)):
            return x_nuevo

        x = x_nuevo

    raise Exception("El metodo no convergio")
