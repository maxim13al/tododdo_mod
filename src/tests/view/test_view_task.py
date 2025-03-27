import allure


@allure.feature("Отображение")
@allure.story("Отображение задачи")
class TestDeleteTask:
    @allure.title("Отсутствие отображения выполненной задачи")
    @allure.description("Проверка отсутствия отображения выполненной задачи")
    @allure.tag("delete")
    def test_no_display_completed_task(
        self, main_page, list_page, create_task
    ):
        list_page.click_last_task_checkbox()
        list_page.click_hide_completed_tasks_btn()
        main_page.check_info_on_screen("There is nothing to do")
