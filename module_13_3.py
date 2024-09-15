import asyncio
from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = 'BOT_TOKEN'

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.")

# Обработчик всех остальных сообщений
@dp.message_handler()
async def all_messages(message: types.Message):
    await message.answer("Введите команду /start, чтобы начать общение.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)