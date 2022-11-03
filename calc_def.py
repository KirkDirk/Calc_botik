from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from calc_log import *

def start_def(update: Update, context: CallbackContext):
    logging(update, context)
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="""Я - бот, умею в калькулятор.
Чтобы что-то посчитать, выбери команду и добавть два числа через пробел.
""")    

def help_def(update: Update, context: CallbackContext):
    logging(update, context)
    update.message.reply_text(f"Доступные команды:\n/start\n/sum\n/raz\n/umn\n/del\n/help\n")

def sum_def(update: Update, context: CallbackContext):
    logging(update, context)
    calc = update.message.text.split()
    one_calc = int(calc[1])
    two_calc = int(calc[2])
    update.message.reply_text(f"{one_calc} + {two_calc} = {one_calc+two_calc}")

def raz_def(update: Update, context: CallbackContext):
    logging(update, context)
    calc = update.message.text.split()
    one_calc = int(calc[1])
    two_calc = int(calc[2])
    update.message.reply_text(f"{one_calc} - {two_calc} = {one_calc-two_calc}")

def umn_def(update: Update, context: CallbackContext):
    logging(update, context)
    calc = update.message.text.split()
    one_calc = int(calc[1])
    two_calc = int(calc[2])
    update.message.reply_text(f"{one_calc} * {two_calc} = {one_calc*two_calc}")

def del_def(update: Update, context: CallbackContext):
    logging(update, context)
    calc = update.message.text.split()
    one_calc = int(calc[1])
    two_calc = int(calc[2])
    update.message.reply_text(f"{one_calc} / {two_calc} = {one_calc/two_calc}")