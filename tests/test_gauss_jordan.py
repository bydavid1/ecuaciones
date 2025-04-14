from src.lineales import gauss_jordan

def test_gauss_jordan():
    a = [
        [2, 1],
        [5, 7]
    ]
    b = [11, 13]
    
    solucion = gauss_jordan(a, b)
    
    # verificar
    assert solucion == [3.0, 1.0], f"Error: {solucion}"