"""
applicant_operations.py - операции с соискателями
"""

from applicant import Applicant
from input_validation import get_validated_input


def add_applicant(applicants):
    """Добавляет нового соискателя с валидацией данных."""
    print("\n" + "=" * 50)
    print("ДОБАВЛЕНИЕ НОВОГО СОИСКАТЕЛЯ")
    print("=" * 50)

    last_name = get_validated_input("Фамилия: ", "name")
    first_name = get_validated_input("Имя: ", "name")
    middle_name = get_validated_input("Отчество: ", "name")

    gender = get_validated_input("Пол (М/Ж): ").upper()
    while gender not in ["М", "Ж"]:
        print("Ошибка: Введите 'М' для мужского пола или 'Ж' для женского")
        gender = get_validated_input("Пол (М/Ж): ").upper()

    birth_date = get_validated_input("Дата рождения (ГГГГ-ММ-ДД): ", "date")

    specialty = get_validated_input("Специальность: ", "specialty")

    experience = int(get_validated_input("Стаж работы (в годах): ", "number", 0, 50, "Стаж"))

    languages_input = input("Иностранные языки (через запятую): ").strip()
    languages = [lang.strip().capitalize() for lang in languages_input.split(',') if lang.strip()]

    salary = get_validated_input("Ожидаемый оклад (руб.): ", "number", 10000, 1000000, "Оклад")
    expected_salary = int(salary)

    new_applicant = Applicant(
        last_name, first_name, middle_name, gender, birth_date,
        specialty, experience, languages, expected_salary
    )

    applicants.append(new_applicant)
    print(f"\nСоискатель {last_name} {first_name} {middle_name} успешно добавлен!")


def delete_applicant(applicants):
    """Удаляет соискателя из списка."""
    if not applicants:
        print("\nСписок соискателей пуст.")
        return

    print("\n" + "=" * 50)
    print("УДАЛЕНИЕ СОИСКАТЕЛЯ")
    print("=" * 50)

    display_applicants(applicants, "СПИСОК СОИСКАТЕЛЕЙ:")

    while True:
        try:
            index = int(input("\nВведите номер соискателя для удаления (0 для отмены): ")) - 1
            if index == -1:
                print("Удаление отменено.")
                return
            if 0 <= index < len(applicants):
                applicant = applicants[index]
                confirm = input(
                    f"Вы уверены, что хотите удалить {applicant.last_name} {applicant.first_name}? (y/n): ").lower()
                if confirm == 'y':
                    del applicants[index]
                    print("Соискатель успешно удален.")
                else:
                    print("Удаление отменено.")
                return
            print("Ошибка: Некорректный номер.")
        except ValueError:
            print("Ошибка: Введите корректное число.")


def display_applicants(applicants, title):
    """Отображает список соискателей."""
    if not applicants:
        print("\nНет данных для отображения.")
        return False

    print(f"\n{title}")
    print("-" * 80)
    for i, applicant in enumerate(applicants, 1):
        print(f"{i:2}. {applicant}")
    print("-" * 80)
    print(f"Всего записей: {len(applicants)}")
    return True