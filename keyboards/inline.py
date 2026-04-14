from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import InlineKeyboardButtonStyle
from config import GHOST_USERNAME, TIO_DUCK_USERNAME, GHOST_SERVICES

def main_menu_keyboard():
    """Teclado principal do bot"""
    keyboard = [
        [InlineKeyboardButton("🤝 Parceiros", callback_data='partners')],
        [InlineKeyboardButton("💎 Comunidade Vip Secreta", url="https://t.me/centralschoolofcbot")],
        [InlineKeyboardButton("🤖 Bot Vip", callback_data='bot_vip'),
         InlineKeyboardButton("🎮 Contas FF", callback_data='ff_accounts')], 
        [InlineKeyboardButton("🛒 Serviços", callback_data='service_acquired'),
         InlineKeyboardButton("📲 Recargas", callback_data='recharges')],
        [InlineKeyboardButton("📖 Regras", callback_data='rules'),
         InlineKeyboardButton("⏰ Horários", callback_data='business_hours'),
         InlineKeyboardButton("❓ Ajuda", callback_data='help_menu', style=InlineKeyboardButtonStyle.SUCCESS)],
    ]
    return InlineKeyboardMarkup(keyboard)

def services_keyboard():
    """Teclado de serviços disponíveis"""
    keyboard = [
        [InlineKeyboardButton("🔍 Consultas", callback_data='consultas')],
        [InlineKeyboardButton("💳 Cartões", callback_data='cards')],
        [InlineKeyboardButton("💸 Notas Fake", callback_data='fake_notes')],
        [InlineKeyboardButton("🏠 Voltar", callback_data='back_to_main')]
    ]
    return InlineKeyboardMarkup(keyboard)

def consultas_keyboard():
    """Teclado de consultas - Ghost e Tio Duck"""
    keyboard = [
        [InlineKeyboardButton("📄 CPF", callback_data='service_CPF'),
         InlineKeyboardButton("🏢 CNPJ", callback_data='service_CNPJ')],
        [InlineKeyboardButton("📍 CEP", callback_data='service_CEP'),
         InlineKeyboardButton("👤 NOME", callback_data='service_NOME')],
        [InlineKeyboardButton("📱 TELEFONE", callback_data='service_TELEFONE'),
         InlineKeyboardButton("🚗 PLACA", callback_data='service_PLACA')],
        [InlineKeyboardButton("💳 BIN", callback_data='service_BIN'),
         InlineKeyboardButton("🌐 IP", callback_data='service_IP')],
        [InlineKeyboardButton("🏠 Voltar", callback_data='back_to_services')]
    ]
    return InlineKeyboardMarkup(keyboard)

def cards_keyboard():
    """Teclado de serviços de cartão"""
    keyboard = [
        [InlineKeyboardButton("💳 Info CC S/Verificação", callback_data='card_no_verification')],
        [InlineKeyboardButton("✅ Info CC Verificado", callback_data='card_verified')],
        [InlineKeyboardButton("🏠 Voltar", callback_data='back_to_main')]
    ]
    return InlineKeyboardMarkup(keyboard)

def specialist_keyboard(specialist_type, service_name, from_screen='main', user_id=None, username=None, first_name=None):
    """Teclado com botão para falar com especialista - VIA CANAL"""
    
    # Link da mensagem direta do CANAL (não do especialista)
    # Formato: https://t.me/SEU_CANAL?start=msg
    CANAL_LINK = "https://t.me/+1Bs3nxvDPCgyODcx"  # 👈 Troque pelo link do seu canal
    
    if specialist_type == 'ghost':
        text = f"💬 Falar com Especialista"
    elif specialist_type == 'tio_duck':
        text = f"💬 Falar com Especialista"
    else:
        text = f"💬 Falar com Especialista"
    
    # Define para onde voltar
    if from_screen == 'consultas':
        back_callback = 'back_to_consultas'
        back_text = "🏡 Retornar"
    elif from_screen == 'cards':
        back_callback = 'back_to_cards'
        back_text = "🏡 Retornar"
    elif from_screen == 'recharges':
        back_callback = 'recharges'
        back_text = "🏡 Retornar"
    else:
        back_callback = 'back_to_main'
        back_text = "🏡 Retornar"
    
    keyboard = [
        [InlineKeyboardButton(text, url=CANAL_LINK)],
        [InlineKeyboardButton(back_text, callback_data=back_callback)]
    ]
    return InlineKeyboardMarkup(keyboard)

def partners_keyboard():
    """Teclado da área de parceiros"""
    keyboard = [
        [InlineKeyboardButton("💳 Gateway", url="https://t.me/pibankofc_bot")],
        [InlineKeyboardButton("🏠 Voltar", callback_data='back_to_main')]
    ]
    return InlineKeyboardMarkup(keyboard)

def help_menu_keyboard():
    """Teclado do menu de ajuda"""
    keyboard = [
        [InlineKeyboardButton("📋 Como Funciona", callback_data='how_it_works')],
        [InlineKeyboardButton("⏱️ Prazos", callback_data='deadlines')],
        [InlineKeyboardButton("💳 Pagamentos", callback_data='payments')],
        [InlineKeyboardButton("🏠 Voltar", callback_data='back_to_main')]
    ]
    return InlineKeyboardMarkup(keyboard)

def help_back_keyboard():
    """Teclado para voltar ao menu de ajuda"""
    keyboard = [
        [InlineKeyboardButton("🏡 Retornar", callback_data='help_menu')],
        [InlineKeyboardButton("🏠 Início", callback_data='back_to_main')]
    ]
    return InlineKeyboardMarkup(keyboard)

