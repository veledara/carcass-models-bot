import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.command_handlers import *
from src.text_handlers import *


if __name__ == "__main__":
    bot.polling(none_stop=True)
