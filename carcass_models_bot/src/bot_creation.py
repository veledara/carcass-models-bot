import telebot
from src.config import TOKEN
from src.messages import *
from src.keyboards import *
from src.db_functions import *

bot = telebot.TeleBot(TOKEN)
print(bot.get_me())

