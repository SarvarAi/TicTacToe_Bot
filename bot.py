from aiogram import executor
from data.loader import dp

import command

if __name__ == '__main__':
    executor.start_polling(dp)