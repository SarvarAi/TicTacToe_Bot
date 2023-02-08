from aiogram.dispatcher.filters.state import State, StatesGroup


class MemoryName(StatesGroup):
    username1 = State()
    username2 = State()
    game1 = State()
    game2 = State()
    coordinates = State()
