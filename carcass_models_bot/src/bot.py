import telebot
from src.config import TOKEN

bot = telebot.TeleBot(TOKEN)
print(bot.get_me())