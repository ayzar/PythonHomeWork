from aiogram import Bot, Dispatcher, types
from aiogram import executor
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from keyboards import create_main_keyboard, create_inline_keyboard, create_calories_keyboard
from crud_functions import initiate_db, get_all_products, add_user, is_included 



API_TOKEN = 'BOT_API_TOKEN'

# Создаем объекты бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())

# Инициализируем базу данных
initiate_db()

# Шаги для калькулятора калорий
class CalorieCalculator(StatesGroup):
    waiting_for_weight = State()
    waiting_for_height = State()
    waiting_for_age = State()
    waiting_for_gender = State()

# Команда /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Добро пожаловать! Выберите действие:", reply_markup=create_main_keyboard())

# Обработка нажатия на кнопку "Рассчитать"
@dp.message_handler(lambda message: message.text == "Рассчитать")
async def calculate_handler(message: types.Message):
    await message.answer("Пожалуйста, выберите опцию:", reply_markup=create_calories_keyboard())

# Обработка инлайн-кнопок для калькуляции калорий
@dp.callback_query_handler(lambda call: call.data == 'calories')
async def start_calories_calculation(call: types.CallbackQuery):
    await call.message.answer("Введите ваш вес в кг:")
    await CalorieCalculator.waiting_for_weight.set()

@dp.message_handler(state=CalorieCalculator.waiting_for_weight)
async def process_weight(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['weight'] = float(message.text)
    await message.answer("Введите ваш рост в см:")
    await CalorieCalculator.waiting_for_height.set()

@dp.message_handler(state=CalorieCalculator.waiting_for_height)
async def process_height(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['height'] = float(message.text)
    await message.answer("Введите ваш возраст:")
    await CalorieCalculator.waiting_for_age.set()

@dp.message_handler(state=CalorieCalculator.waiting_for_age)
async def process_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = int(message.text)
    await message.answer("Введите ваш пол (муж/жен):")
    await CalorieCalculator.waiting_for_gender.set()

@dp.message_handler(state=CalorieCalculator.waiting_for_gender)
async def process_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        gender = message.text.lower()
        data['gender'] = gender

        # Получаем все данные для расчета
        weight = data['weight']
        height = data['height']
        age = data['age']
        gender = data['gender']

        # Расчет калорий по формуле Харриса-Бенедикта
        if gender == "муж":
            bmr = 88.36 + (13.4 * weight) + (4.8 * height) - (5.7 * age)
        elif gender == "жен":
            bmr = 447.6 + (9.2 * weight) + (3.1 * height) - (4.3 * age)
        else:
            await message.answer("Некорректный пол. Пожалуйста, введите 'муж' или 'жен'.")
            return

        await message.answer(f"Ваш базовый уровень метаболизма: {bmr:.2f} калорий в день.")

    await state.finish()

# Обработка нажатия на кнопку "Информация"
@dp.message_handler(lambda message: message.text == "Информация")
async def info_handler(message: types.Message):
    info_text = (
        "Добро пожаловать в нашего бота!\n"
        "Мы можем помочь вам рассчитать калории и предложить товары для вашего здоровья.\n\n"
        "Доступные команды:\n"
        "/start - начать работу\n"
        "/buy - посмотреть продукты и купить\n"
        "/calculate - рассчитать калории"
    )
    await message.answer(info_text)

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


# Обработка нажатия на кнопку "Купить"
@dp.message_handler(lambda message: message.text == "Купить")
async def get_buying_list(message: types.Message):
    products = get_all_products()

    if not products:
        await message.answer("Продукты пока отсутствуют.")
    else:
        for product in products:
            if product[4]:  # Проверка на наличие URL картинки
                await message.answer_photo(photo=product[4])

            await message.answer(f'Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}')

        inline_keyboard = create_inline_keyboard(products)
        await message.answer("Выберите продукт для покупки:", reply_markup=inline_keyboard)

# Обработка инлайн-кнопок для покупки продукта
@dp.callback_query_handler(lambda call: call.data.startswith('buy_'))
async def handle_buy(call: types.CallbackQuery):
    product_id = int(call.data.split('_')[1])
    await call.message.answer(f'Вы успешно приобрели продукт с id: {product_id}')
    await call.answer()



# Состояния регистрации
class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()

# Начало регистрации
@dp.message_handler(Text(equals='Регистрация'))
async def sign_up(message: types.Message):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await RegistrationState.username.set()

# Обработка имени пользователя
@dp.message_handler(state=RegistrationState.username)
async def set_username(message: types.Message, state: FSMContext):
    username = message.text
    if not is_included(username):
        async with state.proxy() as data:
            data['username'] = username
        await message.answer("Введите свой email:")
        await RegistrationState.email.set()
    else:
        await message.answer("Пользователь с таким именем уже существует. Введите другое имя:")

# Обработка email
@dp.message_handler(state=RegistrationState.email)
async def set_email(message: types.Message, state: FSMContext):
    email = message.text
    async with state.proxy() as data:
        data['email'] = email
    await message.answer("Введите свой возраст:")
    await RegistrationState.age.set()

# Обработка возраста
@dp.message_handler(state=RegistrationState.age)
async def set_age(message: types.Message, state: FSMContext):
    age = message.text
    async with state.proxy() as data:
        data['age'] = int(age)
        username = data['username']
        email = data['email']

    # Добавление пользователя в базу данных
    add_user(username, email, age)
    await message.answer("Регистрация завершена!")
    await state.finish()


# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp)

