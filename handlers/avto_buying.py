from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


car_kb = InlineKeyboardMarkup()
car_kb.add(InlineKeyboardButton('Купить', callback_data='car_buy'))

async def car_c(message: types.Message):
    '''
    СПИСОК АBTО
    '''
    await message.answer(text='Все автомобили класса -С-')
    await message.answer_photo((open('images/6ff264as-960.jpg', 'rb')), caption='Авто №1',
                               reply_markup=car_kb)
    await message.answer_photo((open('images/hqdefault.jpg', 'rb')), caption='Авто №2',
                               reply_markup=car_kb)


async def car_e(message: types.Message):
    '''
    СПИСОК АBTО
    '''
    await message.answer(text='Все автомобили класса -E-')
    await message.answer_photo((open('images/e124.jpg', 'rb')), caption='Авто №1',
                               reply_markup=car_kb)
    await message.answer_photo((open('images/e140.jpg', 'rb')), caption='Авто №2',
                               reply_markup=car_kb)


async def car_s(message: types.Message):
    '''
    СПИСОК АBTО
    '''
    await message.answer(text='Все автомобили класса -S-')
    await message.answer_photo((open('images/mazda.jpeg', 'rb')), caption='Авто №1',
                               reply_markup=car_kb)
    await message.answer_photo((open('images/sub.jpg', 'rb')), caption='Авто №2',
                               reply_markup=car_kb)