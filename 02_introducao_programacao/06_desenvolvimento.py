#Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
#A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).
#
#Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.
#
#Trabalhe esse código em seu IDE, suba ele para sua conta no GitHub e compartilhe o link desse projeto no campo ao lado para que outros desenvolvedores possam analisá-lo.

def valida_nome(nome):
    if not nome.strip():
        return False
    return True

def valida_aniversario(ano_aniver):
    if not ano_aniver.isdigit():
        return False
    ano_aniver = int(ano_aniver)
    if ano_aniver < 1922 or ano_aniver > 2021:
        return False
    return True

def main():
    nome = input("Digite seu nome completo: ")
    while not valida_nome(nome):
        print("Erro: Nome inválido.")
        nome = input("Digite seu nome completo: ")

    ano_aniver = input("Digite o ano de nascimento (entre 1922 e 2021): ")
    while not valida_aniversario(ano_aniver):
        print("Erro: Ano de nascimento inválido.")
        ano_aniver = input("Digite o ano de nascimento (entre 1922 e 2021): ")

    idade = 2022 - int(ano_aniver)
    print(f"Nome do usuário: {nome}")
    print(f"Idade que completou ou completará no ano atual: {idade}")

if __name__ == "__main__":
    main()