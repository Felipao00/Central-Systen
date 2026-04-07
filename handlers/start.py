from telegram import Update
from telegram.ext import ContextTypes
from keyboards.inline import main_menu_keyboard, services_keyboard
from messages.texts import WELCOME_MESSAGE, SERVICE_SELECTION

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler para o comando /start"""
    await update.message.reply_text(
        text=WELCOME_MESSAGE,
        reply_markup=main_menu_keyboard(),
        parse_mode='HTML'
    )

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler para o comando /menu"""
    await update.message.reply_text(
        text=WELCOME_MESSAGE,
        reply_markup=main_menu_keyboard(),
        parse_mode='HTML'
    )

async def servicos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler para o comando /servicos"""
    await update.message.reply_text(
        text=SERVICE_SELECTION,
        reply_markup=services_keyboard(),
        parse_mode='HTML'
    )

async def ajuda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler para o comando /ajuda"""
    help_text = """
🆘 <b>CENTRAL DE AJUDA</b>

<b>Como funciona:</b>
1️⃣ Escolha o tipo de serviço
2️⃣ Selecione o serviço adquirido
3️⃣ Fale com nosso especialista

<b>Dúvidas frequentes:</b>
⏱️ <i>Prazo de entrega:</i> Imediato após pagamento
💳 <i>Formas de pagamento:</i> PIX, Cartão, Crypto
📞 <i>Suporte:</i> Use /contato

<b>Ghost:</b> CPF • CNPJ • CEP • NOME
<b>Tio Duck:</b> TELEFONE • PLACA • BIN • IP
"""
    await update.message.reply_text(
        text=help_text,
        parse_mode='HTML'
    )

async def contato(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler para o comando /contato"""
    from config import GHOST_USERNAME, TIO_DUCK_USERNAME
    from telegram import InlineKeyboardButton, InlineKeyboardMarkup
    
    contact_text = f"""
📞 <b>CENTRAL DE ATENDIMENTO</b>

Escolha com qual especialista deseja falar:

👻 <b>Ghost:</b> {GHOST_USERNAME}
🦆 <b>Tio Duck:</b> {TIO_DUCK_USERNAME}
"""
    keyboard = [
        [InlineKeyboardButton("💬 FALAR COM GHOST", url=f"https://t.me/{GHOST_USERNAME.replace('@', '')}")],
        [InlineKeyboardButton("💬 FALAR COM TIO DUCK", url=f"https://t.me/{TIO_DUCK_USERNAME.replace('@', '')}")]
    ]
    
    await update.message.reply_text(
        text=contact_text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode='HTML'
    )