from src.bot import telebot
from src.messages import *

menu_markup = telebot.types.ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True
)
look_button = telebot.types.InlineKeyboardButton(text=LOOK_BUTTON)
menu_markup.add(look_button)
