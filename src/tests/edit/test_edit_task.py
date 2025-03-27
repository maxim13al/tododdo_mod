import allure
from src.helpers.fake_data import fake_data


@allure.feature("Редактирование")
@allure.story("Редактирование задачи")
class TestEditTask:
    @allure.title("Изменение названия задачи")
    @allure.description("Проверка изменения названия задачи")
    @allure.tag("edit")
    def test_rename_list(self, list_page, task_page, create_task):
        task_name = fake_data.get_fake_task_text()
        list_page.open_last_task()
        task_page.fill_task_name_field(task_name)
        task_page.click_save_task_btn()
        list_page.check_task_name_in_list(task_name)
