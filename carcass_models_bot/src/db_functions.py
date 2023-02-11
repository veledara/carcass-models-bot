import random
import time
import sqlite3 as sql


db = r"carcass_models_bot\databases\carcass_models.db"
conn = sql.connect(db, check_same_thread=False)
c = conn.cursor()


# Фукнция, генерирующая айди проблемы и совета
def generate_id() -> str:
    # return str(uuid.uuid4())
    return str(random.randint(100000000, 999999999))


# Фукнция, возвращающая шаг, на котором сейчас находится пользователь
def check_step(user_id: str) -> str:
    c.execute(f"SELECT step FROM users WHERE id = '{user_id}'")
    result = c.fetchone()[0]
    return result


# Фукнция, меняющая шаг, на котором сейчас находится пользователь
def insert_step(n: str, user_id) -> None:
    c.execute(f"UPDATE users SET step = '{n}' WHERE id = '{user_id}'")
    conn.commit()


# Фукнция, проверяющая есть ли пользователь в базе данных
def user_exist(user_id: str) -> bool:
    c.execute(f"SELECT id FROM users WHERE id = '{user_id}'")
    exist = c.fetchone()
    return exist


# Фукнция, создающая пользователя в базе данных
def create_user(user_id: str, tg_username: str) -> None:
    now = int(time.time())
    c.execute(
        f"INSERT INTO users (id, step, tg_username, join_time) VALUES('{user_id}', 'MENU', '{tg_username}', '{now}')"
    )
    conn.commit()


# Фукнция, выбираюая значение из база данных
def select_from_db(
    table: str, value_to_select: str, where_column: str, where_value: str
) -> list:
    c.execute(
        f"SELECT {value_to_select} FROM {table} WHERE {where_column} = '{where_value}'"
    )
    result = c.fetchone()
    return result
