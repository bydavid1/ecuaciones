from src.lineales import cramer

def test_cramer():
    a = [
        [2, 1],
        [5, 7]
    ]
    b = [11, 13]
    
    solucion = cramer(a, b)
    
    # verificar
    assert solucion == [3.0, 1.0], f"Error: {solucion}"