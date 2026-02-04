from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def create_train_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='ЕГЭ информатика'),
                KeyboardButton(text='ОГЭ информатика'),
            ],
            [
                KeyboardButton(text='📖 Статьи по заданиям')
            ],
        ],
        resize_keyboard=True
    )