def out_of_hours_keyboard(from_screen='main'):
    """Teclado para quando está fora do horário"""
    if from_screen == 'consultas':
        back_callback = 'back_to_consultas'
        back_text = "🏠 Retornar"
    elif from_screen == 'cards':
        back_callback = 'back_to_cards'
        back_text = "🏠 Retornar"
    else:
        back_callback = 'back_to_main'
        back_text = "🏠 Início"
    keyboard = [[InlineKeyboardButton(back_text, callback_data=back_callback)]]
    return InlineKeyboardMarkup(keyboard)

def recharges_keyboard():
    """Teclado de operadoras de recarga"""
    keyboard = [
        [InlineKeyboardButton("🔴 Claro", callback_data='recharge_CLARO')],
        [InlineKeyboardButton("🔵 Tim", callback_data='recharge_TIM')],
        [InlineKeyboardButton("🟣 Vivo", callback_data='recharge_VIVO')],
        [InlineKeyboardButton("🏠 Voltar", callback_data='back_to_main')]
    ]
    return InlineKeyboardMarkup(keyboard)

# NOVO - Teclado para falar com especialista de recarga
def recharge_specialist_keyboard(operator, from_screen='recharges', user_id=None, username=None, first_name=None):
    """Teclado com botão para falar com especialista de recarga - VIA CANAL"""
    
    # Link do canal com mensagens diretas
    CANAL_LINK = "https://t.me/+1Bs3nxvDPCgyODcx"  # 👈 Troque pelo link do seu canal
    
    text = f"💬 Falar com Especialista"
    
    if from_screen == 'recharges':
        back_callback = 'recharges'
        back_text = "🏡Retornar"
    else:
        back_callback = 'back_to_main'
        back_text = "🏠 Início"
    
    keyboard = [
        [InlineKeyboardButton(text, url=CANAL_LINK)],
        [InlineKeyboardButton(back_text, callback_data=back_callback)]
    ]
    return InlineKeyboardMarkup(keyboard)

# Adicione no final do arquivo:

def out_of_hours_keyboard(from_screen='main'):
    """Teclado para quando está fora do horário"""
    if from_screen == 'consultas':
        back_callback = 'back_to_consultas'
        back_text = "🏠 Retornar"
    elif from_screen == 'cards':
        back_callback = 'back_to_cards'
        back_text = "🏠 Retornar"
    elif from_screen == 'recharges':
        back_callback = 'recharges'
        back_text = "🏠 Retornar"
    elif from_screen == 'bot_vip':  # 👈 NOVO
        back_callback = 'bot_vip'
    elif from_screen == 'ff_accounts':  # 👈 NOVO
        back_callback = 'ff_accounts'
        back_text = "🏠 Retornar"
    elif from_screen == 'fake_notes':  # 👈 NOVO
        back_callback = 'fake_notes'
        back_text = "🏠 Retornar"
    else:
        back_callback = 'back_to_main'
        back_text = "🏠 Início"
    
    keyboard = [
        [InlineKeyboardButton("⏰ VER HORÁRIOS", callback_data='business_hours')],
        [InlineKeyboardButton(back_text, callback_data=back_callback)]
    ]
    return InlineKeyboardMarkup(keyboard)

# NOVO - Teclado da área BOT VIP
def bot_vip_keyboard():
    """Teclado da área de BOT VIP"""
    keyboard = [
        [InlineKeyboardButton("💬 Falar Com Especialista", callback_data='request_quote')],
        [InlineKeyboardButton("🏠 Início", callback_data='back_to_main')]
    ]
    return InlineKeyboardMarkup(keyboard)

# NOVO - Teclado da área FREE FIRE
def ff_accounts_keyboard():
    """Teclado da área de CONTAS FREE FIRE"""
    keyboard = [
        [InlineKeyboardButton("💰 Contas Disponíveis", callback_data='ff_accounts_list')],
        [InlineKeyboardButton("📊 Ver Preços", callback_data='ff_prices')],
        [InlineKeyboardButton("💬 Solicitar Conta", callback_data='request_ff_account')],
        [InlineKeyboardButton("🏠 Início", callback_data='back_to_main')]
    ]
    return InlineKeyboardMarkup(keyboard)

def ff_accounts_list_keyboard():
    """Teclado da lista de contas"""
    keyboard = [
        [InlineKeyboardButton("🏡 Retornar", callback_data='ff_accounts')],
        [InlineKeyboardButton("🏠 Início", callback_data='back_to_main')]
    ]
    return InlineKeyboardMarkup(keyboard)

def ff_prices_keyboard():
    """Teclado de preços"""
    keyboard = [
        [InlineKeyboardButton("🏡 Retornar", callback_data='ff_accounts')],
        [InlineKeyboardButton("🏠 Início", callback_data='back_to_main')]
    ]
    return InlineKeyboardMarkup(keyboard)

def fake_notes_keyboard():
    """Teclado da área de NOTAS FALSAS"""
    keyboard = [
        [InlineKeyboardButton("💰 Ver Valores", callback_data='fake_notes_prices')],
        [InlineKeyboardButton("📋 Como Funciona", callback_data='fake_notes_info')],
        [InlineKeyboardButton("💬 Solicitar Notas", callback_data='request_fake_notes')],
        [InlineKeyboardButton("🏠 Início", callback_data='back_to_main')]
    ]
    return InlineKeyboardMarkup(keyboard)

def fake_notes_back_keyboard():
    """Teclado para voltar à área de notas falsas"""
    keyboard = [
        [InlineKeyboardButton("💬 Solicitar Notas", callback_data='request_fake_notes')],
        [InlineKeyboardButton("🏡 Retornar", callback_data='fake_notes')],
        [InlineKeyboardButton("🏠 Início", callback_data='back_to_main')]
    ]
    return InlineKeyboardMarkup(keyboard)