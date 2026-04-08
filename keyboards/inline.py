from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from config import GHOST_USERNAME, TIO_DUCK_USERNAME, GHOST_SERVICES

def main_menu_keyboard():
    """Teclado principal do bot"""
    keyboard = [
        [InlineKeyboardButton("🛒 Serviços Disponíveis", callback_data='service_acquired')]
    ]
    return InlineKeyboardMarkup(keyboard)

def services_keyboard():
    """Teclado de serviços disponíveis"""
    keyboard = [
        [InlineKeyboardButton("🔍 Consultas", callback_data='consultas')],
        [InlineKeyboardButton("💳 Cartões", callback_data='cards')],
        [InlineKeyboardButton("🏠 Voltar", callback_data='back_to_main')]
    ]
    return InlineKeyboardMarkup(keyboard)

def consultas_keyboard():
    """Teclado de consultas - Ghost e Tio Duck"""
    keyboard = [
        [InlineKeyboardButton("📄 Consulta de CPF", callback_data='service_CPF'),
         InlineKeyboardButton("🏢 Consulta de CNPJ", callback_data='service_CNPJ')],
        [InlineKeyboardButton("📍 Consulta de CEP", callback_data='service_CEP'),
         InlineKeyboardButton("👤 Consulta de NOME", callback_data='service_NOME')],
        [InlineKeyboardButton("📱 Consulta de TELEFONE", callback_data='service_TELEFONE'),
         InlineKeyboardButton("🚗 Consulta de PLACA", callback_data='service_PLACA')],
        [InlineKeyboardButton("💳 Consulta de BIN", callback_data='service_BIN'),
         InlineKeyboardButton("🌐 Consulta de IP", callback_data='service_IP')],
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

def specialist_keyboard(specialist_type, service_name, from_screen='main'):
    """Teclado com botão para falar com especialista"""
    if specialist_type == 'ghost':
        url = f"https://t.me/{GHOST_USERNAME.replace('@', '')}"
        text = f"💬 Falar com Especialista"
    elif specialist_type == 'tio_duck':
        url = f"https://t.me/{TIO_DUCK_USERNAME.replace('@', '')}"
        text = f"💬 Falar com Especialista"
    else:
        url = f"https://t.me/{GHOST_USERNAME.replace('@', '')}"
        text = f"💬 Falar com Especialista"
    
    # Define para onde voltar baseado em de onde veio
    if from_screen == 'consultas':
        back_callback = 'back_to_consultas'
        back_text = "🏠 Retornar"
    elif from_screen == 'cards':
        back_callback = 'back_to_cards'
        back_text = "🏠 Retornar"
    else:
        back_callback = 'back_to_main'
        back_text = "🏠 Início"
    
    keyboard = [
        [InlineKeyboardButton(text, url=url)],
        [InlineKeyboardButton(back_text, callback_data=back_callback)]
    ]
    return InlineKeyboardMarkup(keyboard)