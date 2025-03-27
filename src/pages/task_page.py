import allure
from src.pages.base_page import BasePage
from src.locators.task_locator import TaskLocators


class TaskPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Нажать на кнопку 'Сохранить задачу'")
    def click_save_task_btn(self) -> None:
        """
        Нажать на кнопку 'Сохранить задачу'
        :return:
        """
        self.click(TaskLocators.SAVE_TASK_BUTTON)

    @allure.step("Заполнить поле 'Название задачи' значением '{value}'")
    def fill_task_name_field(self, value: str) -> None:
        """
        Заполнить поле 'Название задачи' значением '{value}'
        :return:
        """
        self.send_keys(TaskLocators.NEW_TASK_NAME_FIELD, value)

    @allure.step("")
    def check_task_title_in_task_card(self, value: str) -> None:
        """

        :return:
        """
        task_title = self.get_text(TaskLocators.NEW_TASK_NAME_FIELD)
        assert value == task_title, (
            f"Название задачи не соответствует ожидаемому: {value} != {task_title}"
        )
