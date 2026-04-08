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
        BotCommand("start", "🚀 Iniciar atendimento"),
        BotCommand("ajuda", "❓ Ajuda")
    ]
    await application.bot.set_my_commands(commands)

if __name__ == '__main__':
    # Configuração específica para Windows
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
    # Criar aplicação
    application = Application.builder().token(BOT_TOKEN).build()
    
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