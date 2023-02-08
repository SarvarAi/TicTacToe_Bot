from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext
from . import keyboard
from data.loader import dp, bot
from .ram import MemoryName

player_cor = []


@dp.callback_query_handler(lambda call: call.data == "starting_game" or
                                        call.data == "A1" or
                                        call.data == "A2" or
                                        call.data == "A3" or
                                        call.data == "B1" or
                                        call.data == "B2" or
                                        call.data == "B3" or
                                        call.data == "C1" or
                                        call.data == "C2" or
                                        call.data == "C3" in call.data, state=MemoryName.game1)
async def start_game(call: CallbackQuery, state: FSMContext):
    chat_id = call.message.chat.id
    try:
        message_id = call.message.message_id
        cor = call.data
        turn = 2

        data = await state.get_data()
        username1 = data["username1"]
        username2 = data["username2"]

        player_cor.append(cor)

        await bot.edit_message_text(chat_id=chat_id,
                                    message_id=message_id,
                                    text=f"Now It is {username1}'s turn (❌)",
                                    reply_markup=keyboard.board(cor=cor, turn=turn))

        winner = await is_winner(keyboard.memory_cor)
        if winner == 1:
            await bot.send_message(chat_id=chat_id,
                                   text=f"🥳Congratulations {username1} is winner🥳",
                                   reply_markup=keyboard.menu_keyboard())
            await bot.delete_message(message_id=message_id, chat_id=chat_id)
            keyboard.memory_cor = keyboard.default_coordinates
            await state.reset_data()
            await state.finish()
        elif winner == 2:
            await bot.send_message(chat_id=chat_id,
                                   text=f"🥳Congratulations {username2} is winner🥳",
                                   reply_markup=keyboard.menu_keyboard())
            await bot.delete_message(message_id=message_id, chat_id=chat_id)
            keyboard.memory_cor = keyboard.default_coordinates
            await state.reset_data()
            await state.finish()
        else:
            await MemoryName.game2.set()
    except:
        await bot.send_message(chat_id=chat_id, text="Wow do not do this again!😳")
        await MemoryName.game2.set()


@dp.callback_query_handler(lambda call: call.data == "A1" or
                                        call.data == "A2" or
                                        call.data == "A3" or
                                        call.data == "B1" or
                                        call.data == "B2" or
                                        call.data == "B3" or
                                        call.data == "C1" or
                                        call.data == "C2" or
                                        call.data == "C3" in call.data, state=MemoryName.game2)
async def user2_turn(call: CallbackQuery, state: FSMContext):
    chat_id = call.message.chat.id
    try:
        message_id = call.message.message_id
        cor = call.data
        turn = 1

        data = await state.get_data()
        username2 = data["username2"]
        username1 = data["username1"]

        player_cor.append(cor)

        await bot.edit_message_text(chat_id=chat_id,
                                    message_id=message_id,
                                    text=f"Now It is {username2}'s turn (⭕)",
                                    reply_markup=keyboard.board(cor=cor, turn=turn))

        winner = await is_winner(keyboard.memory_cor)

        if winner == 1:
            await bot.send_message(chat_id=chat_id,
                                   text=f"🥳Congratulations {username1} is winner🥳",
                                   reply_markup=keyboard.menu_keyboard())
            await bot.delete_message(message_id=message_id, chat_id=chat_id)
            keyboard.memory_cor = {
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
            await state.reset_data()
            await state.finish()

        elif winner == 2:
            await bot.send_message(chat_id=chat_id,
                                   text=f"🥳Congratulations {username2} is winner🥳",
                                   reply_markup=keyboard.menu_keyboard())
            await bot.delete_message(message_id=message_id, chat_id=chat_id)
            keyboard.memory_cor = {
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
            await state.reset_data()
            await state.finish()
        else:
            await MemoryName.game1.set()
    except:
        await bot.send_message(chat_id=chat_id, text="Wow do not do this again!😳")
        await MemoryName.game1.set()


async def is_winner(board):
    board = [
        [board["A1"], board["A2"], board["A3"]],
        [board["B1"], board["B2"], board["B3"]],
        [board["C1"], board["C2"], board["C3"]]
    ]

    for i in range(0, 3):
        if board[i][0] == board[i][1] == board[i][2] != 0:
            return board[i][0]
        elif board[0][i] == board[1][i] == board[2][i] != 0:
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != 0:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] != 0:
        return board[0][0]

    elif 0 not in board[0] and 0 not in board[1] and 0 not in board[2]:
        return 0
    else:
        return -1
