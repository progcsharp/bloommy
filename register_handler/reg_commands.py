from aiogram import Dispatcher
from aiogram.filters import Command

from handler.commands import cmd_start, cmd_demo, cmd_info, cmd_tariff, cmd_contact


async def register_handlers_commands(dp: Dispatcher):
    dp.message.register(cmd_start, Command('start'))
    dp.message.register(cmd_demo, Command('demo'))
    dp.message.register(cmd_info, Command('info'))
    dp.message.register(cmd_tariff, Command('tariff'))
    dp.message.register(cmd_contact, Command('contact'))
