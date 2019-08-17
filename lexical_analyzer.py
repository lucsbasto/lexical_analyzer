import json

input = open('arquivo.txt', 'r')
linha = input.read()
token = ""
palavraReservadas = ['while', 'do']
operadores = ['<', '=', '+']
terminador = [';']
identificadores = ['i','j']
tokens = []
simbolos = []
erros = []
indice = 1
for i in range(len(linha)):
    if(linha[i] is not " "):
        token += linha[i]
    elif(linha[i] is " "):
        if(token in palavraReservadas):
            tokens.append({
                "token": token,
                "identificacao": "palavra reservada",
                "tamanho": len(token),
                "posicao": ('({},{})'.format(0, i - len(token)))
            })
            token = ""

        elif(token in operadores):
            tokens.append({
                "token": token,
                "identificacao": "operador",
                "tamanho": len(token),
                "posicao": ("({},{})".format(0, i - len(token)))
            })
            token = ""

        elif(token in identificadores):
            simbolos.append({
                "indice": indice,
                "simbolo": ("({})".format(token))
            })
            tokens.append({
                "token": token,
                "identificacao": "identificador",
                "tamanho": len(token),
                "posicao": ("({},{})".format(0, i - len(token)))
            })
            token = ""
            indice+=1
        elif (token.isdigit() and len(token) == 1):
            simbolos.append({
                "indice": indice,
                "simbolo": ("({})".format(token))
            })
            tokens.append({
                "token": token,
                "identificacao": "numero",
                "tamanho": len(token),
                "posicao": ("({},{})".format(0, i - len(token)))
            })
            token = ""
            indice+=1
        elif (token.isdigit() and len(token) > 1):
            simbolos.append({
                "indice": indice,
                "simbolo": ("({})".format(token))
            })
            tokens.append({
                "token": token,
                "identificacao": "constante",
                "tamanho": len(token),
                "posicao": ("({},{})".format(0, i - len(token)))
            })
            token = ""
            indice+=1
        else:
            erros.append({
                "token": token,
                "posicao": ("({},{})".format(0, i - len(token)))
            })
        token = ""

    elif(token in terminador):
        tokens.append({
            "token": token,
            "identificacao": "terminador",
            "tamanho": len(token),
            "posicao": ("({},{})".format(0, i - len(token)))
        })
        token = ""

input.close()

with open('output.txt', 'w+') as output:
    output.write("token: {\n")
    for i in tokens:
        ij = json.dumps(i)
        output.write(ij+",\n")
    output.write("}\n")

    output.write("erros: {\n")
    for i in erros:
        ij = json.dumps(i)
        output.write(ij + ",\n")
    output.write("}\n")

    output.write("simbolos: {\n")
    for i in simbolos:
        ij = json.dumps(i)
        output.write(ij + ",\n")
    output.write("}")

output.close()
