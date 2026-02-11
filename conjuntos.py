def ler_conjunto_usuario():
    while True:
        try:
            entrada = input("Digite entre 4 e 8 números separados por espaço: ")
            elementos = set(map(int, entrada.split()))

            if 4 <= len(elementos) <= 8:
                return elementos
            else:
                print("O conjunto deve ter entre 4 e 8 elementos únicos.")
        except ValueError:
            print("Digite apenas números inteiros.")
