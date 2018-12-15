from db_handler import SQLiteDB
from configparser import ConfigParser
from bot_handler import TelegramBot
from user_handler import TelegramUser


class MessageHandler:
    def __init__(self):
        self.cfg = self.parse_config()
        self.db = SQLiteDB()
        self.bot = TelegramBot(self.cfg['BotToken'], self.cfg['UserId'])
        self.user = TelegramUser()

    def parse_config(self, filename='config.ini'):
        cfg = ConfigParser()
        return cfg.read(filename)['Security']

    def mainloop(self):
        ...