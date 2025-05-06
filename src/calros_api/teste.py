"""O arquivo teste.py é lindo.

Um arquivo lindo e bonito, cheio de charme.
"""

import os


def add(a: float, b: float) -> float:
    """Essa função soma A e B.

    Args:
        a (float): um número
        b (float): um número

    Returns:
        float: A soma dos números
    """
    return a + b


def mult(x, y):
    """Essa função multiplica A e B.

    Args:
        a (float): um número
        b (float): um número

    Returns:
        float: A soma dos números
    """
    return x * y


def main():
    """Essa função é demais."""
    x = 1
    y = 2
    z = add(x, y)
    print(os.getcwd())
    print("Soma:", z)
    print("Multiplicação:", mult(x, y))
    z = (
        x
        + 2
        + y * 3
        + x
        + 2
        + y * 3
        + x
        + 2
        + y * 3
        + x
        + 2
        + y * 3
        + x
        + 2
        + y * 3
        + x
        + 2
        + y * 3
        + x
        + 2
        + y * 3
    )


if __name__ == "__main__":
    main()
