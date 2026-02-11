from conjuntos import (
    ler_conjunto_usuario,
    gerar_conjunto_aleatorio,
    operacoes_conjuntos
)

def main():
    print("Programa de Operações com Conjuntos")

    conjunto_usuario = ler_conjunto_usuario()
    conjunto_aleatorio = gerar_conjunto_aleatorio()

    print("\nConjunto digitado:", conjunto_usuario)
    print("Conjunto aleatório:", conjunto_aleatorio)

    resultados = operacoes_conjuntos(conjunto_usuario, conjunto_aleatorio)

    print("\n--- Operações ---")
    print("União:", resultados["uniao"])
    print("Interseção:", resultados["intersecao"])
    print("Diferença A - B:", resultados["diferenca_a_b"])
    print("Diferença B - A:", resultados["diferenca_b_a"])
    print("Diferença Simétrica:", resultados["diferenca_simetrica"])
    print("Cardinalidade A:", resultados["cardinalidade_a"])
    print("Cardinalidade B:", resultados["cardinalidade_b"])

if __name__ == "__main__":
    main()
