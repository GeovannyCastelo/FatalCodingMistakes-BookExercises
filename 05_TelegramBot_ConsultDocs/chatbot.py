import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Configuración del logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Token de acceso del bot, que obtienes de BotFather en Telegram
TOKEN = 'TU_TOKEN_AQUI'

# Función que se ejecuta cuando el usuario envía el comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('¡Hola! Soy tu bot de Telegram.')

# Función que se ejecuta cuando el usuario envía el comando /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Puedes usar los siguientes comandos:\n/start - Iniciar la conversación\n/help - Mostrar esta ayuda')

# Función principal para configurar el bot
async def main() -> None:
    # Crear la aplicación
    app = Application.builder().token(TOKEN).build()

    # Inicializar la aplicación
    await app.initialize()

    # Registrar comandos y las funciones correspondientes
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    # Iniciar el bot con polling
    logging.info("Iniciando el bot...")
    await app.start()
    await app.updater.start_polling()

    # Mantener el bot corriendo
    logging.info("Bot en ejecución. Presiona Ctrl+C para detenerlo.")
    await asyncio.Event().wait()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
