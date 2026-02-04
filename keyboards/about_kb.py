from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def create_about_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Написать в ТГ',
                url='tg://user?id=5807479922'
            )
        ]
    ])
