from aiogram import Bot, Dispatcher, executor
from dotenv import load_dotenv
from os import getenv
from aiogram.dispatcher.filters import Text

'''импорт функций'''
from handlers.answer import qwerty
from handlers.start import start_command
from handlers.buy import buy_command
from handlers.sell import sell_command
from handlers.avto_buying import car_c
from handlers.avto_buying import car_e
from handlers.avto_buying import car_s


load_dotenv()
bot = Bot(getenv('BOT_TOKEN'))
dp = Dispatcher(bot)


dp.register_message_handler(start_command, commands=['start'])
dp.register_callback_query_handler(buy_command, text='buy_command')
dp.register_callback_query_handler(sell_command, text='sell_command')
dp.register_message_handler(car_c, Text(equals='C class'))
dp.register_message_handler(car_e, Text(equals='E class'))
dp.register_message_handler(car_s, Text(equals='S class'))
dp.register_message_handler(qwerty)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

