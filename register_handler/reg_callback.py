from aiogram import Dispatcher, F

from handler.callback import call_quiz_start


async def register_handlers_callback(dp: Dispatcher):
    dp.callback_query.register(call_quiz_start, F.data == 'quiz')
