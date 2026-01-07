"""
applicant.py - класс для представления соискателя
"""


class Applicant:
    """
    Класс для представления информации о соискателе.
    """

    def __init__(self, last_name, first_name, middle_name, gender, birth_date,
                 specialty, experience, languages, expected_salary):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.gender = gender
        self.birth_date = birth_date
        self.specialty = specialty
        self.experience = experience
        self.languages = languages
        self.expected_salary = expected_salary

    def __str__(self):
        """Возвращает строковое представление соискателя."""
        languages_str = ", ".join(self.languages) if self.languages else "Нет"
        return (f"{self.last_name} {self.first_name[0]}.{self.middle_name[0]}. | "
                f"Пол: {self.gender} | ДР: {self.birth_date} | "
                f"Специальность: {self.specialty} | Стаж: {self.experience} лет | "
                f"Языки: {languages_str} | Оклад: {self.expected_salary} руб.")

    def to_dict(self):
        """Преобразует объект в словарь для сериализации."""
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "middle_name": self.middle_name,
            "gender": self.gender,
            "birth_date": self.birth_date,
            "specialty": self.specialty,
            "experience": self.experience,
            "languages": self.languages,
            "expected_salary": self.expected_salary
        }

    @classmethod
    def from_dict(cls, data):
        """Создает объект из словаря."""
        return cls(
            last_name=data["last_name"],
            first_name=data["first_name"],
            middle_name=data["middle_name"],
            gender=data["gender"],
            birth_date=data["birth_date"],
            specialty=data["specialty"],
            experience=data["experience"],
            languages=data["languages"],
            expected_salary=data["expected_salary"]
        )