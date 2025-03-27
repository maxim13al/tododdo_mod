import allure
from src.helpers.fake_data import fake_data


@allure.feature("Создание")
@allure.story("Создание задачи")
class TestCreateList:
    @allure.title("Создание новой задачи")
    @allure.description("Проверка создания новой задачи")
    @allure.tag("create", "smoke")
    def test_create_task(self, list_page, task_page, create_list):
        task_name = fake_data.get_fake_list_name()
        list_page.click_add_task_btn()
        task_page.fill_task_name_field(task_name)
        task_page.click_save_task_btn()
        list_page.check_task_name_in_list(task_name)
