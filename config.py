import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
GHOST_USERNAME = os.getenv('GHOST_USERNAME')
TIO_DUCK_USERNAME = os.getenv('TIO_DUCK_USERNAME')

# Mapeamento dos serviços
GHOST_SERVICES = ['NOME', 'TELEFONE', 'PLACA', 'BIN', 'Info CC Verificado']
TIO_DUCK_SERVICES = ['CPF', 'CNPJ', 'CEP', 'IP', 'Info CC S/Verificação']