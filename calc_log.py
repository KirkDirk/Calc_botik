from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime

def logging(update: Update, context: CallbackContext):
    with open("logs.csv", "a", encoding = "UTF-8") as file:
        file.write(f"{datetime.datetime.now().time()},{update.effective_user.first_name},{update.effective_user.id}, {update.message.text}\n")