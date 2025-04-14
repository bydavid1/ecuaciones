from src.lineales import jacobi

def test_jacobi():
    a = [
        [2, 1],
        [5, 7]
    ]
    b = [11, 13]
    
    solucion = jacobi(a, b)
    
    # verificar
    assert solucion == [3.0, 1.0], f"Error: {solucion}"