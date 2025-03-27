from src.locators.base_locator import Locator


class MenuLocators:
    ALL_TASKS_BUTTON = Locator(
        value="//android.widget.TextView[@resource-id='com.mdev.tododo:id/tv_nav_draw_all_tasks']",
        name="Кнопка 'Все задачи'",
    )
    TODAY_BUTTON = Locator(
        value="//android.widget.TextView[@resource-id='com.mdev.tododo:id/tv_nav_draw_today']",
        name="Кнопка 'Сегодня'",
    )
    UPCOMING_BUTTON = Locator(
        value="//android.widget.TextView[@resource-id='com.mdev.tododo:id/tv_nav_draw_upcoming']",
        name="Кнопка 'Завтра'",
    )
    CURRENT_WEEK_BUTTON = Locator(
        value="//android.widget.TextView[@resource-id='com.mdev.tododo:id/tv_nav_draw_currweek']",
        name="Кнопка 'Текущая неделя'",
    )
    PRIORITIZED_BUTTON = Locator(
        value="//android.widget.RelativeLayout[@resource-id='com.mdev.tododo:id/ly_nav_draw_important']",
        name="Кнопка 'Приоритет'",
    )
    OVERDUE_BUTTON = Locator(
        value="//android.widget.TextView[@resource-id='com.mdev.tododo:id/tv_nav_draw_overdue']",
        name="Кнопка 'Просроченные'",
    )
    CALENDAR_BUTTON = Locator(
        value="//android.widget.RelativeLayout[@resource-id='com.mdev.tododo:id/ly_nav_draw_calendar']",
        name="Кнопка 'Календарь'",
    )
    ADD_NEW_LIST_BUTTON = Locator(
        value="//android.widget.TextView[@resource-id='com.mdev.tododo:id/tv_nav_draw_newlist']",
        name="Кнопка 'Новый список'",
    )
    UPGRADE_TO_PRO_BUTTON = Locator(
        value="//android.widget.TextView[@resource-id='com.mdev.tododo:id/tv_nav_draw_buy_pro']",
        name="Кнопка 'Обновить до PRO'",
    )
    TRASH_BUTTON = Locator(
        value="//android.widget.TextView[@resource-id='com.mdev.tododo:id/tv_nav_draw_trash']",
        name="Кнопка 'Корзина'",
    )
    INFO_AND_TIPS_BUTTON = Locator(
        value="//android.widget.TextView[@resource-id='com.mdev.tododo:id/tv_nav_draw_about']",
        name="Кнопка 'Информация и советы'",
    )
    SETTINGS_BUTTON = Locator(
        value="//android.widget.TextView[@resource-id='com.mdev.tododo:id/tv_nav_draw_settings']",
        name="Кнопка 'Настройки'",
    )

    NEW_LIST_NAME_FIELD = Locator(
        value="//android.widget.EditText[@text='New list']",
        name="Поле 'Название списка'",
    )

    LAST_LIST = Locator(
        value="(//android.widget.TextView[@resource-id='com.mdev.tododo:id/tv_list_name'])[last()]",
        name="Последний список",
    )
