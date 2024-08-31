"""Sample calculator module to be tested"""


def add(x: int | float, y: int | float) -> int | float:
    """Adds y to x"""
    return x + y


def sub(x: int | float, y: int | float) -> int | float:
    """Subtracts y from x"""
    return x - y


def mul(x: int | float, y: int | float) -> int | float:
    """Multiplies x with y"""
    return x * y


def div(x: int | float, y: int | float) -> int | float:
    """Divides x by y"""
    return x / y


if __name__ == "__main__":
    ...
