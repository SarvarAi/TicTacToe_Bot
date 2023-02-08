from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from data.loader import dp, bot
from . import keyboard
from .ram import MemoryName


# START of bot
@dp.message_handler(commands=["start"])
async def start(message: Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id=chat_id,
                           text="Welcome to the Tic-Tac-Toe bot 😁",
                           reply_markup=keyboard.menu_keyboard())


# Asking first username
@dp.message_handler(regexp="🧮 Start game!")
async def start_game(message: Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id=chat_id,
                           text="Enter the first user name 👤: ",
                           reply_markup=ReplyKeyboardRemove())
    await MemoryName.username1.set()


# Saving the name of the first username and asking the second username
@dp.message_handler(state=MemoryName.username1)
async def star_entering_username(message: Message, state: FSMContext):
    name1 = message.text
    async with state.proxy() as data:
        data["username1"] = name1
    await message.answer("Enter the second user name 👤: ")
    await MemoryName.username2.set()
    

# saving the name of the second username and starting game with button 'Lets start our game 🔆'
@dp.message_handler(state=MemoryName.username2)
async def entering_username(message: Message, state: FSMContext):
    name2 = message.text
    async with state.proxy() as data:
        data["username2"] = name2
    await message.answer("Lets start our game 🔆", reply_markup=keyboard.start_game())
    await MemoryName.game1.set()
