import sqlite3 as sql


def clear_table(database_path: str, table_name: str) -> None:
    conn = sql.connect(database_path)
    c = conn.cursor()
    c.execute(f"DELETE FROM {table_name};")
    conn.commit()
    conn.close()


if __name__ == "__main__":
    clear_table(r"carcass_models_bot\databases\carcass_models.db", "users")
    # clear_table(r"carcass_models_bot\databases\carcass_models.db", "models")
