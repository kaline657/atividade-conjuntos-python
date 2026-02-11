from conjuntos import ler_conjunto_usuario, gerar_conjunto_aleatorio

def main():
    print("Programa de Operações com Conjuntos")

    conjunto_usuario = ler_conjunto_usuario()
    conjunto_aleatorio = gerar_conjunto_aleatorio()

    print("\nConjunto digitado:", conjunto_usuario)
    print("Conjunto aleatório:", conjunto_aleatorio)

if __name__ == "__main__":
    main()
