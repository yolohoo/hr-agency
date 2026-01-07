"""
Главный модуль программы 'Кадровое агентство'.
Точка входа в программу с минимальной логикой.
"""

import sys
from menu import display_menu, get_user_choice
from applicant_operations import add_applicant, delete_applicant
from file_operations import load_data, save_data, load_test_database
from reports import generate_report


def main():
    """Основная функция программы."""
    applicants = []
    default_file = "applicants.json"

    # Приветственное сообщение
    print("=" * 50)
    print("КАДРОВОЕ АГЕНТСТВО")
    print("=" * 50)

    # Загрузка данных при запуске
    applicants = load_data(default_file)

    while True:
        display_menu()
        choice = get_user_choice(8)

        if choice == 1:  # Полный список
            generate_report(applicants, "full")

        elif choice == 2:  # По специальности
            generate_report(applicants, "specialty")

        elif choice == 3:  # По окладу
            generate_report(applicants, "salary")

        elif choice == 4:  # Добавить
            add_applicant(applicants)

        elif choice == 5:  # Удалить
            delete_applicant(applicants)

        elif choice == 6:  # Сохранить
            save_data(applicants)

        elif choice == 7:  # Тестовая база
            load_test_database(applicants)

        elif choice == 8:  # Выход
            if applicants:
                save_confirmation = input("Сохранить данные перед выходом? (y/n): ").lower()
                if save_confirmation == 'y':
                    save_data(applicants)
            print("\nПрограмма завершена. До свидания!")
            sys.exit(0)

        input("\nНажмите Enter для продолжения...")


if __name__ == "__main__":
    main()