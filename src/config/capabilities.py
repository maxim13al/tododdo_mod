from appium.options.android import UiAutomator2Options
from src.config import config


def get_capabilities(device_type: str, server: str) -> UiAutomator2Options:
    """
    Возвращает опции для подключения к Appium в зависимости от устройства и сервера.

    :param device_type: Тип устройства ('emulator' или 'real')
    :param server: Сервер для тестирования ('local' или 'remote')
    :return: UiAutomator2Options
    """
    options = UiAutomator2Options()

    options.automation_name = config.AUTOMATION_NAME
    options.platform_name = config.PLATFORM_NAME
    options.app_package = config.APP_PACKAGE
    options.app_activity = config.APP_ACTIVITY
    options.new_command_timeout = config.NEW_COMMAND_TIMEOUT

    if server == "remote_server":
        options.browserstack_user = config.BS_USER_NAME
        options.browserstack_key = config.BS_ACCESS_KEY
        options.app = config.BS_APP_ID
        options.device_name = config.BS_DEVICE_NAME
        options.os_version = config.BS_OS_VERSION
        options.project = config.BS_PROJECT_NAME
        options.build = config.BS_BUILD_NAME
        options.name = config.BS_NAME
    else:
        if device_type == "emulator":
            options.device_name = config.EMULATOR_DEVICE_NAME
            options.avd = config.EMULATOR_AVD
        else:
            options.device_name = config.REAL_DEVICE_NAME

    return options
