import re

from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from sqlalchemy.util import await_fallback

from State.form import Form
from State.lib import next_state
from config import bot, ADMIN_ID


def is_valid_phone(phone: str) -> bool:
    pattern = r"^\+?[78]\d{10}$"  # Формат +79991234567 или 89991234567
    return re.match(pattern, phone) is not None

def is_valid_email(email: str) -> bool:
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None


async def message_state_phone(message: types.Message, state: FSMContext):
    await state.update_data({"name": message.text})
    await state.set_state(await next_state(await state.get_state(), Form))
    await message.answer("Ввудите номер телефона")


async def message_state_mail(message: types.Message, state: FSMContext):
    if is_valid_phone(message.text):
        await state.update_data({"phone": message.text})
        await state.set_state(await next_state(await state.get_state(), Form))

        keyboard = ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="Пропустить")]],
            resize_keyboard=True,
            one_time_keyboard=True
        )

        await message.answer("Ввудите почту", reply_markup=keyboard)
    else:
        await message.answer("❌ Неверный формат номера! Введите в формате +79991234567 или 89991234567.")


async def message_state_message(message: types.Message, state: FSMContext):
    if is_valid_email(message.text) or message.text == "Пропустить":
        await state.update_data({"mail": message.text})
        await state.set_state(await next_state(await state.get_state(), Form))

        keyboard = ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="Пропустить")]],
            resize_keyboard=True,
            one_time_keyboard=True
        )

        await message.answer("Ввудите дополнительное сообщениче", reply_markup=keyboard)
    else:
        await message.answer("❌ Неверный формат почты! Введите корректный email (например, user@example.com).")

async def message_submit(message: types.Message, state: FSMContext):
    # await state.clear()
    user_data = await state.get_data()
    print(user_data)
    await bot.send_message("1028962949", f"Пользователь @{message.from_user.username} оставил заявку \nФИО: {user_data.get('name')},\nТелефон: {user_data.get('phone')},\nПочта: {user_data.get('mail')},\nДополнительное сооющение: {message.text}")
    await message.answer("Заявка отправлена! В скором времения с вами свяжется менеджер.", reply_markup=types.ReplyKeyboardRemove())
