import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import random
import sqlite3 as sql


db = r"carcass_models_bot\databases\carcass_models.db"
conn = sql.connect(db, check_same_thread=False)
c = conn.cursor()

root = tk.Tk()
root.title("Model Adder")
root.geometry("250x218")
root.resizable(False, False)


def generate_id() -> str:
    return str(random.randint(100000000, 999999999))


def choose_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.png")])
    file_path_label.config(text=file_path)
    return file_path


# Function to insert the data into the database
def insert_data():
    image_path = file_path_label.cget("text")
    model_id = generate_id()
    name = str(name_entry.get())
    description = str(description_entry.get())
    price = str(price_entry.get())

    if image_path == "" or name == "" or description == "" or price == "":
        messagebox.showerror("Error", "Not all fields are filled!")
        return

    with open(image_path, "rb") as image:
        image_data = image.read()
        pic = sql.Binary(image_data)
        c.execute(
            f"INSERT INTO models (id, name, description, price, picture) VALUES('{model_id}', '{name}', '{description}', '{price}', '{pic}')"
        )
        conn.commit()
        messagebox.showinfo("Success", "Data successfully inserted into the database")
        name_entry.delete(0, tk.END)


# GUI components
name_label = tk.Label(root, text="Enter model name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

description_label = tk.Label(root, text="Enter model description:")
description_label.pack()
description_entry = tk.Entry(root)
description_entry.pack()

price_label = tk.Label(root, text="Enter model price:")
price_label.pack()
price_entry = tk.Entry(root)
price_entry.pack()


image_label = tk.Label(root, text="Choose an Image:")
image_label.pack()
browse_button = tk.Button(root, text="Browse", command=choose_file)
browse_button.pack()
file_path_label = tk.Label(root, text="")
file_path_label.pack()


submit_button = tk.Button(root, text="Add to database", command=insert_data)
submit_button.pack()

# Run the GUI
root.mainloop()

if __name__ == "__main__":
    pass
