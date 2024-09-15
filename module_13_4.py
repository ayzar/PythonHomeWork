import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

API_TOKEN = 'BOT_API_TOKEN'

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я бот для подсчета нормы калорий. Используйте команду /calories, чтобы начать.")

@dp.message_handler(commands=['calories'])
async def start_calories(message: types.Message):
    await message.answer("Давайте рассчитаем вашу норму калорий. Для начала, введите свой возраст:")
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Пожалуйста, введите возраст числом.")
        return
    await state.update_data(age=int(message.text))
    await message.answer("Теперь введите свой рост в сантиметрах:")
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Пожалуйста, введите рост числом.")
        return
    await state.update_data(growth=int(message.text))
    await message.answer("И наконец, введите свой вес в килограммах:")
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    if not message.text.replace('.', '').isdigit():
        await message.answer("Пожалуйста, введите вес числом.")
        return
    await state.update_data(weight=float(message.text))
    data = await state.get_data()

    age = data['age']
    growth = data['growth']
    weight = data['weight']

    # Формула Миффлина-Сан Жеора для женщин
    calories = (10 * weight) + (6.25 * growth) - (5 * age) - 161

    await message.answer(f"Ваша норма калорий: {calories:.2f} ккал/день")
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)