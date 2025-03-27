import allure
from src.helpers.fake_data import fake_data


@allure.feature("Падение тестов")
@allure.story("Проваленные тесты")
class TestFailedList:
    @allure.title("Проваленное изменение названия списка")
    @allure.description("Проверка изменения названия списка с ошибкой")
    @allure.tag("failed")
    def test_failed_rename(self, main_page, menu_page, list_page, create_list):
        list_name = fake_data.get_fake_list_name()
        list_page.click_more_btn()
        list_page.click_rename_list_btn()
        list_page.fill_rename_list_field(list_name)
        main_page.click_ok_btn()
        list_page.check_list_title('Failed')
