# lexical_analyzer

Trabalho desenvolvido na disciplina de Compiladores do CEULP/ULBRA ministrada pelo MSc. Jackson Gomes De Souza com objetivo de desenvolver um analisador léxico que analise e reconheça lexemas de uma determinada linguagem de programação.

Características importantes do scanner:
* a entrada é um arquivo texto (qualquer nome e qualquer extensão)
* o scanner pode ser implementado em qualquer linguagem/plataforma
* a saída do scanner deve ser um arquivo JSON, contendo a tabela de tokens, a tabela de símbolos e um possível erro encontrado durante a análise

A tabela de ***tokens*** deve armazenar: o *token*, sua identificação, tamanho e a posição (linha e coluna).

A tabela de **símbolos** deve armazenar o índice e o símbolo.

O **erro** deve ter: uma mensagem textual, o *token* e a posição (linha e coluna).

No caso de haver **erro**, a saída do scanner deve ter *tokens* e **símbolos** até a existência do **erro**.

# Documentação
## Processo de Criação do Parser

* Definição da tabela de tokens
    * Palavras Reservadas
    * Operadores
    * Terminadores
    * Numeros
    * Identificadores
    ### Implementação
    ```python
   palavraReservadas = ['while', 'do']
   operadores = ['<', '=', '+']
   terminador = [';']
   numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
   identificadores = ['i','j']
    ```
* Leitura do arquivo que contém o texto
```python
   input = open('arquivo.txt', 'r')
   linha = input.read()
```
* Percorrendo o arquivo que contem o texto verificando se o token é uma:
    * palavra reservada
        * o token precisa estar presente na lista de palavras reservadas
    * operador
        * o token precisa estar presente na lista de operadores
    * identificador
        * o token precisa estar presente na lista de identificadores
    * digito
        * o token precisa ser do tipo numérico e ter o tamanho igual a 1
    * constante
        * o token precisa ser do tipo numerico e ter o tamanho maior que 1

##  Estrutura do parser e como ele funciona 

Este parser foi estruturado com uma variável e um laço de repetição para analisar os dados adicionados em um arquivo.  A repetição é feita em cada elemento da variavel *linha*, que contém o conteúdo do arquivo, e a variavel, que na implementação está nomeada como *token*, concatena o valor dela com o valor desse elemento. A cada passo é feito uma verificação para descobrir se o token formado pelos elementos presentes na variável *token* é um token da linguagem e identificando esses tokens com base nas listas de palavraReservadas, operadores e identificadores definidas previamente.

```python
if (token in palavraReservadas):
    tokens.append({
        "token": token,
        "identificacao": "palavra reservada",
        "tamanho": len(token),
        "posicao": ('({},{})'.format(0, i - len(token)))
    })
```


### Tabela de tokens execução sem erros
* Entrada 
```
while i < 100 do i = i + j;
```

| token | identificação     | tamanho | Posição (*linha, coluna*) |
|-------|-------------------|---------|---------------------------|
| while | palavra reservada | 5       | (0,0)                     |
| i     | identificador     | 1       | (0,6)                     |
| <     | operador          | 1       | (0,8)                     |
| 100   | constante         | 3       | (0,10)                    |
| do    | palavra reservada | 2       | (0,14)                    |
| i     | identificador     | 1       | (0,17)                    |
| =     | operador          | 1       | (0,19)                    |
| i     | identificador     | 1       | (0,21)                    |
| +     | operador          | 1       | (0,23)                    |
| j     | identificador     | 1       | (0,25)                    |
| ;     | terminador        | 1       | (0,26)                    |


### Tabela de símbolos

|indice|simbolo|
|------|-------|
|1     |(i)    |
|2     |(100)  |
|3     |(i)    |
|4     |(i)    |

### Tabela de erros 

|token|posicao|
|-----|-------|
|     |       |

### Tablea de tokens execução com erro
* Entrada 
```
while i < 100 do i = i + for;
```

| token | identificação     | tamanho | Posição (*linha, coluna*) |
|-------|-------------------|---------|---------------------------|
| while | palavra reservada | 5       | (0,0)                     |
| i     | identificador     | 1       | (0,6)                     |
| <     | operador          | 1       | (0,8)                     |
| 100   | constante         | 3       | (0,10)                    |
| do    | palavra reservada | 2       | (0,14)                    |
| i     | identificador     | 1       | (0,17)                    |
| =     | operador          | 1       | (0,19)                    |
| i     | identificador     | 1       | (0,21)                    |
| +     | operador          | 1       | (0,23)                    |


### Tabela de símbolos

|indice|simbolo|
|------|-------|
|1     |(i)    |
|2     |(100)  |
|3     |(i)    |
|4     |(i)    |

### Tabela de erros 

|token|posicao|
|-----|-------|
| for | (0,25) |
