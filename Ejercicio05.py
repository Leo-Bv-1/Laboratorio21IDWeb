class OperadorInvalidoError(Exception):
    def __init__(self, operador):
        super().__init__(f"Operador inválido: '{operador}'. Usa + - * /")

def calcular(operacion):
    try:
        partes = operacion.split()

        if len(partes) != 3:
            raise ValueError("Formato incorrecto. Usa: numero operador numero")

        num1_str, operador, num2_str = partes

        num1 = float(num1_str)
        num2 = float(num2_str)

        if operador not in ['+', '-', '*', '/']:
            raise OperadorInvalidoError(operador)

        if operador == '+':
            return num1 + num2
        elif operador == '-':
            return num1 - num2
        elif operador == '*':
            return num1 * num2
        elif operador == '/':
            if num2 == 0:
                raise ZeroDivisionError("No se puede dividir entre cero")
            return num1 / num2

    except ZeroDivisionError:
        print("Error: División entre cero no permitida.")
    except ValueError as e:
        print(f"Error de valor: {e}")
    except OperadorInvalidoError as e:
        print(f"{e}")
print(calcular("10 / 2"))
print(calcular("5 * 3"))
print(calcular("8 / 0"))
print(calcular("a + 3"))
print(calcular("10 x 2"))
print(calcular("10+2"))