import asyncio
from aiogram import Bot, Dispatcher

from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import load_config
from handlers.user import router as user_router
from handlers.other import router as other_router
from keyboards.menu import set_main_menu

from handlers import user
from services.dbloader import load_tasks_from_db


async def main():
    # Загружаем задания
    user.tasks_data['7'] = load_tasks_from_db('db/ege_bot_db.db', 'task_7')
    user.tasks_data['8'] = load_tasks_from_db('db/ege_bot_db.db', 'task_8')
    user.tasks_data['11'] = load_tasks_from_db('db/ege_bot_db.db', 'task_11')

    config = load_config()

    # ===== СОЗДАНИЕ БОТА =====
    bot = Bot(
        token=config.bot.token,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML
        )
    )
    # ===== СОЗДАНИЕ ДИСПЕТЧЕРА =====
    dp = Dispatcher()

    # ===== ПОДКЛЮЧЕНИЕ РОУТЕРОВ =====
    dp.include_router(user_router)
    dp.include_router(other_router)

    # ===== КНОПКИ МЕНЮ С КОМАНДАМИ =====
    await set_main_menu(bot)

    # ===== ЗАПУСК POLLING =====
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
