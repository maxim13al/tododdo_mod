import allure
from src.helpers.fake_data import fake_data


@allure.feature("Отображение")
@allure.story("Отображение списка")
class TestViewList:
    @allure.title("Отображение созданного списка в меню")
    @allure.description("Проверка отображения созданного списка в меню")
    @allure.tag("view")
    def test_display_created_list_in_menu(self, driver, main_page, menu_page):
        list_name = fake_data.get_fake_list_name()
        main_page.click_open_menu_btn()
        menu_page.click_add_list_btn()
        menu_page.fill_list_name_field(list_name)
        main_page.click_ok_btn()
        main_page.click_open_menu_btn()
        menu_page.check_display_list_in_menu(list_name)
