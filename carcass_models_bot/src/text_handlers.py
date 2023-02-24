from src.bot_creation import *


@bot.message_handler(content_types=["text"])
def conversation(message) -> None:
    # Если пользователь новый и пытается что-то написать - говорим ему написать /start
    if not user_exist(message.chat.id):
        bot.send_message(message.chat.id, NOT_REGISTERED_MESSAGE)
        return

    if check_step(message.chat.id) == MENU_STEP:
        if message.text == LOOK_BUTTON:
            scroll_message_id = select_from_db(
                "users", "scroll_message_id", "id", message.chat.id
            )[0]
            if scroll_message_id:
                try:
                    bot.delete_message(
                        chat_id=message.chat.id,
                        message_id=scroll_message_id,
                    )
                except Exception as e:
                    print(type(e))
                    # обработать
            available_models = show_models()
            if not available_models:
                scroll_message = bot.send_message(
                    message.chat.id,
                    ZERO_MODELS_MESSAGE,
                    reply_markup=menu_markup,
                )
            else:
                scroll_message = bot.send_photo(
                    chat_id=message.chat.id,
                    photo=available_models[0][4],
                    caption=f"Модель №: {available_models[0][0]}\nНазвание модели: {available_models[0][1]}\nОписание модели: {available_models[0][2]}\n\n"
                    + f"Цена: <b>{available_models[0][3]}</b>",
                    reply_markup=scroll_one_inline_markup
                    if len(available_models) == 1
                    else scroll_right_inline_markup,
                    parse_mode="HTML",
                )
            update_db(
                "users", "scroll_message_id", scroll_message.id, "id", message.chat.id
            )
            conn.commit()
            insert_step("MENU", message.chat.id)

        else:
            bot.send_message(
                message.chat.id,
                DO_NOT_KNOW_THE_COMMAND_MESSAGE,
                reply_markup=menu_markup,
            )
    # TODO
    elif check_step(message.chat.id) == "OTHER":
        pass
    else:
        pass


@bot.callback_query_handler(func=lambda call: call.data.startswith("scroll_"))
def scroll_callback(call) -> None:
    # Если пользователь новый и пытается что-то написать - говорим ему написать /start
    if not user_exist(call.message.chat.id):
        bot.send_message(call.message.chat.id, NOT_REGISTERED_MESSAGE)
        return

    available_models = show_models()
    current_model_id = call.message.caption.split(": ")[1].split("\n")[0]
    print(current_model_id)
    position = search_id(available_models, current_model_id)
    print(position)

    if call.data == "scroll_right":
        if overdue_scroll_handler(call):
            return
        scroll_handler(
            call, available_models, int(position) + 1, 1, scroll_left_inline_markup
        )
    elif call.data == "scroll_delete":
        bot.send_message(call.message.chat.id, "Фукнция скоро будет готова.")
    elif call.data == "scroll_left":
        if overdue_scroll_handler(call):
            return
        scroll_handler(
            call,
            available_models,
            int(position) - 1,
            len(available_models),
            scroll_right_inline_markup,
        )
    else:
        pass


def scroll_handler(call, available_models, position, length, markup):
    bot.edit_message_media(
        chat_id=call.message.chat.id,
        message_id=call.message.id,
        media=telebot.types.InputMediaPhoto(
            media=available_models[position][4],
            caption=f"Модель №: {available_models[position][0]}\nНазвание модели: {available_models[position][1]}\nОписание модели: {available_models[position][2]}\n\n"
            + f"Цена: <b>{available_models[position][3]}</b>",
            parse_mode="HTML",
        ),
        reply_markup=markup
        if position == len(available_models) - length
        else scroll_mid_inline_markup,
    )


def search_id(available_models: list, search_value: str) -> str:
    for index, item in enumerate(available_models):
        if item[0] == search_value:
            return index


def overdue_scroll_handler(call):
    temp = too_old(user_id=call.message.chat.id, call_message_id=call.message.id)
    if temp:
        bot.send_message(
            call.message.chat.id, SCROLL_IS_TOO_OLD, reply_markup=menu_markup
        )
    return temp
