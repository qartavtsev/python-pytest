import qrcode
from PIL import Image

# Создание QR-кода
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)  # Высокая коррекция
qr.add_data("https://t.me/+-nF-7B7J7vMxZGRi")
qr.make(fit=True)

# Генерация изображения QR-кода
qr_img = qr.make_image(fill="black", back_color="white").convert("RGBA")

# Открытие логотипа
logo = Image.open("E:\\QAtools\\logo.jpeg").convert("RGBA")  # Преобразуем в RGBA

# Масштабируем логотип
logo_size = (qr_img.size[0] // 5, qr_img.size[1] // 5)
logo = logo.resize(logo_size, Image.LANCZOS)

# Создаём маску прозрачности
mask = logo.split()[3] if logo.mode == "RGBA" else None  # Альфа-канал

# Вставляем логотип в центр
pos = ((qr_img.size[0] - logo_size[0]) // 2, (qr_img.size[1] - logo_size[1]) // 2)
qr_img.paste(logo, pos, mask=mask)  # Используем альфа-канал в качестве маски

# Сохранение изображения
qr_img.save("E:\\QAtools\\qr_with_logo.png")

print("QR-код успешно сохранен!")
