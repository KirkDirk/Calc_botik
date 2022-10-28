# Программа для телеграмм-бота с функцией калькулятора

# from telegram.ext import Updater

with open("HWtask027/token.txt", "r", encoding = "UTF-8") as num_token:
    token = num_token.read()

# получаем экземпляр `Updater`
# updater = Updater(token, use_context=True)
# получаем экземпляр `Dispatcher`
# dispatcher = updater.dispatcher