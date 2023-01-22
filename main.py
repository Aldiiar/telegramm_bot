from aiogram import Bot, Dispatcher, executor
from dotenv import load_dotenv
from os import getenv
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage

'''импорт функций'''
from handlers.answer import qwerty
from handlers.start import start_command
from handlers.buy import buy_command
from handlers.sell import sell_command
from handlers.avto_buying import car_c, car_e, car_s

'''импорт функций формы'''
from handlers.sell import Form
from handlers.sell import cancel_handler
from handlers.sell import (
    form_start,
    name_process,
    phone_number_process,
    car_brand_process,
    car_price_process,
    address_process
)


load_dotenv()
bot = Bot(getenv('BOT_TOKEN'))
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


dp.register_message_handler(start_command, commands=['start'])
dp.register_callback_query_handler(buy_command, text='buy_command')
dp.register_message_handler(car_c, Text(equals='C class'))
dp.register_message_handler(car_e, Text(equals='E class'))
dp.register_message_handler(car_s, Text(equals='S class'))
dp.register_callback_query_handler(sell_command, text='sell_command')
dp.register_message_handler(form_start, commands=['form'])
dp.register_message_handler(cancel_handler, state='*', commands='cancel')
dp.register_message_handler(cancel_handler, Text(equals='cancel', ignore_case=True), state='*')
dp.register_message_handler(name_process, state=Form.name)
dp.register_message_handler(phone_number_process, state=Form.phone_number)
dp.register_message_handler(car_brand_process, state=Form.car_brand)
dp.register_message_handler(car_price_process, state=Form.car_price)
dp.register_message_handler(address_process, state=Form.address)
dp.register_message_handler(qwerty)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)