from appium.webdriver.common.appiumby import AppiumBy
from pydantic import BaseModel, Field, ConfigDict, field_validator
from typing import Optional, Literal


class Locator(BaseModel):
    """
    Класс для представления и работы с локаторами элементов на веб-странице.
    Допускается только использование локаторов типа XPATH.

    :param by: Тип локатора (по умолчанию XPATH).
    :param value: Строка локатора (XPath).
    :param name: Описание локатора (необязательно).
    """

    model_config = ConfigDict(arbitrary_types_allowed=True)

    by: Literal[AppiumBy.XPATH] = Field(
        default=AppiumBy.XPATH,
        description="Тип локатора, разрешён только XPATH.",
    )
    value: str = Field(..., description="Строка локатора в формате XPath.")
    name: Optional[str] = Field(default=None, description="Описание локатора.")

    @field_validator("by")
    def validate_by(cls, v):
        """Валидация типа локатора. Разрешён только XPATH."""
        if v != AppiumBy.XPATH:
            raise ValueError(
                f"Неподдерживаемый тип локатора: {v}. Разрешён только XPATH."
            )
        return v

    def __repr__(self):
        """Упрощённое строковое представление объекта Locator."""
        return f"<Locator name='{self.name}' value='{self.value}'>"

    def format(self, *args, **kwargs):
        """
        Возвращает новый объект Locator с отформатированным значением.

        :param args: Позиционные аргументы для форматирования.
        :param kwargs: Именованные аргументы для форматирования.
        :return: Новый объект Locator с обновлённым значением.
        """
        return Locator(
            by=self.by,
            value=self.value.format(*args, **kwargs),
            name=self.name,
        )
