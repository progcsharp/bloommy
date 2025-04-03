from aiogram.types import BotCommand


async def set_commands(bot):
    commands = [
        BotCommand(command="/start", description="Запустить бота!"),
        BotCommand(command="/demo", description="Посмотреть демонстрацию работы."),
        BotCommand(command="/info", description="Узнать, как это работает."),
        BotCommand(command="/tariff", description="Ознакомиться с тарифом."),
        BotCommand(command="/contact", description="Получить контакты менеджера.")
    ]
    await bot.set_my_commands(commands)
