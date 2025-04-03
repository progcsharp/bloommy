from aiogram import Dispatcher

from State.form import Form
from handler.message import message_state_message, message_state_mail, message_state_phone, message_submit


async def register_handlers_message(dp: Dispatcher):
    dp.message.register(message_state_phone, Form.phone)
    dp.message.register(message_state_mail, Form.mail)
    dp.message.register(message_state_message, Form.message)
    dp.message.register(message_submit, Form.submit)
