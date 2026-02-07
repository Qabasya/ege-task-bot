from aiogram import Router, F
from aiogram.types import Message

# Создаём роутер
router = Router(name='other_router')

@router.message()
async def other_handler(message: Message):
    await message.answer('Используйте кнопки бота.')
