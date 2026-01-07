"""
input_validation.py - валидация пользовательского ввода
"""


def validate_name(name):
    """Базовая валидация ФИО."""
    if len(name) < 2:
        return False, "Имя должно содержать минимум 2 символа"
    if not name.isalpha():
        return False, "Имя должно содержать только буквы"
    return True, ""


def validate_date(date_str):
    """Улучшенная валидация даты рождения."""
    if len(date_str) != 10 or date_str[4] != '-' or date_str[7] != '-':
        return False, "Неверный формат даты (используйте ГГГГ-ММ-ДД)"

    try:
        year = int(date_str[0:4])
        month = int(date_str[5:7])
        day = int(date_str[8:10])

        # Проверка диапазона значений
        if year < 1900 or year > 2024:
            return False, "Год рождения должен быть от 1900 до 2024"

        if month < 1 or month > 12:
            return False, "Месяц должен быть от 1 до 12"

        # Определение количества дней в месяце
        days_in_month = 31
        if month in [4, 6, 9, 11]:
            days_in_month = 30
        elif month == 2:
            # Проверка високосного года
            is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
            days_in_month = 29 if is_leap else 28

        # Финальная проверка дня
        if day < 1 or day > days_in_month:
            return False, f"Некорректный день для месяца {month} (максимум {days_in_month} дней)."

        return True, ""
    except Exception as e:
        return False, f"Некорректные значения в дате: {str(e)}"


def validate_specialty(specialty):
    """Валидация специальности."""
    if len(specialty) < 3:
        return False, "Специальность должна содержать минимум 3 символа"

    allowed_chars = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ -"
    for char in specialty:
        if char.lower() not in allowed_chars:
            return False, "Специальность может содержать только буквы, пробелы и дефисы"

    return True, ""


def validate_number(value, min_val=0, max_val=100, field_name=""):
    """Универсальная валидация числовых полей."""
    try:
        num = int(value)
        if num < min_val or num > max_val:
            return False, f"{field_name} должен быть в диапазоне от {min_val} до {max_val}"
        return True, ""
    except ValueError:
        return False, f"{field_name} должен быть целым числом"


def get_validated_input(prompt, validation_type=None, min_val=None, max_val=None, field_name=""):
    """Получает ввод с валидацией."""
    while True:
        value = input(prompt).strip()
        if not value:
            print("Ошибка: Поле не может быть пустым")
            continue

        if validation_type == "name":
            is_valid, msg = validate_name(value.capitalize())
        elif validation_type == "date":
            is_valid, msg = validate_date(value)
        elif validation_type == "specialty":
            is_valid, msg = validate_specialty(value)
        elif validation_type == "number" and min_val is not None and max_val is not None:
            is_valid, msg = validate_number(value, min_val, max_val, field_name)
        else:
            return value

        if is_valid:
            return value
        print(f"Ошибка: {msg}")