from aiogram.types import Message

async def other_handler(message: Message):
    await message.answer('Используйте кнопки бота.')
