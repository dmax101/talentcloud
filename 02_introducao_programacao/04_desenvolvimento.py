def calculadora(num1: float, num2: float, op: str):
    """
    Realiza operações aritméticas básicas com dois números.

    Parâmetros:
    - num1 (float): O primeiro operando.
    - num2 (float): O segundo operando.
    - op (str): A operação a ser realizada. Pode ser '+', '-', '*', ou '/'.

    Retorna:
    - float: O resultado da operação aritmética.
    - str: Em caso de divisão por zero.
    """
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        try:
            return num1 / num2
        except ZeroDivisionError as e:
            return f"Erro: {e}"

def main():
    """
    Exemplo de uso da função calculadora.

    Imprime os resultados de adição, subtração, multiplicação e divisão
    de dois números.
    """
    num1 = 15.5
    num2 = 0

    print(f"{num1} + {num2} = {calculadora(num1, num2, '+')}")
    print(f"{num1} - {num2} = {calculadora(num1, num2, '-')}")
    print(f"{num1} * {num2} = {calculadora(num1, num2, '*')}")
    print(f"{num1} / {num2} = {calculadora(num1, num2, '/')}")

if __name__ == "__main__":
    main()
