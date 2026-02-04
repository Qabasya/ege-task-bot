import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command

from config.config import load_config
from services.task_loader import load_tasks
from handlers import user, other
from keyboards.menu import set_main_menu

async def main():
    config = load_config()

    bot = Bot(token=config.bot.token)
    dp = Dispatcher()

    # Загружаем задания
    user.tasks_data['7'] = load_tasks('tasks/task_7.txt')
    user.tasks_data['8'] = load_tasks('tasks/task_8.txt')
    user.tasks_data['11'] = load_tasks('tasks/task_11.txt')

    # Регистрация хендлеров
    dp.message.register(user.start_menu_handler, Command('start'))
    dp.message.register(user.train_handler, Command('train'))
    dp.message.register(user.about_handler, Command('about'))

    dp.message.register(user.ege_button_handler, F.text == 'ЕГЭ информатика')

    dp.callback_query.register(user.choose_type_handler, F.data.startswith('type_'))
    dp.callback_query.register(user.paginate_handler, F.data.in_(['left', 'right']))
    dp.callback_query.register(user.ask_answer_handler, F.data == 'answer')
    dp.callback_query.register(user.back_task_handler, F.data == 'back_task')
    dp.callback_query.register(user.back_types_handler, F.data == 'back_types')

    dp.message.register(user.check_answer_handler)
    dp.message.register(other.other_handler)

    # Кнопка Menu
    await set_main_menu(bot)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
