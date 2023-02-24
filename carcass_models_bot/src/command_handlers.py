from src.bot_creation import *


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
