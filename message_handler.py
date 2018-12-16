from db_handler import SQLiteDB
from configparser import ConfigParser
from bot_handler import TelegramBot
from user_handler import TelegramUser

from time import time, sleep
import asyncio

class MessagesHandler:
    def __init__(self):
        self.cfg = self.parse_config()
        self.db = SQLiteDB()
        self.bot = TelegramBot(self.cfg['BotToken'], self.cfg['UserId'])
        self.user = TelegramUser(self.message_handler, self.cfg)

    @staticmethod
    def parse_config(filename='config.ini'):
        cfg = ConfigParser()
        cfg.read(filename)
        return cfg['Security']

    @staticmethod
    def parse_message(msg):
        timestamp = int(time())
        user_id = int(msg.chat.id)
        msg_id = int(msg.message_id)
        data = {
            'text': msg.text,
        }
        if msg.photo:
            data['photo'] = True
        if msg.audio:
            data['audio'] = True
        if msg.document:
            data['document'] = True
        if msg.voice:
            data['voice'] = True
        return {
            'timestamp': timestamp,
            'user_id': user_id,
            'msg_id': msg_id,
            'data': str(data),
        }

    def message_handler(self, client, message):
        msg_parsed = self.parse_message(message)
        self.db.add_entry(
            msg_parsed['timestamp'],
            msg_parsed['user_id'],
            msg_parsed['msg_id'],
            msg_parsed['data']
        )
        print('adding msg to db')

    def check_all(self):
        timestamp_ref = int(time()) - 48 * 3600
        self.db.remove_old(timestamp_ref)
        all_msgs = self.db.get_all()
        breakpoint()

    def mainloop(self):
        self.check_all()

if __name__ == '__main__':
    m = MessagesHandler()
    m.mainloop()