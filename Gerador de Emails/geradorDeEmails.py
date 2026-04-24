from random import choice

def gerarEmail(tamanho=10 , tipoEmail="@gmail" , quantidadeEmails=1):
    
    caracs = "abcdefghijklmnopqrstuvwxyz"
    # nums = "1234567890"
    
    emails = list()
    if tipoEmail == "":
        tipoEmail = "@gmail"
    while len(emails) < quantidadeEmails:
        email = ""
        for carac in range(tamanho):
            email += choice(caracs)
        email = f"{email}{tipoEmail}.com"
        if email not in emails:
            emails.append(email)
    return emails

#============================================================================

quantidade = int(input("Quantos emails quer gerar? "))
tipo = input("Qual tipo de domínio?(ex: gmail) ")
if tipo == "":
    tipo = "@gmail"
tamanhoCarac = int(input("Quantos caracteres terá os emails? "))

confirmar = input(f"""Deseja alterar alguma escolha?
                [ 1 ] Alterar quantidadade de emails - Atual:{quantidade}
                [ 2 ] Alterar tipo de domínio - Atual:{tipo}
                [ 3 ] Alterar tamanho do email - Atual:{tamanhoCarac}
                [ 4 ] Concluir  """)
while confirmar != "4":
    if confirmar == "1":
        quantidade = int(input("Quantos emails quer gerar? "))
    elif confirmar == "2":
        tipo = input("Qual tipo de domínio?(padrao: gmail) ")
        if tipo == "":
            tipo = "@gmail"
    elif confirmar == "3":
        tamanhoCarac = int(input("Quantos caracteres terá os emails? "))
    else:
        print("Opção inválida, tente novamente")
    confirmar = input(f"""Deseja alterar alguma escolha?
                [ 1 ] Alterar quantidadade de emails - Atual:{quantidade}
                [ 2 ] Alterar tipo de domínio - Atual:{tipo}
                [ 3 ] Alterar tamanho do email - Atual:{tamanhoCarac}
                [ 4 ] Concluir  """)
    
print(gerarEmail(tamanho=tamanhoCarac ,quantidadeEmails=quantidade , tipoEmail=tipo))
    
