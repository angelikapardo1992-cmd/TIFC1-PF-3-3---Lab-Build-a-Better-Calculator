def addmultiplenumbers(numbers):
    """Suma todos los números en una lista"""
    return sum(numbers)


def multiplymultiplenumbers(numbers):
    """Multiplica todos los números en una lista"""
    result = 1
    for num in numbers:
        result *= num
    return result


def isiteven(num):
    """Devuelve True si el número es par y entero, False si no"""
    # Primero verificamos si es un número entero
    if not isinstance(num, int) or isinstance(num, bool):
        # Si es float, comprobamos si es un número completo
        if isinstance(num, float):
            if num % 1 != 0:  # Si tiene decimales
                return False
    # Ahora comprobamos si es par
    return num % 2 == 0


def isitaninteger(num):
    """Devuelve True si el número es un entero, False si no"""
    # Verificamos si es un int (pero no bool, que hereda de int en Python)
    if isinstance(num, bool):
        return False
    if isinstance(num, int):
        return True
    # Si es float, comprobamos si es un número entero (sin decimales)
    if isinstance(num, float):
        return num % 1 == 0
    return False


def main():
    print("Hello learners!")


if __name__ == "__main__":
    main()