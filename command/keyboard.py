from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

memory_cor = {
              "A1": 0,
              "A2": 0,
              "A3": 0,
              "B1": 0,
              "B2": 0,
              "B3": 0,
              "C1": 0,
              "C2": 0,
              "C3": 0
              }

default_coordinates = {
              "A1": 0,
              "A2": 0,
              "A3": 0,
              "B1": 0,
              "B2": 0,
              "B3": 0,
              "C1": 0,
              "C2": 0,
              "C3": 0
              }


def menu_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    start = KeyboardButton(text="🧮 Start game!")
    history = KeyboardButton(text="📝 History")
    return markup.add(start, history)


def start_game():
    markup = InlineKeyboardMarkup()
    start = InlineKeyboardButton(text="Start Game", callback_data="starting_game")
    return markup.add(start)


def board(cor=None, turn=None):
    markup = InlineKeyboardMarkup()
    btns = []

    memory_cor[cor] = turn
    for key, value in memory_cor.items():
        if value == 1:
            btn = InlineKeyboardButton(text="❌", callback_data=key)
            btns.append(btn)
        elif key == "starting_game" and value == 2:
            pass
        elif value == 2:
            btn = InlineKeyboardButton(text="⭕", callback_data=key)
            btns.append(btn)
        elif value == 0:
            btn = InlineKeyboardButton(text=" ", callback_data=key)
            btns.append(btn)

    return markup.add(*btns)
