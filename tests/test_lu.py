from src.lineales import lu

def test_lu():
    a = [
        [2, 1],
        [5, 7]
    ]
    b = [11, 13]

    solucion = lu(a, b)

    # verificar
    assert solucion == [3.0, 1.0], f"Error: {solucion}"