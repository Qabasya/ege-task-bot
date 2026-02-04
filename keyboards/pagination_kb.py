from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from lexicon.lexicon import LEXICON

def create_task_keyboard():
    """
    Клавиатура под текстом задания с пагинацией
    :return:
    """
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=LEXICON['left'], callback_data='left'),
            InlineKeyboardButton(text=LEXICON['answer_btn'], callback_data='answer'),
            InlineKeyboardButton(text=LEXICON['right'], callback_data='right'),
        ]
    ])


def create_back_keyboard():
    """
    Клавиатура возврата к выбору типа задания или к заданиям выбранного типа
    :return:
    """
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=LEXICON['back_task'], callback_data='back_task')],
        [InlineKeyboardButton(text=LEXICON['back_types'], callback_data='back_types')],
    ])
