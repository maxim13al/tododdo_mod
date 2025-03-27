import subprocess
from appium.webdriver.common.appiumby import AppiumBy


class DeviceActions:
    def __init__(self, driver):
        """
        Инициализация класса с драйвером и логгером
        """
        self.driver = driver
        self.logger = driver.logger

    def rotate_screen(self, orientation="LANDSCAPE"):
        """
        Меняет ориентацию экрана
        """
        try:
            self.driver.orientation = orientation
            self.logger.info(f"Экран повернут в {orientation}")
        except Exception as e:
            self.logger.error(f"Ошибка при изменении ориентации экрана: {e}")

    def lock_device(self):
        """
        Блокирует устройство
        """
        try:
            self.driver.lock()
            self.logger.info("Устройство заблокировано")
        except Exception as e:
            self.logger.error(f"Ошибка при блокировке устройства: {e}")

    def unlock_device(self):
        """
        Разблокирует устройство
        """
        try:
            self.driver.unlock()
            self.logger.info("Устройство разблокировано")
        except Exception as e:
            self.logger.error(f"Ошибка при разблокировке устройства: {e}")

    def adb_command(self, command):
        """
        Выполняет ADB-команду и возвращает результат
        """
        try:
            result = subprocess.run(
                ["adb", "shell"] + command.split(),
                capture_output=True,
                text=True,
            )
            output = result.stdout.strip()
            self.logger.info(f"ADB команда: {command} -> {output}")
            return output
        except Exception as e:
            self.logger.error(
                f"Ошибка при выполнении ADB команды '{command}': {e}"
            )
            return None

    def swipe(self, start_x, start_y, end_x, end_y, duration=800):
        """
        Свайп по экрану
        """
        try:
            self.driver.swipe(start_x, start_y, end_x, end_y, duration)
            self.logger.info(
                f"Свайп: ({start_x}, {start_y}) -> ({end_x}, {end_y}), длительность {duration} мс"
            )
        except Exception as e:
            self.logger.error(f"Ошибка при свайпе: {e}")

    def scroll_to_text(self, text):
        """
        Скролл до текста на странице
        """
        try:
            element = self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("{text}"))',
            )
            self.logger.info(f"Скролл до текста: {text}")
            return element
        except Exception as e:
            self.logger.error(f"Ошибка при скролле до текста '{text}': {e}")
            return None

    def back(self):
        """
        Нажатие кнопки 'Назад' на устройстве
        """
        try:
            self.driver.back()
            self.logger.info("Нажата кнопка 'Назад'")
        except Exception as e:
            self.logger.error(f"Ошибка при нажатии кнопки 'Назад': {e}")
