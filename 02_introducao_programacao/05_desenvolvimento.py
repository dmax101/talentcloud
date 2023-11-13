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
            print(f"Erro: {e}")
            return 0
    else:
        return 0


def calcView():
    while True:
        print("\nOperações disponíveis:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        opcao = input("Escolha uma operação (0-4): ")
        operation = ""

        if opcao == "0":
            print("Saindo da calculadora. Até logo!")
            break
        elif opcao == "1":
            operation = "+"
        elif opcao == "2":
            operation = "-"
        elif opcao == "3":
            operation = "*"
        elif opcao == "4":
            operation = "/"
        else:
            print("Essa opção não existe. Tente novamente.")
            continue

        try:
            num1 = float(input("Digite o primeiro valor: "))
            num2 = float(input("Digite o segundo valor: "))
        except ValueError:
            print("Valores inválidos. Tente novamente.")
            continue

        

        print(f"{num1} {operation} {num2} = {calculadora(num1, num2, operation)}")


def main():
    calcView()


if __name__ == "__main__":
    main()
