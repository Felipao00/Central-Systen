from telegram import Update
from telegram.ext import ContextTypes
from keyboards.inline import main_menu_keyboard, services_keyboard
from messages.texts import WELCOME_MESSAGE, SERVICE_SELECTION

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler para o comando /start"""
    user = update.effective_user
    first_name = user.first_name or "Visitante"
    
    await update.message.reply_text(
        text=WELCOME_MESSAGE.format(first_name=first_name),
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