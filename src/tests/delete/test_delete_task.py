import allure


@allure.feature("Удаление")
@allure.story("Удаление задачи")
class TestDeleteTask:
    @allure.title("Удаление выполненной задачи")
    @allure.description("Проверка удаления выполненной задачи")
    @allure.tag("delete")
    def test_delete_completed_task(self, main_page, list_page, create_task):
        list_page.click_last_task_checkbox()
        list_page.click_more_btn()
        list_page.click_delete_completed_tasks_btn()
        list_page.click_confirm_delete_tasks_btn()
        main_page.check_info_on_screen("There is nothing to do")
