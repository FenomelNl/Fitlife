# Проект FitLife - MVP версия 1.0

# 1. Знакомство
user_name = input('Введите имя: ')
user_age = int(input('Введите возраст: '))

# 2. Сбор данных
user_weight = float(input('Введите вес в формате килограммы.граммы: '))
user_height = float(input('Введите рост в формате метры.сантиметры: '))

# 3. Логика расчетов
bmi = user_weight / (user_height ** 2)

# Подсчет воды
water_ml = user_weight * 30 
water_l = water_ml / 1000


# 4. Вывод красивого результата
print(f"Отчет для пользователя: {user_name} ({user_age} г.)")
print(f"Твой Индекс Массы Тела: {bmi:.1f}")
print(f"Рекомендуемая норма воды: {water_l:.1f} л. воды в день")
print("Расчет окончен. Будьте здоровы!")