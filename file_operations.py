"""
file_operations.py - работа с файлами
"""

from file_io import load_applicants_from_file, save_applicants_to_file, create_test_database


def load_data(filename):
    """Загружает данные из файла при запуске программы."""
    try:
        applicants = load_applicants_from_file(filename)
        print(f"Загружено {len(applicants)} записей из файла {filename}")
        return applicants
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден. Будет создана новая база данных.")
    except Exception as e:
        print(f"Ошибка загрузки данных: {e}")
    return []


def save_data(applicants):
    """Сохраняет данные в файл."""
    if not applicants:
        print("\nНет данных для сохранения.")
        return

    filename = input("\nВведите имя файла (по умолчанию applicants.json): ").strip() or "applicants.json"
    try:
        save_applicants_to_file(applicants, filename)
        print(f"Данные успешно сохранены в файл {filename}")
    except Exception as e:
        print(f"Ошибка при сохранении: {e}")


def load_test_database(applicants):
    """Загружает тестовую базу данных."""
    confirm = input("Загрузить тестовую базу? Это удалит текущие данные (y/n): ").lower()
    if confirm == 'y':
        applicants.clear()
        applicants.extend(create_test_database())
        print(f"Загружено {len(applicants)} тестовых записей.")