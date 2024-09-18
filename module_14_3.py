import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import filters
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from aiogram.utils.callback_data import CallbackData
import os

API_TOKEN = '6991918148:AAGK8X9t9ukY_Dvq_Z04JeSlsfOd0ShcsV0'

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
main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_calculate = KeyboardButton('Рассчитать')
button_info = KeyboardButton('Информация')
button_buy = KeyboardButton('Купить')
# Добавляем кнопки "Рассчитать" и "Информация" в первую строку, а "Купить" во вторую
main_keyboard.row(button_calculate, button_info).add(button_buy)



# Создаем Inline-клавиатуру с двумя кнопками
inline_keyboard = InlineKeyboardMarkup(row_width=1)
button_calories = InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories')
button_formulas = InlineKeyboardButton('Формулы расчёта', callback_data='formulas')
inline_keyboard.add(button_calories, button_formulas)

# Стартовая команда, отправляющая клавиатуру
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply(
        "Привет! Нажмите 'Рассчитать', чтобы начать расчет нормы калорий, или 'Информация' для дополнительной информации.",
        reply_markup=main_keyboard
    )

# Обработка нажатия кнопки "Рассчитать" на обычной клавиатуре
@dp.message_handler(Text(equals='Рассчитать', ignore_case=True))
async def main_menu(message: types.Message):
    await message.reply("Выберите опцию:", reply_markup=inline_keyboard)

# Обработка нажатия кнопки "Формулы расчёта" на Inline-клавиатуре
@dp.callback_query_handler(Text(equals='formulas'))
async def get_formulas(call: types.CallbackQuery):
    info_text = (
        "Формула Миффлина-Сан Жеора:\n\n"
        "Для мужчин:\n"
        "`10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (лет) + 5`\n\n"
        "Для женщин:\n"
        "`10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (лет) - 161`\n\n"
        "Эти формулы позволяют рассчитать базовый уровень метаболизма (BMR), который показывает, сколько калорий "
        "вам нужно для поддержания текущего веса при отсутствии физической активности."
    )
    await call.message.reply(info_text, parse_mode=types.ParseMode.MARKDOWN)
    await call.answer()  # Закрываем уведомление о callback

# Обработка нажатия кнопки "Рассчитать норму калорий" на Inline-клавиатуре
@dp.callback_query_handler(Text(equals='calories'))
async def set_age(call: types.CallbackQuery):
    await UserState.age.set()
    await call.message.reply("Введите свой возраст:")
    await call.answer()  # Закрываем уведомление о callback

# Обработка возраста и переход к следующему вопросу
@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=int(message.text))
    await UserState.growth.set()
    await message.reply("Введите свой рост в сантиметрах:")

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

# Обработка роста и переход к следующему вопросу
@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=int(message.text))
    await UserState.weight.set()
    await message.reply("Введите свой вес в килограммах:")

# Обработка веса, расчет калорий и завершение цепочки
@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    # Обновляем данные состояния
    await state.update_data(weight=int(message.text))

    # Получаем все данные, введенные пользователем
    data = await state.get_data()
    age = data['age']
    growth = data['growth']
    weight = data['weight']

    # Вычисляем норму калорий, используя упрощенную формулу Миффлина-Сан Жеора
    # Формула для мужчин:
    calories = 10 * weight + 6.25 * growth - 5 * age + 5  # Используем формулу для мужчин

    # Отправляем результат пользователю
    await message.reply(f"Ваша норма калорий: {calories:.2f} ккал в день.", reply_markup=types.ReplyKeyboardRemove())

    # Завершаем состояние
    await state.finish()

inline_keyboard_buy = InlineKeyboardMarkup(row_width=2)
inline_keyboard_buy.add(
    InlineKeyboardButton("Product1", callback_data="product_buying"),
    InlineKeyboardButton("Product2", callback_data="product_buying"),
    InlineKeyboardButton("Product3", callback_data="product_buying"),
    InlineKeyboardButton("Product4", callback_data="product_buying"),
)
# Хэндлер для команды /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Добро пожаловать! Выберите действие:", reply_markup=main_keyboard)

# Хэндлер для нажатия на кнопку "Купить"
@dp.message_handler(filters.Text(equals="Купить"))
async def get_buying_list(message: types.Message):
    products = [
        {"name": "Product1", "description": "описание 1", "price": 100, "photo": "http://valayzts.beget.tech/pic/vitamin-complex-package.jpg"},
        {"name": "Product2", "description": "описание 2", "price": 200, "photo": "http://valayzts.beget.tech/pic/realistic-vitamin-complex-package.jpg"},
        {"name": "Product3", "description": "описание 3", "price": 300, "photo": "http://valayzts.beget.tech/pic/realistic-vitamin-complex-package2.jpg"},
        {"name": "Product4", "description": "описание 4", "price": 400, "photo": "http://valayzts.beget.tech/pic/vitamin-complex-container.jpg"},
    ]

    # Обработка и отправка информации о продуктах
    for product in products:
        await message.answer(
            f'Название: {product["name"]} | Описание: {product["description"]} | Цена: {product["price"]}'
        )
        await message.answer_photo(photo=product["photo"])

    await message.answer("Выберите продукт для покупки:", reply_markup=inline_keyboard_buy)

# Хэндлер для инлайн-кнопок
@dp.callback_query_handler(filters.Text("product_buying"))
async def send_confirm_message(call: types.CallbackQuery):
    await call.answer()  # Подтверждаем, что запрос обработан
    await call.message.answer("Вы успешно приобрели продукт!") 

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)