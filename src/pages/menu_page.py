import allure
from src.pages.base_page import BasePage
from src.locators.menu_locator import MenuLocators


class MenuPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Нажать на кнопку 'Добавить новый список'")
    def click_add_list_btn(self) -> None:
        """
        Нажать на кнопку 'Добавить новый список'
        :return:
        """
        self.click(MenuLocators.ADD_NEW_LIST_BUTTON)

    @allure.step("Нажать на кнопку 'Создать'")
    def click_create_btn(self) -> None:
        """
        Нажать на кнопку 'Создать'
        :return:
        """
        self.click(MenuLocators.CREATE_BUTTON)

    @allure.step("Заполнить поле 'Название списка' значением '{value}'")
    def fill_list_name_field(self, value: str) -> None:
        """
        Заполнить поле 'Название списка' значением '{value}'
        :param value:
        :return:
        """
        self.send_keys(MenuLocators.NEW_LIST_NAME_FIELD, value)

    @allure.step("Проверка отображения списка в меню")
    def check_display_list_in_menu(self, value: str) -> None:
        """
        Проверка отображения списка в меню
        :param value:
        :return:
        """
        name_list_in_menu = self.get_text(MenuLocators.LAST_LIST)
        assert value == name_list_in_menu, (
            f"Название спика '{value}' не совпадает с названием в меню '{name_list_in_menu}'"
        )
