from django.core.management.base import BaseCommand
from botapp.bot import run_bot

class Command(BaseCommand):
    help = 'Run the Telegram bot'

    def handle(self, *args, **options):
        run_bot()