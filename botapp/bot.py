import os
import django
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from decouple import config

# Django setup
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from botapp.models import TelegramUser

BOT_TOKEN = config('BOT_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    TelegramUser.objects.get_or_create(
        user_id=user.id,
        default={
            'username': user.username,
            'first_name': user.first_name,
        }
    )
    await update.message.reply_text("👋 Hello! You're now connected to Django!")

def run_bot():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    app.run_polling()