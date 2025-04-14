from src.lineales import gauss_elimination

def test_gauss_elimination():
    a = [
        [2, 1],
        [5, 7]
    ]
    b = [11, 13]
    
    solucion = gauss_elimination(a, b)
    
    # verificar
    assert solucion == [3.0, 1.0], f"Error: {solucion}"