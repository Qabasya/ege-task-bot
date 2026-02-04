from aiogram.types import BotCommand


async def set_main_menu(bot):
    commands = [
        BotCommand(command='/start', description='Начало работы'),
        BotCommand(command='/train', description='Тренажёр'),
        BotCommand(command='/about', description='Об авторе'),
    ]

    await bot.set_my_commands(commands)