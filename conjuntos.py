import random

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


def gerar_conjunto_aleatorio():
    tamanho = random.randint(4, 8)
    conjunto = set()

    while len(conjunto) < tamanho:
        numero = random.randint(1, 20)
        conjunto.add(numero)

    return conjunto


def operacoes_conjuntos(a, b):
    return {
        "uniao": a | b,
        "intersecao": a & b,
        "diferenca_a_b": a - b,
        "diferenca_b_a": b - a,
        "diferenca_simetrica": a ^ b,
        "cardinalidade_a": len(a),
        "cardinalidade_b": len(b)
    }
