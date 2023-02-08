import sqlite3
import os
import datetime

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


class ConnectToDatabase:
    """
    Подключение к базе данных
    """

    def __init__(self):
        self.database_path = os.path.join(BASE_DIR, 'users.db')
        self.database = sqlite3.connect(self.database_path)
        self.cursor = self.database.cursor()
        self.commit = self.database.commit
        self.close = self.database.close


class CreatingUsersTable(ConnectToDatabase):
    """
    Создание таблиц в базе данных пользователей
    """

    def __init__(self):
        super().__init__()

    def creating_table_all_games(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS all_games (
        game_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_player_id TEXT NOT NULL,
        firs_player_name TEXT NOT NULL,
        second_player_id TEXT NOT NULL,
        second_player_name TEXT NOT NULL,
        start_of_the_game DATETIME NOT NULL,
        end_of_the_game DATETIME,
        winnerTEXT
        );''')
        self.commit()
        self.close()
