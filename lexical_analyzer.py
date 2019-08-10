import json

input = open('arquivo.txt', 'r')
linha = input.read()
token = ""
palavraReservadas = ['while', 'do']
operadores = ['<', '=', '+']
terminador = [';']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
identificadores = ['i','j']
tokens = []

for i in range(len(linha)):
    if(linha[i] is not " "):
        token += linha[i]
    if(linha[i] is " "):
        if(token in palavraReservadas):
            tokens.append({
                "token": token,
                "identificacao": "palavra reservada",
                "tamanho": len(token),
                "posicao": ('({},{})'.format(0, i - len(token)))
            })
            token = ""

        if(token in operadores):
            tokens.append({
                "token": token,
                "identificacao": "operador",
                "tamanho": len(token),
                "posicao": ("({},{})".format(0, i - len(token)))
            })
            token = ""

        if(token in identificadores):
            tokens.append({
                "token": token,
                "identificacao": "identificador",
                "tamanho": len(token),
                "posicao": ("({},{})".format(0, i - len(token)))
            })
            token = ""

        if (token.isdigit() and len(token) == 1):
            tokens.append({
                "token": token,
                "identificacao": "numero",
                "tamanho": len(token),
                "posicao": ("({},{})".format(0, i - len(token)))
            })
            token = ""

        if (token.isdigit() and len(token) > 1):
            tokens.append({
                "token": token,
                "identificacao": "constante",
                "tamanho": len(token),
                "posicao": ("({},{})".format(0, i - len(token)))
            })
            token = ""
        token = ""

    if(token in terminador):
        tokens.append({
            "token": token,
            "identificacao": "terminador",
            "tamanho": len(token),
            "posicao": ("({},{})".format(0, i - len(token)))
        })
        token = ""
input.close()

with open('output.txt', 'w+') as output:
    for i in tokens:
        ij = json.dumps(i)
        output.write(ij+",\n")
        print(i)
output.close()

