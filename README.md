Atividade Prática – Unidade 1
Conjuntos em Python

Disciplina: Lógica e Matemática Discreta
Turma de Férias

Professor: Rondineli Seba

Aluna: Kaline Maria Carvalho


## 1 Introdução

Esta atividade prática foi desenvolvida com o objetivo de aplicar, na linguagem Python, os conceitos fundamentais da Teoria dos Conjuntos estudados na disciplina de Lógica e Matemática Discreta.

A proposta consiste na manipulação de dois conjuntos:

Um conjunto definido pelo usuário (com 4 a 8 elementos);

Um conjunto gerado aleatoriamente pelo programa (também com 4 a 8 elementos).

A partir desses conjuntos, o programa realiza e exibe as principais operações da Teoria dos Conjuntos, reforçando a aplicação prática dos conceitos matemáticos abordados em sala.

## 2 Objetivos da Atividade
-> Objetivo Geral

Aplicar conceitos matemáticos da Teoria dos Conjuntos por meio de programação em Python.

-> Objetivos Específicos

Trabalhar com a estrutura de dados set da linguagem Python;

Implementar operações de conjuntos;

Validar entrada de dados;

Aplicar modularização do código;

Organizar o projeto seguindo boas práticas de programação.

## 3 Estrutura do Projeto

O projeto foi organizado em dois arquivos principais:

atividade-conjuntos-python
│
├── main.py
├── conjuntos.py
└── README.md

📌 main.py

Arquivo responsável por:

Executar o programa;

Chamar as funções do módulo conjuntos.py;

Exibir os resultados na tela.

Esse arquivo funciona como o ponto principal de controle da aplicação.

📌 conjuntos.py

Arquivo responsável por:

Implementar a leitura do conjunto do usuário;

Gerar o conjunto aleatório;

Realizar todas as operações de conjuntos;

Retornar os resultados para o arquivo principal.

Essa separação demonstra aplicação do princípio de modularização, melhorando organização, clareza e manutenção do código.

## 4 Funcionamento do Programa
4.1 Leitura do Conjunto do Usuário

A função ler_conjunto_usuario():

Solicita ao usuário que insira entre 4 e 8 números inteiros;

Converte a entrada para o tipo set;

Garante que o conjunto tenha tamanho válido;

Trata possíveis erros de digitação.

Trecho relevante:

elementos = set(map(int, entrada.split()))


Esse comando:

Divide a entrada digitada;

Converte cada valor para inteiro;

Armazena em um conjunto (eliminando elementos repetidos automaticamente).

4.2 Geração do Conjunto Aleatório

A função gerar_conjunto_aleatorio():

Define aleatoriamente o tamanho do conjunto entre 4 e 8 elementos;

Gera números aleatórios;

Garante que não existam repetições.

Trecho relevante:

while len(conjunto) < tamanho:
    numero = random.randint(1, 20)
    conjunto.add(numero)


O uso do tipo set garante a propriedade fundamental dos conjuntos: ausência de elementos repetidos.

4.3 Operações de Conjuntos Implementadas

A função operacoes_conjuntos(a, b) realiza as seguintes operações:

Operação Matemática	Implementação em Python
União (A ∪ B)	`a
Interseção (A ∩ B)	a & b
Diferença (A - B)	a - b
Diferença (B - A)	b - a
Diferença Simétrica (A Δ B)	a ^ b
Cardinalidade	len(conjunto)

Esses operadores da linguagem Python correspondem diretamente aos operadores matemáticos da Teoria dos Conjuntos.

## 5 Conceitos de Lógica e Matemática Discreta Aplicados

O programa aplica diretamente os seguintes conceitos:

Definição formal de conjunto;

Cardinalidade;

União;

Interseção;

Diferença;

Diferença Simétrica;

Conjuntos finitos;

Propriedades fundamentais dos conjuntos.

Além disso, reforça a representação computacional de estruturas matemáticas.

## 6 Como Executar o Programa

No terminal, dentro da pasta do projeto:

py main.py


O usuário deverá inserir entre 4 e 8 números inteiros separados por espaço.

Exemplo:

1 2 3 4


O programa exibirá:

Os dois conjuntos;

Todas as operações solicitadas;

As cardinalidades.

## 7 Considerações Finais

-A atividade cumpre integralmente os requisitos propostos, realizando corretamente todas as operações da Teoria dos Conjuntos.

-A organização modular do código demonstra aplicação de boas práticas de programação, além de estabelecer uma conexão clara entre conceitos matemáticos abstratos e sua implementação computacional.

-O projeto evidencia a aplicação prática dos conteúdos da disciplina de Lógica e Matemática Discreta.
