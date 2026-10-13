import os
from flask import Flask
import threading
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Salut ! 👋 Bienvenue chez Aroma Cloud !\nTape /help pour voir ce que je peux faire.")

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text("Je suis le bot Aroma ! 🌸\n- /start pour commencer\n- Envoie ton parfum préféré !")

def handle_message(update: Update, context: CallbackContext):
    text = update.message.text
    update.message.reply_text(f"Tu as dit : {text} 😊\nMerci pour ton message chez Aroma !")

def run_bot():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    updater.start_polling()
    updater.idle()

@app.route('/')
def home():
    return "Aroma Bot est en ligne !"

if __name__ == '__main__':
    threading.Thread(target=run_bot).start()
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))