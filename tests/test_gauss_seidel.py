from src.lineales import gauss_seidel

def test_gauss_seidel():
    a = [
        [2, 1],
        [5, 7]
    ]
    b = [11, 13]

    solucion = gauss_seidel(a, b)

    # verificar
    assert solucion == [3.0, 1.0], f"Error: {solucion}"