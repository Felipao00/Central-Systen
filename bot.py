import logging
import sys
import asyncio
from telegram import BotCommand
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from config import BOT_TOKEN
from handlers import *

# Desativa logs HTTP
logging.getLogger('httpx').setLevel(logging.ERROR)
logging.getLogger('httpcore').setLevel(logging.ERROR)
logging.getLogger('telegram.vendor.ptb_urllib3.urllib3').setLevel(logging.ERROR)

# Configuração de logging
logging.basicConfig(
    format='%(asctime)s - %(message)s',
    level=logging.WARNING,
    datefmt='%H:%M:%S'
)

async def set_bot_commands(application: Application):
    """Configura o menu de comandos do bot"""
    commands = [
        BotCommand("start", "🚀 Iniciar atendimento")
    ]
    await application.bot.set_my_commands(commands)

if __name__ == '__main__':
    # Configuração específica para Windows
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
    # Criar aplicação
    application = (
        Application.builder()
        .token(BOT_TOKEN)
        .build()
    )

    
    # Adicionar handlers
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('menu', menu))
    application.add_handler(CommandHandler('servicos', servicos))
    application.add_handler(CommandHandler('ajuda', ajuda))
    application.add_handler(CommandHandler('contato', contato))
    
    # Callback Query Handlers
    application.add_handler(CallbackQueryHandler(handle_service_acquired, pattern='^service_acquired$'))
    application.add_handler(CallbackQueryHandler(handle_consultas, pattern='^consultas$'))
    application.add_handler(CallbackQueryHandler(handle_cards, pattern='^cards$'))
    application.add_handler(CallbackQueryHandler(handle_service_selection, pattern='^service_'))
    application.add_handler(CallbackQueryHandler(handle_card_selection, pattern='^card_'))
    application.add_handler(CallbackQueryHandler(handle_back_to_main, pattern='^back_to_main$'))
    application.add_handler(CallbackQueryHandler(handle_back_to_services, pattern='^back_to_services$'))
    application.add_handler(CallbackQueryHandler(handle_back_to_consultas, pattern='^back_to_consultas$'))
    application.add_handler(CallbackQueryHandler(handle_back_to_cards, pattern='^back_to_cards$'))
    # Na seção de Callbacks, adicione:
    application.add_handler(CallbackQueryHandler(handle_recharges, pattern='^recharges$'))
    application.add_handler(CallbackQueryHandler(handle_recharge_selection, pattern='^recharge_'))
    # Novos handlers do menu
    application.add_handler(CallbackQueryHandler(handle_partners, pattern='^partners$'))
    application.add_handler(CallbackQueryHandler(handle_help_menu, pattern='^help_menu$'))
    application.add_handler(CallbackQueryHandler(handle_how_it_works, pattern='^how_it_works$'))
    application.add_handler(CallbackQueryHandler(handle_deadlines, pattern='^deadlines$'))
    application.add_handler(CallbackQueryHandler(handle_payments, pattern='^payments$'))
    # Na seção de Callbacks, adicione:
    application.add_handler(CallbackQueryHandler(handle_business_hours, pattern='^business_hours$'))
    application.add_handler(CallbackQueryHandler(handle_rules, pattern='^rules$'))
    # Callbacks do BOT VIP
    application.add_handler(CallbackQueryHandler(handle_bot_vip, pattern='^bot_vip$'))
    application.add_handler(CallbackQueryHandler(handle_request_quote, pattern='^request_quote$'))
    # Callbacks do FREE FIRE
    application.add_handler(CallbackQueryHandler(handle_ff_accounts, pattern='^ff_accounts$'))
    application.add_handler(CallbackQueryHandler(handle_ff_accounts_list, pattern='^ff_accounts_list$'))
    application.add_handler(CallbackQueryHandler(handle_ff_prices, pattern='^ff_prices$'))
    application.add_handler(CallbackQueryHandler(handle_request_ff_account, pattern='^request_ff_account$'))
    # Callbacks do NOTAS FALSAS
    application.add_handler(CallbackQueryHandler(handle_fake_notes, pattern='^fake_notes$'))
    application.add_handler(CallbackQueryHandler(handle_fake_notes_prices, pattern='^fake_notes_prices$'))
    application.add_handler(CallbackQueryHandler(handle_fake_notes_info, pattern='^fake_notes_info$'))
    application.add_handler(CallbackQueryHandler(handle_request_fake_notes, pattern='^request_fake_notes$'))
    
    # Configurar menu de comandos
    application.post_init = set_bot_commands
    
    print("\n" + "="*50)
    print("🤖 BOT DA CENTRAL SYSTEN INICIADO!")
    print("="*50)
    print("✅ Bot online e aguardando clientes")
    print("📱 Envie /start no Telegram para testar")
    print("⚡ Menu de comandos configurado!")
    print("⏹️  Pressione Ctrl+C para parar\n")
    
    # Iniciar o bot
    application.run_polling(poll_interval=1.0)