from aiogram import types
from handlers import constans
from config import bot
import asyncio
import aioschedule

async def remind_command(message: types.Message):
    '''
    Функция для добавления напоминалки
    '''
    global chat_id
    chat_id = message.from_user.id
    await message.answer(text=constans.REMIND_BOT)

async def notice(message: types.Message):
    '''
    функция срезает слово напомни
    '''
    await bot.send_message(
        chat_id=chat_id,
        text=message.text[8:]
    )

async def schedule(message: types.Message):
    if message.text.lower().split()[0] == 'напомни':
        aioschedule.every(10).seconds.do(notice)

        while True:
            await aioschedule.run_pending()
            await asyncio.sleep(1)