import os
import json

caminho = input("Caminho: ")

pasta = os.listdir(caminho)

def pegarExtensoes(pasta):
    extensoes = set()
    for arq in pasta:
        # if os.path.isfile(arq):
            ext = os.path.splitext(arq)[1]
            extensoes.add(ext)
    return extensoes

def quantidadeArquivoPorExtensao(pasta):
    quantExt = dict()
    for ext in pegarExtensoes(pasta):
        contador = 0
        for arq in pasta:
            if os.path.splitext(arq)[1] == ext:
                contador += 1
                quantExt[ext] = contador
            
        contador = 0
    return json.dumps(quantExt , indent=4)

print(quantidadeArquivoPorExtensao(pasta))

# with open("pastas.txt" , 'w') as arq:
    