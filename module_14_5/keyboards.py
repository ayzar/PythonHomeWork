from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# Клавиатура с кнопками "Рассчитать", "Информация", "Купить", "Регистрация"
def create_main_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("Купить"))
    keyboard.add(KeyboardButton("Рассчитать"))
    keyboard.add(KeyboardButton("Информация"))
    keyboard.add(KeyboardButton("Регистрация"))  # Кнопка регистрации
    return keyboard

# Инлайн-клавиатура для калькуляции калорий и формул расчёта
def create_calories_keyboard():
    inline_keyboard = InlineKeyboardMarkup(row_width=1)
    button_calories = InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories')
    button_formulas = InlineKeyboardButton('Формулы расчёта', callback_data='formulas')
    inline_keyboard.add(button_calories, button_formulas)
    return inline_keyboard

# Клавиатура для покупки продукта
def create_inline_keyboard(products):
    inline_keyboard = InlineKeyboardMarkup(row_width=1)
    for product in products:
        inline_keyboard.add(InlineKeyboardButton(product[1], callback_data=f'buy_{product[0]}'))
    return inline_keyboard
