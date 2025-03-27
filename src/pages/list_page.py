import allure
from src.pages.base_page import BasePage
from src.locators.list_locator import ListLocators


class ListPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Нажать на кнопку 'Добавить задачу'")
    def click_add_task_btn(self) -> None:
        """
        Нажать на кнопку 'Добавить задачу'
        :return:
        """
        self.click(ListLocators.ADD_TASK_BUTTON)

    @allure.step("Нажать на кнопку 'Добавить задачу'")
    def click_add_task_btn(self) -> None:
        """
        Нажать на кнопку 'Добавить задачу'
        :return:
        """
        self.click(ListLocators.ADD_TASK_BUTTON)

    @allure.step("Нажать на кнопку 'Еще'")
    def click_more_btn(self) -> None:
        """
        Нажать на кнопку 'Еще'
        :return:
        """
        self.click(ListLocators.MORE_BUTTON)

    @allure.step("Нажать на кнопку 'Удалить список'")
    def click_delete_list_btn(self) -> None:
        """
        Нажать на кнопку 'Удалить список'
        :return:
        """
        self.click(ListLocators.DELETE_LIST_BUTTON)

    @allure.step("Нажать на кнопку 'Удалить выполненные задачи'")
    def click_delete_completed_tasks_btn(self) -> None:
        """
        Нажать на кнопку 'Удалить выполненные задачи'
        :return:
        """
        self.click(ListLocators.DELETE_COMPLETED_TASKS_BUTTON)

    @allure.step("Подтвердить удаление задач")
    def click_confirm_delete_tasks_btn(self) -> None:
        """
        Подтвердить удаление задач
        :return:
        """
        self.click(ListLocators.CONFIRM_DELETE_TASKS_BUTTON)

    @allure.step("Нажать на кнопку 'Переименовать список'")
    def click_rename_list_btn(self) -> None:
        """
        Нажать на кнопку 'Переименовать список'
        :return:
        """
        self.click(ListLocators.RENAME_LIST_BUTTON)

    @allure.step("Нажать на кнопку 'Скрыть выполненные задачи'")
    def click_hide_completed_tasks_btn(self) -> None:
        """
        Нажать на кнопку 'Скрыть выполненные задачи'
        :return:
        """
        self.click(ListLocators.HIDE_COMPLETED_TASKS_BUTTON)

    @allure.step("Нажать на чекбокс последней задачи в списке")
    def click_last_task_checkbox(self) -> None:
        """
        Нажать на чекбокс последней задачи в списке
        :return:
        """
        self.click(ListLocators.LAST_TASK_CHECKBOX)

    @allure.step("Заполнить поле 'Переименование списка' значением '{value}'")
    def fill_rename_list_field(self, value: str) -> None:
        """
        Заполнить поле 'Переименование списка' значением '{value}'
        :param value:
        :return:
        """
        self.send_keys(ListLocators.RENAME_LIST_FIELD, value)

    @allure.step("Открыть последнюю задачу в списке")
    def open_last_task(self) -> None:
        """
        Открыть последнюю задачу в списке
        :return:
        """
        self.click(ListLocators.LAST_TASK)

    @allure.step("Проверка названия списка '{value}'")
    def check_list_title(self, value: str) -> None:
        """
        Проверка названия списка
        :param value:
        :return:
        """
        list_title = self.get_text(ListLocators.LIST_TITLE)
        assert value == list_title, (
            f"Название списка не соответствует ожидаемому: {value} != {list_title}"
        )

    @allure.step("Проверка названия задачи в списке '{value}'")
    def check_task_name_in_list(self, value: str) -> None:
        """
        Проверка названия задачи в списке
        :param value:
        :return:
        """
        list_title = self.get_text(ListLocators.LAST_TASK_TITLE)
        assert value == list_title, (
            f"Название задачи не соответствует ожидаемому: {value} != {list_title}"
        )
