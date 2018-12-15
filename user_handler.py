from configparser import ConfigParser
from pyrogram import Client, MessageHandler
from pyrogram.client.methods.messages import GetMessages


class TelegramUser:
    def __init__(self, callback, cfg):
        self.app = self.login(cfg)
        self.app.add_handler(MessageHandler(callback))
        self.app.run()

    @staticmethod
    def login(cfg_):
        app = Client(
                'cl',
                api_hash=cfg_['ApiHash'],
                api_id=cfg_['ApiId'],
                phone_number=cfg_['Phone'])
        return app


if __name__ == '__main__':
    t = TelegramUser()
    import pdb; pdb.set_trace();
