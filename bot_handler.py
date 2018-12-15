from telegram.ext import Updater, CommandHandler


class TelegramBot:

    def __init__(self, token, user_id):
        self.user_id = user_id
        self.upd = Updater(token)
        self.dp = self.upd.dispatcher

    def send_message(self, text):
        self.upd.bot.send_message(self.user_id, text)


