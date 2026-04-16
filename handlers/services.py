from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from keyboards.inline import *
from messages.texts import *
from config import GHOST_SERVICES, TIO_DUCK_SERVICES, CANAL_LINK

async def handle_service_acquired(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler para o botão SERVIÇO ADQUIRIDO"""
    query = update.callback_query
    await query.answer()
    
    await query.edit_message_text(
        text=SERVICE_SELECTION,
        reply_markup=services_keyboard(),
        parse_mode='HTML'
    )

async def handle_consultas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler para o botão CONSULTAS"""
    query = update.callback_query
    await query.answer()
    
    await query.edit_message_text(
        text="🔍 <b>SERVIÇOS DE CONSULTA</b>\n\n<i>Selecione logo abaixo o serviço que você adquiriu em nosso site:</i>",
        reply_markup=consultas_keyboard(),
        parse_mode='HTML'
    )

async def handle_cards(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler para o botão CARTÕES"""
    query = update.callback_query
    await query.answer()
    
    await query.edit_message_text(
        text=CARD_SERVICES,
        reply_markup=cards_keyboard(),
        parse_mode='HTML'
    )

async def handle_service_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler para seleção de serviço específico"""
    query = update.callback_query
    await query.answer()
    
    service = query.data.replace('service_', '')
    context.user_data['selected_service'] = service
    
    user = query.from_user
    user_id = user.id
    username = user.username
    first_name = user.first_name
    
    if service in GHOST_SERVICES:
        message = ghost_specialist_message(service)
        keyboard = specialist_keyboard('ghost', service, from_screen='consultas',
                                       user_id=user_id, username=username, first_name=first_name)
    elif service in TIO_DUCK_SERVICES:
        message = tio_duck_specialist_message(service)
        keyboard = specialist_keyboard('tio_duck', service, from_screen='consultas',
                                       user_id=user_id, username=username, first_name=first_name)
    else:
        return
    
    await query.edit_message_text(
        text=message,
        reply_markup=keyboard,
        parse_mode='HTML'
    )

async def handle_card_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler para seleção de tipo de cartão"""
    query = update.callback_query
    await query.answer()
    
    card_type = "Info CC S/Verificação" if query.data == 'card_no_verification' else "Info CC Verificado"
    context.user_data['selected_service'] = card_type
    
    user = query.from_user
    user_id = user.id
    username = user.username
    first_name = user.first_name
    
    if card_type == "Info CC Verificado":
        message = ghost_specialist_message(card_type)
        keyboard = specialist_keyboard('ghost', card_type, from_screen='cards',
                                       user_id=user_id, username=username, first_name=first_name)
    else:
        message = tio_duck_specialist_message(card_type)
        keyboard = specialist_keyboard('tio_duck', card_type, from_screen='cards',
                                       user_id=user_id, username=username, first_name=first_name)
    
    await query.edit_message_text(
        text=message,
        reply_markup=keyboard,
        parse_mode='HTML'
    )

async def handle_back_to_main(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler para voltar ao menu principal"""
    query = update.callback_query
    await query.answer()
    
    user = query.from_user
    first_name = user.first_name or "Visitante"
    
    await query.edit_message_text(
        text=WELCOME_MESSAGE.format(first_name=first_name),
        reply_markup=main_menu_keyboard(),
        parse_mode='HTML'
    )

async def handle_back_to_services(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler para voltar ao menu de serviços (SERVIÇO ADQUIRIDO)"""
    query = update.callback_query
    await query.answer()
    
    await query.edit_message_text(
        text=SERVICE_SELECTION,
        reply_markup=services_keyboard(),
        parse_mode='HTML'
    )

async def handle_back_to_consultas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler para voltar à tela de consultas"""
    query = update.callback_query
    await query.answer()
    
    await query.edit_message_text(
        text="🔍 <b>SERVIÇOS DE CONSULTA</b>\n\n<i>Selecione o serviço adquirido:</i>",
        reply_markup=consultas_keyboard(),
        parse_mode='HTML'
    )

async def handle_back_to_cards(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler para voltar à tela de cartões"""
    query = update.callback_query
    await query.answer()
    
    await query.edit_message_text(
        text=CARD_SERVICES,
        reply_markup=cards_keyboard(),
        parse_mode='HTML'
    )

async def handle_partners(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler para o botão PARCEIROS"""
    query = update.callback_query
    await query.answer()
    
    await query.edit_message_text(
        text=PARTNERS_MESSAGE,
        reply_markup=partners_keyboard(),
        parse_mode='HTML',
        disable_web_page_preview=True
    )

async def handle_help_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler para o botão AJUDA"""
    query = update.callback_query
    await query.answer()
    
    await query.edit_message_text(
        text=HELP_MENU_MESSAGE,
        reply_markup=help_menu_keyboard(),
        parse_mode='HTML'
    )

async def handle_how_it_works(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler para COMO FUNCIONA"""
    query = update.callback_query
    await query.answer()
    
    await query.edit_message_text(
        text=HOW_IT_WORKS_MESSAGE,
        reply_markup=help_back_keyboard(),
        parse_mode='HTML'
    )

async def handle_deadlines(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler para PRAZOS"""
    query = update.callback_query
    await query.answer()
    
    await query.edit_message_text(
        text=DEADLINES_MESSAGE,
        reply_markup=help_back_keyboard(),
        parse_mode='HTML'
    )

async def handle_payments(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler para PAGAMENTOS"""
    query = update.callback_query
    await query.answer()
    
    await query.edit_message_text(
        text=PAYMENTS_MESSAGE,
        reply_markup=help_back_keyboard(),
        parse_mode='HTML'
    )

async def handle_rules(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler para o botão REGRAS"""
    query = update.callback_query
    await query.answer()
    
    keyboard = [
        [InlineKeyboardButton("🏠 Início", callback_data='back_to_main')]
    ]
    
    await query.edit_message_text(
        text=RULES_MESSAGE,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode='HTML'
    )

async def handle_business_hours(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler para o botão HORÁRIOS (apenas informativo)"""
    query = update.callback_query
    await query.answer()
    
    keyboard = [
        [InlineKeyboardButton("🏠 Início", callback_data='back_to_main')]
    ]
    
    await query.edit_message_text(
        text=BUSINESS_HOURS_MESSAGE,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode='HTML'
    )

async def handle_recharges(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler para o botão RECARGAS"""
    query = update.callback_query
    await query.answer()
    
    await query.edit_message_text(
        text=RECHARGES_MESSAGE,
        reply_markup=recharges_keyboard(),
        parse_mode='HTML'
    )

async def handle_recharge_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler para seleção de operadora de recarga"""
    query = update.callback_query
    await query.answer()
    
    operator = query.data.replace('recharge_', '')
    context.user_data['selected_service'] = f"RECARGA {operator}"
    
    user = query.from_user
    user_id = user.id
    username = user.username
    first_name = user.first_name
    
    from messages.texts import claro_message, tim_message, vivo_message
    
    if operator == 'CLARO':
        message = claro_message()
    elif operator == 'TIM':
        message = tim_message()
    elif operator == 'VIVO':
        message = vivo_message()
    else:
        return
    
    keyboard = recharge_specialist_keyboard(operator, from_screen='recharges',
                                            user_id=user_id, username=username, first_name=first_name)
    
    await query.edit_message_text(
        text=message,
        reply_markup=keyboard,
        parse_mode='HTML'
    )

async def handle_bot_vip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler para o botão BOT VIP"""
    query = update.callback_query
    await query.answer()
    
    await query.edit_message_text(
        text=BOT_VIP_MESSAGE,
        reply_markup=bot_vip_keyboard(),
        parse_mode='HTML'
    )

async def handle_request_quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler para SOLICITAR ORÇAMENTO"""
    query = update.callback_query
    await query.answer()
    
    keyboard = [
        [InlineKeyboardButton("💬 Falar com Especialista", url=CANAL_LINK)],
        [InlineKeyboardButton("🏠 Início", callback_data='bot_vip')]
    ]
    
    await query.edit_message_text(
        text=REQUEST_QUOTE_MESSAGE,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode='HTML'
    )

async def handle_ff_accounts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler para o botão CONTAS FF"""
    query = update.callback_query
    await query.answer()
    
    await query.edit_message_text(
        text=FF_ACCOUNTS_MESSAGE,
        reply_markup=ff_accounts_keyboard(),
        parse_mode='HTML'
    )

async def handle_ff_accounts_list(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler para VER CONTAS DISPONÍVEIS"""
    query = update.callback_query
    await query.answer()
    
    await query.edit_message_text(
        text=FF_ACCOUNTS_LIST_MESSAGE,
        reply_markup=ff_accounts_list_keyboard(),
        parse_mode='HTML'
    )

async def handle_ff_prices(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler para VER PREÇOS"""
    query = update.callback_query
    await query.answer()
    
    await query.edit_message_text(
        text=FF_PRICES_MESSAGE,
        reply_markup=ff_prices_keyboard(),
        parse_mode='HTML'
    )

async def handle_request_ff_account(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler para SOLICITAR CONTA FF"""
    query = update.callback_query
    await query.answer()
    
    keyboard = [
        [InlineKeyboardButton("💬 Falar com Especialista", url=CANAL_LINK)],
        [InlineKeyboardButton("🏡 Retornar", callback_data='ff_accounts')]
    ]
    
    await query.edit_message_text(
        text=REQUEST_FF_ACCOUNT_MESSAGE,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode='HTML'
    )

async def handle_fake_notes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler para o botão NOTAS FALSAS"""
    query = update.callback_query
    await query.answer()
    
    await query.edit_message_text(
        text=FAKE_NOTES_MESSAGE,
        reply_markup=fake_notes_keyboard(),
        parse_mode='HTML'
    )

async def handle_fake_notes_prices(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler para VER VALORES"""
    query = update.callback_query
    await query.answer()
    
    await query.edit_message_text(
        text=FAKE_NOTES_PRICES_MESSAGE,
        reply_markup=fake_notes_back_keyboard(),
        parse_mode='HTML'
    )

async def handle_fake_notes_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler para COMO FUNCIONA"""
    query = update.callback_query
    await query.answer()
    
    await query.edit_message_text(
        text=FAKE_NOTES_INFO_MESSAGE,
        reply_markup=fake_notes_back_keyboard(),
        parse_mode='HTML'
    )

async def handle_request_fake_notes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler para SOLICITAR NOTAS"""
    query = update.callback_query
    await query.answer()
    
    keyboard = [
        [InlineKeyboardButton("💬 Falar com Especialista", url=CANAL_LINK)],
        [InlineKeyboardButton("🏡 Retornar", callback_data='fake_notes')]
    ]
    
    await query.edit_message_text(
        text=REQUEST_FAKE_NOTES_MESSAGE,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode='HTML'
    )