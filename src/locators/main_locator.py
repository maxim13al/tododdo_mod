from src.locators.base_locator import Locator


class MainLocators:
    OPEN_MENU_BUTTON = Locator(
        value="//android.widget.ImageButton[@content-desc='Open navigation drawer']",
        name="Кнопка 'Меню'",
    )
    CANCEL_BUTTON = Locator(
        value="//android.widget.Button[@resource-id='android:id/button2']",
        name="Кнопка 'Отменить действие'",
    )
    OK_BUTTON = Locator(
        value="//android.widget.Button[@resource-id='android:id/button1']",
        name="Кнопка 'Подтвердить действие'",
    )
    INFO_ON_SCREEN = Locator(
        value="//android.widget.TextView[@resource-id='com.mdev.tododo:id/tv_frmnt_task_illustration_text1']",
        name="Информация на экране",
    )
