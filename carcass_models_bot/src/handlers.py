import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.bot import bot
from src.config import ADMIN
from src.messages import *
from src.keyboards import *
from src.db_functions import *


@bot.message_handler(commands=["start"])
def welcome(message) -> None:
    # Если пользователь новый - регистрируем его
    if not user_exist(message.chat.id):
        create_user(message.chat.id, message.from_user.username)
        bot.send_message(message.chat.id, WELCOME_MESSAGE, reply_markup=menu_markup)
    else:
        bot.send_message(
            message.chat.id, ALREADY_REGISTERED_MESSAGE, reply_markup=menu_markup
        )
        insert_step(MENU_STEP, message.chat.id)


@bot.message_handler(commands=["help"])
def help(message) -> None:
    # Если пользователь новый и пытается что-то написать - говорим ему написать /start
    if not user_exist(message.chat.id):
        bot.send_message(message.chat.id, NOT_REGISTERED_MESSAGE)
        return

    bot.send_message(message.chat.id, HELP_MESSAGE, reply_markup=menu_markup)
    insert_step(MENU_STEP, message.chat.id)


@bot.message_handler(content_types=["text"])
def conversation(message) -> None:
    # Если пользователь новый и пытается что-то написать - говорим ему написать /start
    if not user_exist(message.chat.id):
        bot.send_message(message.chat.id, NOT_REGISTERED_MESSAGE)
        return

    if check_step(message.chat.id) == MENU_STEP:
        if message.text == LOOK_BUTTON:
            bot.send_message(message.chat.id, "ее")
        else:
            bot.send_message(
                message.chat.id,
                DO_NOT_KNOW_THE_COMMAND_MESSAGE,
                reply_markup=menu_markup,
            )
    # TODO
    elif check_step(message) == "OTHER":
        pass
    else:
        pass


@bot.callback_query_handler(func=lambda call: call.data.startswith("scroll_"))
def scroll_callback(call) -> None:
    # Если пользователь новый и пытается что-то написать - говорим ему написать /start
    if not user_exist(call.message):
        bot.send_message(call.message.chat.id, NOT_REGISTERED_MESSAGE)
        return


if __name__ == "__main__":
    bot.polling(none_stop=True)
