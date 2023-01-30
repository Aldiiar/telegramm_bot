from aiogram import types
from handlers import constans
from config import bot
import asyncio
import aioschedule

async def remind_command(message: types.Message):
    '''
    Функция для добавления напоминалки
    '''
    await message.answer(text=constans.REMIND_BOT)

async def schedule_command(message: types.Message):
    '''
    Функция для добавления напоминалки
    '''
    global chat_id
    chat_id = message.from_user.id
    await message.answer(text='okay')

async def notice():
    '''
    функция срезает слово напомни
    '''
    await bot.send_message(
        chat_id=chat_id,
        text='hello bro'
    )

async def schedule():
    aioschedule.every(15).seconds.do(notice)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)