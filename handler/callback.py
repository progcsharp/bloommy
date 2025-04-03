from aiogram import types
from aiogram.fsm.context import FSMContext

from State.form import Form


async def call_quiz_start(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(Form.phone)
    await call.message.answer("Введите свое ФИО")



