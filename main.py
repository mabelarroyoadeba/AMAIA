
""""
IMPORTANTE:

INSTALAR:
pip install python-telegram-bot
pip install pyTelegramBotAPI
pip install transformers
pip install torch

NO INSTALAR:
pip install telegram
"""

import logging
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


# Este modelo está extraido de https://huggingface.co/docs/transformers/model_doc/blenderbot
mname = "facebook/blenderbot-400M-distill"
model = BlenderbotForConditionalGeneration.from_pretrained(mname)
tokenizer = BlenderbotTokenizer.from_pretrained(mname)

# Genera las respuestas
def modelo(UTTERANCE):
    inputs = tokenizer([UTTERANCE], return_tensors="pt")
    reply_ids = model.generate(**inputs)
    respuesta = tokenizer.batch_decode(reply_ids)[0][4:-4]
    return respuesta

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Esta es la función que responde. Se trata de meter en el modelo "update.message.text"
# y responder con el resultado del modelo
def answer(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(modelo(update.message.text))

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN_ID_BOT_TELEGRAM, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on noncommand i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, answer))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()