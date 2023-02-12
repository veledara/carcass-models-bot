from src.bot import telebot
from src.messages import *

# menu keyboard
menu_markup = telebot.types.ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True
)
look_button = telebot.types.InlineKeyboardButton(text=LOOK_BUTTON)
menu_markup.add(look_button)

# scroll keyboard
scroll_right_inline_markup = telebot.types.InlineKeyboardMarkup()
scroll_mid_inline_markup = telebot.types.InlineKeyboardMarkup()
scroll_left_inline_markup = telebot.types.InlineKeyboardMarkup()
scroll_one_inline_markup = telebot.types.InlineKeyboardMarkup()

left_button = telebot.types.InlineKeyboardButton(
    text=LEFT_BUTTON, callback_data="scroll_left"
)
delete_button = telebot.types.InlineKeyboardButton(
    text=DELETE_BUTTON, callback_data="scroll_delete"
)
right_button = telebot.types.InlineKeyboardButton(
    text=RIGHT_BUTTON, callback_data="scroll_right"
)

scroll_right_inline_markup.add(delete_button, right_button)
scroll_mid_inline_markup.add(left_button, delete_button, right_button)
scroll_left_inline_markup.add(left_button, delete_button)
scroll_one_inline_markup.add(delete_button)
