from aiogram import types

async def sell_command(cb: types.CallbackQuery):
    '''
    Функция для того, чтобы пользователь продал авто
    '''
    await cb.bot.send_message(
        chat_id=cb.from_user.id,
        text='Этот переход ещё не готов, пока что можете только купить авто'
    )