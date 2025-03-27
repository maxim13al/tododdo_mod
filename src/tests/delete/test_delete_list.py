import allure


@allure.feature("Удаление")
@allure.story("Удаление списка")
class TestDeleteList:
    @allure.title("Удаление списка")
    @allure.description("Проверка удаления списка")
    @allure.tag("delete")
    def test_delete_list(self, main_page, menu_page, list_page, create_list):
        list_page.click_more_btn()
        list_page.click_delete_list_btn()
        main_page.click_ok_btn()
        main_page.check_info_on_screen("There are no lists yet")
