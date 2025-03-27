from src.locators.base_locator import Locator


class TaskLocators:
    SAVE_TASK_BUTTON = Locator(
        value="//android.widget.ImageButton[@resource-id='com.mdev.tododo:id/fab_save_task']",
        name="Кнопка 'Сохранить задачу'",
    )

    NEW_TASK_NAME_FIELD = Locator(
        value="//android.widget.EditText[@resource-id='com.mdev.tododo:id/et_task_name']",
        name="Поле 'Название задачи'",
    )
