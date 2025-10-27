def add(a: float, b: float) -> float:
    return a + b

def sub(a: float, b: float) -> float:
    return a - b

def mul(a: float, b: float) -> float:
    return a * b

def div(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

def pow_(a: float, b: float) -> float:
    return a ** b

def safe_mod(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Modulo by zero is not allowed")
    return a % b
