# Программа для телеграмм-бота с функцией калькулятора

from telegram import Update
from telegram.ext import Updater, CommandHandler
from calc_def import *


with open("token.txt", "r", encoding = "UTF-8") as num_token:
    token = num_token.read()

updater = Updater(token, use_context=True)
updater.dispatcher.add_handler(CommandHandler('start', start_def))
updater.dispatcher.add_handler(CommandHandler('help', help_def))
updater.dispatcher.add_handler(CommandHandler('sum', sum_def))
updater.dispatcher.add_handler(CommandHandler('raz', raz_def))
updater.dispatcher.add_handler(CommandHandler('umn', umn_def))
updater.dispatcher.add_handler(CommandHandler('del', del_def))

updater.start_polling()