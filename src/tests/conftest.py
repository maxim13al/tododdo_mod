import pytest
from src.pages.main_page import MainPage
from src.pages.menu_page import MenuPage
from src.pages.list_page import ListPage
from src.pages.task_page import TaskPage
from src.helpers.fake_data import fake_data


@pytest.fixture()
def main_page(driver):
    yield MainPage(driver)


@pytest.fixture()
def menu_page(driver):
    yield MenuPage(driver)


@pytest.fixture()
def list_page(driver):
    yield ListPage(driver)


@pytest.fixture()
def task_page(driver):
    yield TaskPage(driver)


@pytest.fixture()
def create_list(main_page, menu_page, list_page):
    list_name = fake_data.get_fake_list_name()
    main_page.click_open_menu_btn()
    menu_page.click_add_list_btn()
    menu_page.fill_list_name_field(list_name)
    main_page.click_ok_btn()
    yield


@pytest.fixture()
def create_task(list_page, task_page, create_list):
    task_name = fake_data.get_fake_list_name()
    list_page.click_add_task_btn()
    task_page.fill_task_name_field(task_name)
    task_page.click_save_task_btn()
    yield
