import os
import allure
from src.helpers.logging import get_project_root


def attach_screenshot(driver, test_name: str) -> None:
    """
    Делает скриншот и прикрепляет его к Allure-отчету
    """
    screenshot_dir = os.path.join(get_project_root(), "screenshots")
    os.makedirs(screenshot_dir, exist_ok=True)
    screenshot_path = os.path.join(screenshot_dir, f"{test_name}.png")

    driver.save_screenshot(screenshot_path)

    with open(screenshot_path, "rb") as image:
        allure.attach(
            image.read(),
            name=f"Failure Screenshot: {test_name}",
            attachment_type=allure.attachment_type.PNG,
        )
