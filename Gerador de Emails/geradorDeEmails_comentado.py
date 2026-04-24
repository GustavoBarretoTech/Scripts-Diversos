from random import choice

# Função principal para gerar emails aleatórios
# Parâmetros:
# - tamanho: comprimento da parte do usuário do email (padrão: 10 caracteres)
# - tipoEmail: provedor do email como "@gmail" (padrão: "@gmail")
# - quantidadeEmails: número de emails únicos a gerar (padrão: 1)
def gerarEmail(tamanho=10 , tipoEmail="@gmail" , quantidadeEmails=1):
    
    # Conjunto de caracteres permitidos para gerar nomes de usuário (apenas letras minúsculas a-z)
    caracs = "abcdefghijklmnopqrstuvwxyz"
    # nums = "1234567890"  # Linha comentada originalmente
    
    # Lista para armazenar os emails gerados
    emails = list()
    # Garante que tipoEmail tenha um valor padrão se vazio
    if tipoEmail == "":
        tipoEmail = "@gmail"
    # Loop para gerar a quantidade desejada de emails únicos
    while len(emails) < quantidadeEmails:
        email = ""
        # Gera um nome de usuário aleatório com o tamanho especificado
        for carac in range(tamanho):
            email += choice(caracs)
        # Formata o email completo adicionando o domínio e .com
        email = f"{email}{tipoEmail}.com"
        # Adiciona apenas se o email ainda não existir na lista (garante unicidade)
        if email not in emails:
            emails.append(email)
    # Retorna a lista de emails gerados
    return emails

#============================================================================

# Entrada interativa do usuário para configurações
quantidade = int(input("Quantos emails quer gerar? "))
tipo = input("Qual tipo de domínio?(ex: gmail) ")
# Define domínio padrão se nada for inserido
if tipo == "":
    tipo = "@gmail"
tamanhoCarac = int(input("Quantos caracteres terá os emails? "))

# Loop de confirmação/editação das configurações
confirmar = input(f"""Deseja alterar alguma escolha?
                [ 1 ] Alterar quantidadade de emails - Atual:{quantidade}
                [ 2 ] Alterar tipo de domínio - Atual:{tipo}
                [ 3 ] Alterar tamanho do email - Atual:{tamanhoCarac}
                [ 4 ] Concluir  """)
while confirmar != "4":
    # Opção 1: alterar quantidade
    if confirmar == "1":
        quantidade = int(input("Quantos emails quer gerar? "))
    # Opção 2: alterar tipo de domínio
    elif confirmar == "2":
        tipo = input("Qual tipo de domínio?(padrao: gmail) ")
        if tipo == "":
            tipo = "@gmail"
    # Opção 3: alterar tamanho
    elif confirmar == "3":
        tamanhoCarac = int(input("Quantos caracteres terá os emails? "))
    # Opção inválida
    else:
        print("Opção inválida, tente novamente")
    # Repete o menu de confirmação com valores atualizados
    confirmar = input(f"""Deseja alterar alguma escolha?
                [ 1 ] Alterar quantidadade de emails - Atual:{quantidade}
                [ 2 ] Alterar tipo de domínio - Atual:{tipo}
                [ 3 ] Alterar tamanho do email - Atual:{tamanhoCarac}
                [ 4 ] Concluir""")
    
# Gera e imprime os emails com as configurações finais
print(gerarEmail(tamanho=tamanhoCarac ,quantidadeEmails=quantidade , tipoEmail=tipo))

