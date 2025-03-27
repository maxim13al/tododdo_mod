from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver, timeout=10) -> None:
        """
        Инициализация страницы

        :param driver: экземпляр WebDriver
        :param timeout: время ожидания элементов по умолчанию
        """
        self.driver = driver
        self.logger = driver.logger
        self.wait = WebDriverWait(driver, timeout)

    def get_locator(self, locator):
        """
        Возвращает локатор в формате кортежа (by, value) для использования в Selenium.

        :param locator: объект Locator с полями by и value.
        :return: кортеж (by, value).
        """
        if not hasattr(locator, "by") or not hasattr(locator, "value"):
            raise ValueError(
                "Некорректный локатор. Ожидается объект с атрибутами 'by' и 'value'."
            )
        return (locator.by, locator.value)

    def find_element(self, locator, timeout=None):
        """
        Ожидает появления элемента и возвращает его

        :param locator: локатор элемента
        :param timeout: время ожидания"""
        _locator = self.get_locator(locator)
        try:
            self.logger.debug(f"Поиск элемента по локатору: {_locator}")
            return self.wait.until(EC.visibility_of_element_located(_locator))
        except Exception as e:
            self.logger.error(
                f"Элемент по локатору: {_locator} не найден за {timeout or self.wait._timeout} секунд."
            )
            raise e

    def find_elements(self, locator, timeout=None):
        """
        Ожидает появления элементов и возвращает список

        :param locator: локатор элемента
        :param timeout: время ожидания
        """
        _locator = self.get_locator(locator)
        try:
            self.logger.debug(f"Поиск элементов по локатору: {_locator}")
            return self.wait.until(
                EC.visibility_of_all_elements_located(locator)
            )

        except Exception as e:
            self.logger.error(
                f"Элементы по локатору: {locator} не найдены за {timeout or self.wait._timeout} секунд."
            )
            raise e

    def click(self, locator):
        """
        Находит элемент и кликает по нему

        :param locator: локатор элемента
        """
        element = self.find_element(locator)
        if element:
            self.logger.debug(f"Клик по локатору: {locator}")
            element.click()

    def send_keys(self, locator, text, clear_first=True):
        """
        Находит поле ввода и отправляет туда текст

        :param locator: локатор поля ввода
        :param text: текст, который будет отправлен
        :param clear_first: очистить поле перед отправлением текста
        """
        element = self.find_element(locator)
        if element:
            if clear_first:
                element.clear()
            self.logger.debug(
                f"Отправка текста: {text} по локатору: {locator}"
            )
            element.send_keys(text)

    def get_text(self, locator):
        """
        Получает текст элемента

        :param locator: локатор элемента
        """
        element = self.find_element(locator)
        self.logger.debug(f"Получение текста по локатору: {locator}")
        return element.text if element else None

    def is_element_visible(self, locator, timeout=5):
        """
        Проверяет, видим ли элемент на странице

        :param locator: локатор элемента
        :param timeout: время ожидания
        """
        try:
            self.logger.debug(
                f"Проверка видимости элемента по локатору: {locator}"
            )
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            self.logger.error(f"Элемент по локатору: {locator} не виден.")
            return False
