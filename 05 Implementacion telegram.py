'''
Importante:
pip install pyTelegramBotAPI--> ejecutar desde el terminal

INSTALAR
pip install python-telegram-bot
pip install pyTelegramBotAPI
pip install transformers
pip install torch
NO INSTALAR!
pip install telegram
'''

import logging
import openai

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

openai.api_key ='OPENAI_API_KEY'

def modelo(UTTERANCE):
    ft_model = "ada:ft-mabel-2022-12-30-17-12-42"
    res = openai.Completion.create(model=ft_model, prompt=UTTERANCE, max_tokens=18, temperature=1)
    respuesta = res['choices'][0]['text']
    return respuesta

# Activa el logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Función de respuesta a los mensajes del usuario.
def answer(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(modelo(update.message.text))

def main():
    # Inicialización
    updater = Updater("CHATBOT_ID", use_context=True)
    dispatcher = updater.dispatcher

    # Responde a la entrada del usuario
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, answer))

    # Arranca el chatbot
    updater.start_polling()

    # Ejecuta el chatbot hasta que se cancela la ejecución con Ctrl-C 
    updater.idle()


if __name__ == '__main__':
    main()