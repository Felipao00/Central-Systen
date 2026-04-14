from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from config import GHOST_USERNAME, TIO_DUCK_USERNAME, GHOST_SERVICES

# ============================================
# MENU PRINCIPAL
# ============================================

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
         InlineKeyboardButton("🚨 Ajuda", callback_data='help_menu')],
    ]
    return InlineKeyboardMarkup(keyboard)

# ============================================
# SERVIÇOS
# ============================================

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
        [InlineKeyboardButton("📄 Consulta CPF", callback_data='service_CPF'),
         InlineKeyboardButton("🏢 Consulta CNPJ", callback_data='service_CNPJ')],
        [InlineKeyboardButton("📍 Consulta CEP", callback_data='service_CEP'),
         InlineKeyboardButton("👤 Consulta NOME", callback_data='service_NOME')],
        [InlineKeyboardButton("📱 Consulta TELEFONE", callback_data='service_TELEFONE'),
         InlineKeyboardButton("🚗 Consulta PLACA", callback_data='service_PLACA')],
        [InlineKeyboardButton("💳 Consulta BIN", callback_data='service_BIN'),
         InlineKeyboardButton("🌐 Consulta IP", callback_data='service_IP')],
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

# ============================================
# RECARGAS
# ============================================

def recharges_keyboard():
    """Teclado de operadoras de recarga"""
    keyboard = [
        [InlineKeyboardButton("🔴 Claro", callback_data='recharge_CLARO')],
        [InlineKeyboardButton("🔵 Tim", callback_data='recharge_TIM')],
        [InlineKeyboardButton("🟣 Vivo", callback_data='recharge_VIVO')],
        [InlineKeyboardButton("🏠 Voltar", callback_data='back_to_main')]
    ]
    return InlineKeyboardMarkup(keyboard)

def recharge_specialist_keyboard(operator, from_screen='recharges', user_id=None, username=None, first_name=None):
    """Teclado com botão para falar com especialista de recarga - VIA CANAL"""
    CANAL_LINK = "https://t.me/+1Bs3nxvDPCgyODcx"
    text = f"💬 Falar com Especialista"
    
    if from_screen == 'recharges':
        back_callback = 'recharges'
        back_text = "🏡 Retornar"
    else:
        back_callback = 'back_to_main'
        back_text = "🏠 Início"
    
    keyboard = [
        [InlineKeyboardButton(text, url=CANAL_LINK, style="success")],
        [InlineKeyboardButton(back_text, callback_data=back_callback, style="danger")]
    ]
    return InlineKeyboardMarkup(keyboard)

# ============================================
# BOT VIP
# ============================================

def bot_vip_keyboard():
    """Teclado da área de BOT VIP"""
    keyboard = [
        [InlineKeyboardButton("💬 Falar Com Especialista", callback_data='request_quote')],
        [InlineKeyboardButton("🏠 Início", callback_data='back_to_main')]
    ]
    return InlineKeyboardMarkup(keyboard)

# ============================================
# CONTAS FREE FIRE
# ============================================

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
        [InlineKeyboardButton("💬 Solicitar Conta", callback_data='request_ff_account')],
        [InlineKeyboardButton("🏡 Retornar", callback_data='ff_accounts')],
        [InlineKeyboardButton("🏠 Início", callback_data='back_to_main')]
    ]
    return InlineKeyboardMarkup(keyboard)

# ============================================
# NOTAS FALSAS
# ============================================

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

# ============================================
# PARCEIROS E AJUDA
# ============================================

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

# ============================================
# ESPECIALISTA E FORA DO HORÁRIO
# ============================================

def specialist_keyboard(specialist_type, service_name, from_screen='main', user_id=None, username=None, first_name=None):
    """Teclado com botão para falar com especialista - VIA CANAL"""
    CANAL_LINK = "https://t.me/+1Bs3nxvDPCgyODcx"
    text = f"💬 Falar com Especialista"
    
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
        [InlineKeyboardButton(text, url=CANAL_LINK, style="success")],
        [InlineKeyboardButton(back_text, callback_data=back_callback, style="danger")]
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
    elif from_screen == 'recharges':
        back_callback = 'recharges'
        back_text = "🏠 Retornar"
    elif from_screen == 'bot_vip':
        back_callback = 'bot_vip'
        back_text = "🏠 Retornar"
    elif from_screen == 'ff_accounts':
        back_callback = 'ff_accounts'
        back_text = "🏠 Retornar"
    elif from_screen == 'fake_notes':
        back_callback = 'fake_notes'
        back_text = "🏠 Retornar"
    else:
        back_callback = 'back_to_main'
        back_text = "🏠 Início"
    
    keyboard = [
        [InlineKeyboardButton("⏰ Ver Horários", callback_data='business_hours')],
        [InlineKeyboardButton(back_text, callback_data=back_callback)]
    ]
    return InlineKeyboardMarkup(keyboard)