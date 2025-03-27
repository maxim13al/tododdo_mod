from src.locators.base_locator import Locator


class ListLocators:
    ADD_TASK_BUTTON = Locator(
        value="//android.widget.ImageButton[@content-desc='New Task']",
        name="Кнопка 'Добавить задачу'",
    )
    HIDE_COMPLETED_TASKS_BUTTON = Locator(
        value="//android.widget.Button[@content-desc='Show/Hide completed tasks']",
        name="Кнопка 'Показывать выполненные задачи'",
    )
    MORE_BUTTON = Locator(
        value="//android.widget.ImageView[@content-desc='More options']",
        name="Кнопка 'Ещё'",
    )
    SEARCH_BUTTON = Locator(
        value="//android.widget.Button[@content-desc='Search']",
        name="Кнопка 'Поиск'",
    )
    SORT_BUTTON = Locator(
        value="//android.widget.Button[@content-desc='Sort']",
        name="Кнопка 'Сортировка'",
    )
    DELETE_LIST_BUTTON = Locator(
        value="//android.widget.TextView[@resource-id='com.mdev.tododo:id/title' and @text='Delete list']",
        name="Кнопка 'Удалить список'",
    )
    DELETE_COMPLETED_TASKS_BUTTON = Locator(
        value="//android.widget.TextView[@resource-id='com.mdev.tododo:id/title' and @text='Delete all completed tasks']",
        name="Кнопка 'Удалить выполненные задачи'",
    )
    CONFIRM_DELETE_TASKS_BUTTON = Locator(
        value="//android.widget.Button[@resource-id='com.mdev.tododo:id/bu_dialog_delete_all_completed_pos']",
        name="Кнопка 'Подтвердить удаление'",
    )
    RENAME_LIST_BUTTON = Locator(
        value="//android.widget.TextView[@resource-id='com.mdev.tododo:id/title' and @text='Rename list']",
        name="Кнопка 'Переименовать список'",
    )
    LAST_TASK_CHECKBOX = Locator(
        value="(//android.widget.CheckBox[@resource-id='com.mdev.tododo:id/check_box_completed'])[last()]",
        name="Чекбокс последней задачи в списке",
    )
    SEARCH_FIELD = Locator(
        value="//android.widget.EditText[@resource-id='com.mdev.tododo:id/search_src_text']",
        name="Поле 'Поиск'",
    )
    RENAME_LIST_FIELD = Locator(
        value="//android.widget.FrameLayout[@resource-id='com.mdev.tododo:id/custom']/android.widget.EditText",
        name="Поле 'Переименование списка'",
    )
    LIST_TITLE = Locator(
        value="//android.widget.ImageButton[@content-desc='Open navigation drawer']/following-sibling::android.widget.TextView",
        name="Название списка",
    )
    LAST_TASK = Locator(
        value="(//android.widget.LinearLayout[@resource-id='com.mdev.tododo:id/linearLayout'])[last()]",
        name="Последняя задача в списке",
    )
    LAST_TASK_TITLE = Locator(
        value="(//android.widget.LinearLayout[@resource-id='com.mdev.tododo:id/linearLayout'])[last()]/android.widget.TextView",
        name="Название последней задачи в списке",
    )
