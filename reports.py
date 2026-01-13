"""
reports.py - генерация отчетов
"""

from sorting import shaker_sort
from input_validation import get_validated_input
from applicant_operations import display_applicants


def generate_report(applicants, report_type):
    """Генерирует отчеты в зависимости от типа."""
    if not applicants:
        print("\nБаза данных пуста.")
        return

    if report_type == "full":
        __generate_full_report(applicants)
    elif report_type == "specialty":
        __generate_specialty_report(applicants)
    elif report_type == "salary":
        __generate_salary_report(applicants)


def __generate_full_report(applicants):
    """Генерирует полный список соискателей."""
    sorted_list = shaker_sort(
        applicants,
        key=lambda x: (x.specialty.lower(), x.last_name.lower())
    )
    display_applicants(sorted_list, "ПОЛНЫЙ СПИСОК СОИСКАТЕЛЕЙ (по специальности и фамилии):")


def __generate_specialty_report(applicants):
    """Генерирует список по специальности."""
    specialty = input("Введите специальность: ").strip()
    filtered = [a for a in applicants if a.specialty.lower() == specialty.lower()]

    if filtered:
        sorted_list = shaker_sort(
            filtered,
            key=lambda x: (
                -x.experience,  # По убыванию стажа
                -1 if x.gender == "М" else 0,  # Мужчины перед женщинами
                x.last_name.lower()  # По алфавиту фамилий
            )
        )
        display_applicants(sorted_list, f"СОИСКАТЕЛИ СО СПЕЦИАЛЬНОСТЬЮ '{specialty.upper()}':")
    else:
        print(f"Нет соискателей со специальностью '{specialty}'.")


def __generate_salary_report(applicants):
    """Генерирует список по диапазону оклада."""
    try:
        min_salary = int(get_validated_input("Минимальный оклад: ", "number", 10000, 1000000, "Оклад"))
        max_salary = int(get_validated_input("Максимальный оклад: ", "number", 10000, 1000000, "Оклад"))

        if min_salary > max_salary:
            print("Ошибка: Минимальный оклад не может быть больше максимального")
            return

        filtered = [a for a in applicants if min_salary <= a.expected_salary <= max_salary]

        if filtered:
            sorted_list = shaker_sort(
                filtered,
                key=lambda x: (-x.expected_salary, x.last_name.lower())
            )
            display_applicants(sorted_list, f"СОИСКАТЕЛИ С ОКЛАДОМ ОТ {min_salary} ДО {max_salary} РУБ.:")
        else:
            print(f"Нет соискателей с окладом в диапазоне от {min_salary} до {max_salary} руб.")
    except ValueError:
        print("Ошибка: Введите корректные числовые значения.")
