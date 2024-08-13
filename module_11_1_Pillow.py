from PIL import Image, ImageDraw, ImageFilter, ImageFont

# 1. Открытие и сохранение изображения
image = Image.open('example.jpg')
image.save('example_copy.png')  # Сохранение в другом формате

# 2. Изменение размера изображения (ресайзинг)
resized_image = image.resize((300, 300))
resized_image.save('example_resized.png')

# 3. Поворот и зеркалирование
rotated_image = image.rotate(45)  # Поворот на 45 градусов
rotated_image.save('example_rotated.png')

flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)  # Зеркальное отражение по горизонтали
flipped_image.save('example_flipped.png')

# 4. Применение фильтров
blurred_image = image.filter(ImageFilter.BLUR)  # Размытие изображения
blurred_image.save('example_blurred.png')

# 5. Добавление текста на изображение
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()  # Загружаем шрифт
text = "Hello, World!"
draw.text((10, 10), text, font=font, fill=(55, 55, 55))  #  текст в верхнем левом углу
image.save('example_text.png')