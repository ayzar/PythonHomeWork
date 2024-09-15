import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
import os

API_TOKEN = 'BOT_API_TOKEN'

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Создаем объекты бота и диспетчера
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Определяем состояния
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

# Создаем клавиатуру с кнопками "Рассчитать" и "Информация"
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_calculate = KeyboardButton('Рассчитать')
button_info = KeyboardButton('Информация')
keyboard.add(button_calculate, button_info)

# Стартовая команда, отправляющая клавиатуру
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Нажмите 'Рассчитать', чтобы начать расчет нормы калорий, или 'Информация' для дополнительной информации.", reply_markup=keyboard)

# Начало цепочки вопросов по нажатию кнопки "Рассчитать"
@dp.message_handler(Text(equals='Рассчитать', ignore_case=True))
async def set_age(message: types.Message):
    await UserState.age.set()
    await message.reply("Введите свой возраст:")

# Обработка нажатия кнопки "Информация"
@dp.message_handler(Text(equals='Информация', ignore_case=True))
async def send_information(message: types.Message):
    # Здесь можно добавить любую информацию, которую вы хотите предоставить пользователю
    info_text = (
        "Этот бот поможет вам рассчитать вашу дневную норму калорий.\n\n"
        "Чтобы начать расчет, нажмите 'Рассчитать' и следуйте инструкциям.\n\n"
        "Формула расчета основана на методе Миффлина-Сан Жеора, который учитывает ваш возраст, рост и вес.\n\n"
        "Для мужчин формула выглядит так:\n"
        "`10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (лет) + 5`\n\n"
        "Для женщин формула немного отличается:\n"
        "`10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (лет) - 161`\n\n"
        "Используйте точные данные для получения наиболее точного результата."
    )
    await message.reply(info_text, parse_mode=types.ParseMode.MARKDOWN)

# Обработка возраста и переход к следующему вопросу
@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=int(message.text))
    await UserState.growth.set()
    await message.reply("Введите свой рост в сантиметрах:")

# Обработка роста и переход к следующему вопросу
@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=int(message.text))
    await UserState.weight.set()
    await message.reply("Введите свой вес в килограммах:")

# Обработка веса, расчет калорий и завершение цепочки
@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=int(message.text))

    # Получаем все данные
    data = await state.get_data()
    age = data['age']
    growth = data['growth']
    weight = data['weight']

    # Вычисляем норму калорий, используя упрощенную формулу Миффлина - Сан Жеора
    calories = 10 * weight + 6.25 * growth - 5 * age + 5  # Используем формулу для мужчин

    # Отправляем результат
    await message.reply(f"Ваша норма калорий: {calories:.2f} ккал в день.", reply_markup=types.ReplyKeyboardRemove())

    # Завершаем состояние
    await state.finish()

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)