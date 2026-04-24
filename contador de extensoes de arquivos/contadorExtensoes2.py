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
    extensoes = pegarExtensoes(pasta)

    for arq in pasta:
        if os.path.splitext(arq)[1] in extensoes:
            contador += 1
            quantExt[os.path.splitext()[1]] = 0 #sei la
            
    return json.dumps(quantExt , indent=4)

print(quantidadeArquivoPorExtensao(pasta))

# with open("pastas.txt" , 'w') as arq:
    