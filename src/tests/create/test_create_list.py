import allure
from src.helpers.fake_data import fake_data


@allure.feature("Создание")
@allure.story("Создание списка")
class TestCreateList:
    @allure.title("Создание нового списка")
    @allure.description("Проверка создания нового списка")
    @allure.tag("create", "smoke")
    def test_create_list(self, main_page, menu_page, list_page):
        list_name = fake_data.get_fake_list_name()
        main_page.click_open_menu_btn()
        menu_page.click_add_list_btn()
        menu_page.fill_list_name_field(list_name)
        main_page.click_ok_btn()
        list_page.check_list_title(list_name)
