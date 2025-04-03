from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

from db.handler.create import create_user
from db.handler.get import get_user_by_tg_id


async def cmd_start(message: types.Message):
    # Проверяем и создаем пользователя при необходимости
    if await get_user_by_tg_id(message.from_user.id):
        await create_user(tg_id=message.from_user.id, nickname=message.from_user.username)

    # Создаем кнопку
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="✨ Узнать больше",
        callback_data="quiz")
    )

    # Форматированное приветственное сообщение
    welcome_text = """
<b>🌸 Привет, я Bloommy!</b>

Добро пожаловать в <b>Bloommy</b> — конструктор магазина в формате веб-бота для Telegram, созданный специально для <b>цветочных и подарочных магазинов</b>.

С <b>Bloommy</b> ты можешь:
✅ <b>Легко настроить</b> и запустить свой Telegram-магазин
✅ Сделать его <b>удобным для клиентов</b>
✅ <b>Автоматизировать</b> процесс продаж

<b>🚀 Доступные команды:</b>

🔹 /demo — посмотри <b>демо-версию</b> и возможности сервиса
🔹 /info — узнай <b>как настроить</b> свой магазин
🔹 /tariff — выбери <b>подходящий тарифный план</b>
🔹 /contact — <b>свяжись с поддержкой</b>

<b>Bloommy</b> делает твой магазин доступным прямо в Telegram и помогает адаптировать его под твои нужды.

<b>⚡ Начни прямо сейчас!</b>
"""

    await message.answer(welcome_text, reply_markup=builder.as_markup(), parse_mode="HTML")


async def cmd_demo(message: types.Message):
    # Создаем WebApp кнопку
    web_app_info = types.WebAppInfo(
        url="https://demo.bloommy.ru/?action=wptelegram_login_webapp&confirm_login=0&redirect_to=https://demo.bloommy.ru/"
    )

    # Создаем кнопку
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="🚀 Посмотреть демо",  # Добавили эмодзи для привлекательности
        web_app=web_app_info)
    )

    # Форматированное сообщение с HTML-разметкой
    demo_text = """
<b>🌷 Демонстрация Bloommy</b>

Познакомься с возможностями нашего сервиса в <b>демо-режиме</b> и увидишь, как просто создать свой магазин в Telegram!

<b>✨ Что ты увидишь в демо-версии:</b>

🌸 <b>Каталог товаров</b> - красивое оформление для цветов и подарков
🛒 <b>Процесс заказа</b> - удобное оформление прямо в боте
⚙️ <b>Панель управления</b> - простые настройки магазина

<b>Bloommy</b> превращает твой Telegram-бот в полноценное <b>мини-приложение</b> для продаж!

Нажми на кнопку ниже, чтобы <b>опробовать демо-версию</b> прямо сейчас 👇
"""

    await message.answer(
        demo_text,
        reply_markup=builder.as_markup(),
        parse_mode="HTML"  # Включаем HTML-разметку
    )


async def cmd_info(message: types.Message):
    # Создаем кнопку с эмодзи
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="📝 Пройти опрос",  # Добавили эмодзи для визуального выделения
        callback_data="quiz"
    ))

    # Форматированное информационное сообщение
    info_text = """
<b>🌿 Bloommy — твой идеальный магазин в Telegram</b>

<b>📌 Как это работает?</b>

Bloommy — это <b>профессиональный конструктор</b> для создания веб-бота в Telegram, специально разработанный для <b>цветочных и подарочных магазинов</b>.

<b>🔹 Простой процесс подключения:</b>

1. <b>📞 Опрос с менеджером</b>
   Уточним ваши потребности и предпочтения для идеальной настройки сервиса

2. <b>⚙️ Настройка бота</b>
   Наша команда адаптирует:
   • Логотип и название
   • Цветовую гамму
   • Основные функции

3. <b>🆓 Пробный период 7 дней</b>
   Полный доступ к:
   • Каталогу товаров
   • Админ-панели
   • Всем функциям бота

4. <b>💳 Оплата тарифа</b>
   Продолжение работы после пробного периода

<b>✨ Преимущества Bloommy:</b>
• Простое управление товарами
• Удобный интерфейс для клиентов
• Полная автоматизация продаж

<b>🚀 Начни автоматизировать продажи уже сегодня!</b>
"""

    await message.answer(
        info_text,
        reply_markup=builder.as_markup(),
        parse_mode="HTML"  # Включаем HTML-разметку
    )


async def cmd_tariff(message: types.Message):
    # Создаем кнопку с эмодзи
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="💳 Оформить заказ",  # Добавили эмодзи для визуального выделения
        callback_data="quiz"
    ))

    # Форматированное сообщение о тарифах
    tariff_text = """
<b>💎 Тарифы Bloommy</b>

<b>🌿 Базовый тариф: 3 000 ₽/месяц</b>

Полный пакет возможностей для создания и управления вашим магазином в Telegram.

<b>✨ Что включено:</b>

✅ <b>Полная настройка бота</b>
   • Логотип и название
   • Цветовая гамма
   • Основные параметры

✅ <b>Удобная админ-панель</b>
   • Управление каталогом товаров
   • Редактирование ассортимента
   • Контроль заказов

✅ <b>Полный функционал продаж</b>
   • Прием заказов
   • Обработка платежей
   • Уведомления

✅ <b>Поддержка 24/7</b>
   • Консультации
   • Помощь в настройке
   • Решение вопросов

<b>🆓 Пробный период 7 дней</b> - полноценный тест-драйв всех возможностей!

<b>💼 Условия:</b>
• Ежемесячная оплата
• Автопродление
• Без скрытых платежей

<b>🚀 Начни продавать в Telegram уже сегодня!</b>
"""

    await message.answer(
        tariff_text,
        reply_markup=builder.as_markup(),
        parse_mode="HTML"  # Включаем HTML-разметку
    )

async def cmd_contact(message: types.Message):
    # Создаем кнопку с эмодзи
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="💬 Получить консультацию",  # Добавили эмодзи
        callback_data="quiz"
    ))

    # Форматированное контактное сообщение
    contact_text = """
<b>📩 Контакты Bloommy</b>

Мы всегда готовы помочь с настройкой и запуском твоего магазина!

<b>🔹 Способы связи:</b>

📞 <b>Телефон:</b> 
+7 (978) 179-75-78

✉️ <b>Email:</b> 
support@bloommy.ru

📲 <b>Telegram:</b> 
@bloommy_support

<b>⏰ Часы работы поддержки:</b>
Пн-Пт: 9:00 - 18:00
Сб-Вс: 10:00 - 15:00

<b>💡 Нужна срочная помощь?</b>
Нажми кнопку ниже для быстрой консультации 👇
"""

    await message.answer(
        contact_text,
        reply_markup=builder.as_markup(),
        parse_mode="HTML"  # Включаем HTML-разметку
    )
