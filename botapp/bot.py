import os
import django
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext
from decouple import config
from asgiref.sync import sync_to_async

# Django setup
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from botapp.models import TelegramUser

BOT_TOKEN = config('BOT_TOKEN')

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user = update.message.from_user
#     TelegramUser.objects.get_or_create(
#         user_id=user.id,
#         defaults={
#             'username': user.username,
#             'first_name': user.first_name,
#         }
#     )
#     await update.message.reply_text("👋 Hello! You're now connected to Django!")

@sync_to_async
def get_or_create_user(user):
    TelegramUser.objects.get_or_create(
        user_id=user.id,
        defaults={
            'username': user.username,
            'first_name': user.first_name,
        }
    )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    await get_or_create_user(user)
    await update.message.reply_text(f"👋 Hello, {user.first_name}! You're now connected to Django!")
    text = (
        f"🧾 User Info:\n"
        f"ID: {user.id}\n"
        f"Username: @{user.username}\n"
        f"Name: {user.first_name} {user.last_name or ''}\n"
        f"Language: {user.language_code}\n"
        f"Premium: {user.is_premium}\n"
    )
    await update.message.reply_text(text)

def run_bot():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    app.run_polling()