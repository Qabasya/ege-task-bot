from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.types import ReplyKeyboardRemove

from keyboards.about_kb import create_about_keyboard
from keyboards.pagination_kb import create_task_keyboard, create_back_keyboard
from keyboards.train_kb import create_train_keyboard
from keyboards.type_kb import create_type_keyboard
from lexicon.lexicon import LEXICON

# Создаём роутер
router = Router(name='user_router')

users = {}
# Формат словаря users:
# users = {
#     user_id: { # Словарь под каждого пользователя
#         'type': '7', # тип задания: 7 8 или 11
#         'index': 0, # номер задания по порядку
#         'waiting_answer': False # Нажата ли кнопка "дать ответ"
#     }
# }
tasks_data = {}


async def show_task(message, user_id):
    """
    Функция отображения задания
    """
    user = users[user_id]
    tasks = tasks_data[user['type']]
    task = tasks[user['index']]

    text = LEXICON['task'].format(id=task['id'], text=task['text'])

    await message.edit_text(text, reply_markup=create_task_keyboard())


@router.callback_query(F.data.startswith('type_'))
async def choose_type_handler(callback: CallbackQuery):
    """
    Хендлер выбора типа задания.
    Принимает коллбек от кнопок create_type_keyboard
    Например: type_7
    """
    task_type = callback.data.split('_')[1]

    users[callback.from_user.id] = {
        'type': task_type,
        'index': 0,
        'waiting_answer': False
    }
    # Вызываем функцию отображения задания
    await show_task(callback.message, callback.from_user.id)
    await callback.answer()


@router.callback_query(F.data.in_(['left', 'right']))
async def paginate_handler(callback: CallbackQuery):
    """
    Хендлер нажатия на кнопки пагинации (<<< и >>>)
    """
    user = users[callback.from_user.id]
    tasks = tasks_data[user['type']]

    # Перемещение по заданиям (пагинация)
    if callback.data == 'right':
        user['index'] = (user['index'] + 1) % len(tasks)
    else:
        user['index'] = (user['index'] - 1) % len(tasks)

    await show_task(callback.message, callback.from_user.id)
    await callback.answer()


@router.callback_query(F.data == 'answer')
async def ask_answer_handler(callback: CallbackQuery):
    """
    Хендлер кнопки "Дать ответ"
    """
    users[callback.from_user.id]['waiting_answer'] = True
    await callback.message.answer('Введите численный ответ:')
    await callback.answer()


@router.callback_query(F.data == 'back_task')
async def back_task_handler(callback: CallbackQuery):
    """
    Хендлер кнопки возврата к заданиям
    """
    await show_task(callback.message, callback.from_user.id)
    await callback.answer()


@router.callback_query(F.data == 'back_types')
async def back_types_handler(callback: CallbackQuery):
    """
    Хендлер кнопки возврата к типам заданий
    """
    await callback.message.edit_text(
        LEXICON['choose_type'],
        reply_markup=create_type_keyboard()
    )
    await callback.answer()


@router.message(Command("start"))
async def start_menu_handler(message: Message):
    await message.answer(LEXICON['start_text'])


@router.message(Command("train"))
async def train_handler(message: Message):
    await message.answer(
        LEXICON['train_text'],
        reply_markup=create_train_keyboard()
    )


@router.message(Command("about"))
async def about_handler(message: Message):
    await message.answer(
        LEXICON['about_text'],
        reply_markup=create_about_keyboard(),
    )


@router.message(F.text == 'ЕГЭ информатика')
async def ege_button_handler(message: Message):
    await message.answer(
        LEXICON['choose_type'],
        reply_markup=create_type_keyboard()
    )


@router.message()
async def check_answer_handler(message: Message):
    """
    Функция проверки ответа
    """
    user = users.get(message.from_user.id)

    if not user or not user['waiting_answer']:
        return

    tasks = tasks_data[user['type']]
    task = tasks[user['index']]

    if message.text.strip() == task['answer']:
        await message.answer(
            LEXICON['correct'],
            reply_markup=create_back_keyboard()
        )
    else:
        await message.answer(
            LEXICON['wrong'],
            reply_markup=create_back_keyboard()
        )

    user['waiting_answer'] = False
