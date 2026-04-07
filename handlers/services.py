from telegram import Update
from telegram.ext import ContextTypes
from keyboards.inline import *
from messages.texts import *
from config import GHOST_SERVICES, TIO_DUCK_SERVICES

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
        text="🔍 <b>SERVIÇOS DE CONSULTA</b>\n\nSelecione o serviço adquirido:",
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
    
    if service in GHOST_SERVICES:
        message = ghost_specialist_message(service)
        keyboard = specialist_keyboard('ghost', service, from_screen='consultas')
    elif service in TIO_DUCK_SERVICES:
        message = tio_duck_specialist_message(service)
        keyboard = specialist_keyboard('tio_duck', service, from_screen='consultas')
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
    message = card_specialist_message(card_type)
    keyboard = specialist_keyboard('ghost', card_type, from_screen='cards')
    
    await query.edit_message_text(
        text=message,
        reply_markup=keyboard,
        parse_mode='HTML'
    )

async def handle_back_to_main(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler para voltar ao menu principal"""
    query = update.callback_query
    await query.answer()
    
    await query.edit_message_text(
        text=WELCOME_MESSAGE,
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
        text="🔍 <b>SERVIÇOS DE CONSULTA</b>\n\nSelecione o serviço adquirido:",
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