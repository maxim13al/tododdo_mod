import os
from dotenv import load_dotenv
from faker import Faker
import random
import string


load_dotenv()
FAKER_LOCALE = os.getenv("FAKER_LOCALE", "en_US")


class FakeDataGenerator:
    def __init__(self, locale=FAKER_LOCALE):
        self.faker = Faker(locale)

    def get_fake_list_name(self, valid_length="valid", max_length=30) -> str:
        """
        Генерирует случайное название списка задач
        :param valid_length:
        :param max_length:
        :return:
        """
        while True:
            todo_list_name = self.faker.catch_phrase()
            name_length = len(todo_list_name)
            if valid_length == "valid":
                if name_length <= max_length:
                    return todo_list_name
            else:
                if name_length > max_length:
                    return todo_list_name

    def get_fake_task_text(self) -> str:
        """
        Генерирует случайное описание задачи
        :return:
        """
        return self.faker.sentence()

    def generate_random_word(self, length: int) -> str:
        """
        Генерирует случайное слово строго заданной длины из букв
        :param length:
        :return:
        """
        return "".join(random.choices(string.ascii_lowercase, k=length))


fake_data = FakeDataGenerator()
