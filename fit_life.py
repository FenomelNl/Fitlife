# Проект FitLife - MVP версия 1.0
import constants

# 1. Знакомство
user_name = input('Введите имя: ').title()
while True:
    try:
        user_age = int(input("Введите возраст: "))
        break
    except ValueError:
        print("Неверный формат! Нужно целое число.")

# 2. Сбор данных
user_weight = float(input('Введите вес в формате кг.г: ').replace(",", "."))
user_height = float(input('Введите рост в формате м.см: ').replace(",", "."))

# 3. Логика расчетов
bmi = user_weight / (user_height ** 2)

# Подсчет воды
water_ml = user_weight * constants.ML_PER_KG
water_l = water_ml / constants.ML_TO_L

# 4. Вывод красивого результата
print(f"Отчет для пользователя: {user_name} ({user_age} г.)")
print(f"Твой Индекс Массы Тела: {bmi:.1f}")
print(f"Рекомендуемая норма воды: {water_l:.1f} л. воды в день")
print("Расчет окончен. Будьте здоровы!")
