from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):
    phone = State()
    mail = State()
    message = State()
    submit = State()
