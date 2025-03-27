import allure
from src.pages.base_page import BasePage
from src.locators.main_locator import MainLocators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Нажать на кнопку 'Открыть меню'")
    def click_open_menu_btn(self) -> None:
        """
        Нажать на кнопку 'Открыть меню'
        :return:
        """
        self.click(MainLocators.OPEN_MENU_BUTTON)

    @allure.step("Нажать на кнопку 'Отменить действие'")
    def click_cancel_btn(self) -> None:
        """
        Нажать на кнопку 'Отменить действие'
        :return:
        """
        self.click(MainLocators.CANCEL_BUTTON)

    @allure.step("Нажать на кнопку 'Подтвердить действие'")
    def click_ok_btn(self) -> None:
        """
        Нажать на кнопку 'Подтвердить дейстиве'
        :return:
        """
        self.click(MainLocators.OK_BUTTON)

    @allure.step("")
    def check_info_on_screen(self, value: str) -> None:
        """
        Проверка информации на экране
        """
        info_about_list = self.get_text(MainLocators.INFO_ON_SCREEN)
        assert value == info_about_list, (
            f"Информация на экране не соответствует ожидаемому: {info_about_list} != {value}"
        )
