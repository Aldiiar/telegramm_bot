from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


car_kb = InlineKeyboardMarkup()
car_kb.add(InlineKeyboardButton('Купить', callback_data='car_buy'))

async def car_c(message: types.Message):
    '''
    СПИСОК АBTО
    '''
    photo1 = open('images/6ff264as-960.jpg', 'rb')
    photo2 = open('images/hqdefault.jpg', 'rb')
    await message.answer(text='Все автомобили класса -С-')
    await message.answer_photo(photo1)
    await message.answer(text='Авто №1', reply_markup=car_kb)
    await message.answer_photo(photo2)
    await message.answer(text='Авто №2', reply_markup=car_kb)


async def car_e(message: types.Message):
    '''
    СПИСОК АBTО
    '''
    photo3 = open('images/e124.jpg', 'rb')
    photo4 = open('images/e140.jpg', 'rb')
    await message.answer(text='Все автомобили класса -E-')
    await message.answer_photo(photo3)
    await message.answer(text='Авто №1', reply_markup=car_kb)
    await message.answer_photo(photo4)
    await message.answer(text='Авто №2', reply_markup=car_kb)


async def car_s(message: types.Message):
    '''
    СПИСОК АBTО
    '''
    photo5 = open('images/mazda.jpeg', 'rb')
    photo6 = open('images/sub.jpg', 'rb')
    await message.answer(text='Все автомобили класса -S-')
    await message.answer_photo(photo5)
    await message.answer(text='Авто №1', reply_markup=car_kb)
    await message.answer_photo(photo6)
    await message.answer(text='Авто №2', reply_markup=car_kb)

