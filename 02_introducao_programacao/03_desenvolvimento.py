# Função que lista os andares e se for o 13º ele pula para o próximo
def describe_floors(build_size: int) -> None:
    for floor in range(build_size, 0, -1):
        if floor != 13:
            print(f"The floor is {floor}")

# Função principal
def main():
    # Chama a função que lista os andares
    describe_floors(20)

if __name__ == "__main__":
    main()