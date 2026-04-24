#!/usr/bin/env python3
"""
Gerador de Emails Profissional.
Melhorias: validação input, charset completo (letras, números, ._ ), regex validação,
type hints, progress bar (tqdm), logging, menu sem repetição, suporte YAML.
"""

from random import choice
from typing import List
import re
import logging
from tqdm import tqdm
import sys
import argparse
import yaml  # pip install pyyaml

# Configuração de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Charset realista para usernames de email (RFC 5322 simplificado)
CHARSET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._'

# Regex para validar formato básico de email
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

DOMINIOS_COMUNS = ['@gmail.com', '@outlook.com', '@yahoo.com', '@hotmail.com', '@protonmail.com']

def validar_input_int(prompt: str, min_val: int = 1, max_val: int = 1000) -> int:
    """Valida e retorna inteiro do input."""
    while True:
        try:
            valor = int(input(prompt))
            if min_val <= valor <= max_val:
                return valor
            print(f"Valor deve ser entre {min_val} e {max_val}.")
        except ValueError:
            print("Digite um número válido.")

def validar_dominio() -> str:
    """Valida domínio inserido."""
    while True:
        dominio = input("Domínio (ex: gmail.com)? ").strip()
        if not dominio:
            return '@gmail.com'
        if dominio.startswith('@'):
            dominio = dominio[1:]
        if '.' in dominio and re.match(r'^[a-z0-9.-]+\.[a-z]{2,}$', dominio, re.IGNORECASE):
            return f"@{dominio.lower()}"
        print("Domínio inválido. Ex: gmail.com")

def gerar_email(tamanho: int, dominio: str) -> str:
    """Gera um email aleatório único."""
    usuario = ''.join(choice(CHARSET) for _ in range(tamanho))
    email = f"{usuario}{dominio}"
    if EMAIL_REGEX.match(email):
        return email
    # Fallback se regex falhar (raro)
    logger.warning(f"Email inválido gerado: {email}, regenerando...")
    return gerar_email(tamanho, dominio)

def gerar_emails(tamanho: int, dominio: str, quantidade: int) -> List[str]:
    """
    Gera lista de emails únicos e válidos.
    
    Args:
        tamanho: Tamanho do username.
        dominio: Domínio como '@gmail.com'.
        quantidade: Número de emails.
    
    Returns:
        Lista de emails únicos.
    """
    emails = set()
    with tqdm(total=quantidade, desc="Gerando emails", unit="email") as pbar:
        while len(emails) < quantidade:
            email = gerar_email(tamanho, dominio)
            emails.add(email)
            pbar.update(1)
    logger.info(f"Gerados {quantidade} emails únicos.")
    return list(emails)

def carregar_config(yaml_path: str = None) -> dict:
    """Carrega config de YAML se fornecido."""
    if yaml_path:
        try:
            with open(yaml_path, 'r') as f:
                return yaml.safe_load(f)
        except Exception as e:
            logger.error(f"Erro YAML: {e}")
    # Default config
    return {
        'tamanho': 10,
        'dominio': '@gmail.com',
        'quantidade': 1
    }

def menu_interativo(config: dict) -> tuple:
    """Menu interativo sem repetição."""
    print("\n=== Configurações atuais ===")
    print(f"Tamanho username: {config['tamanho']}")
    print(f"Domínio: {config['dominio']}")
    print(f"Quantidade: {config['quantidade']}")
    
    while True:
        escolha = input("\n[1] Alterar tamanho [2] Alterar domínio [3] Alterar qtd [4] Gerar: ").strip()
        if escolha == '1':
            config['tamanho'] = validar_input_int("Tamanho (5-50)? ", 5, 50)
        elif escolha == '2':
            config['dominio'] = validar_dominio()
        elif escolha == '3':
            config['quantidade'] = validar_input_int("Quantidade (1-100)? ", 1, 100)
        elif escolha == '4':
            break
        else:
            print("Opção inválida!")
    return config['tamanho'], config['dominio'], config['quantidade']

def main():
    parser = argparse.ArgumentParser(description="Gerador de Emails Profissional")
    parser.add_argument('-q', '--quantidade', type=int, default=1, help="Qtd emails")
    parser.add_argument('-t', '--tamanho', type=int, default=10, help="Tamanho username")
    parser.add_argument('-d', '--dominio', default='@gmail.com', help="Domínio ex: @gmail.com")
    parser.add_argument('-c', '--config', help="Arquivo YAML config")
    parser.add_argument('--interativo', action='store_true', help="Modo interativo")
    
    args = parser.parse_args()
    
    # Carrega config
    config = carregar_config(args.config)
    config['quantidade'] = args.quantidade or config['quantidade']
    config['tamanho'] = args.tamanho or config['tamanho']
    config['dominio'] = args.dominio or config['dominio']
    
    if args.interativo:
        tamanho, dominio, quantidade = menu_interativo(config)
    else:
        tamanho, dominio, quantidade = config['tamanho'], config['dominio'], config['quantidade']
    
    # Gera e exibe
    emails = gerar_emails(tamanho, dominio, quantidade)
    print("\nEmails gerados:")
    for email in emails:
        print(email)
    
    logger.info("Geração concluída!")

if __name__ == "__main__":
    main()

