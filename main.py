def suma(x: int, y: int):
    return x + y

def resta(x: int, y: int):
    return x - y

def multiplicacion(x: int, y: int):
    return x * y

def division(x: int, y: int):
    try:
        return x / y
    except ZeroDivisionError:
        print("No se puede divir entre 0")
