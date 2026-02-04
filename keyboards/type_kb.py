from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def create_type_keyboard():
    """
    Клавиатура выбора типа задания
    :return:
    """
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Задания 7', callback_data='type_7')],
        [InlineKeyboardButton(text='Задания 8', callback_data='type_8')],
        [InlineKeyboardButton(text='Задания 11', callback_data='type_11')],
    ])
