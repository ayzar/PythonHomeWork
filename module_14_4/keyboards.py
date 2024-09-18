from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# Клавиатура с кнопками "Рассчитать", "Информация", "Купить"
def create_main_keyboard():
    main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button_calculate = KeyboardButton('Рассчитать')
    button_info = KeyboardButton('Информация')
    button_buy = KeyboardButton('Купить')
    main_keyboard.row(button_calculate, button_info).add(button_buy)
    return main_keyboard

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
