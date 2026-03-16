# TODO Написать 3 класса с документацией и аннотацией типов

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
import doctest
from abc import ABC, abstractmethod


class Figure(ABC):
    """
    Абстрактный класс, представляющий геометрическую фигуру.
    Атрибуты:
    - color (str): цвет фигуры.
    - material (str): материал, из которого сделана фигура.
    """

    def __init__(self, color: str, material: str) -> None:
        """
        Инициализация фигуры с характеристиками.

        :param color: цвет фигуры.
        :param material: материал фигуры.
        :raises ValueError: если цвет или материал пустые строки.

        Примеры:
        >>> fig = Figure("red", "plastic")
        """
        if not isinstance(color, str):
            raise TypeError("Цвет должен быть строкой")
        if not isinstance(material, str):
            raise TypeError("Материал должен быть строкой")
        if not color:
            raise ValueError("Цвет не может быть пустым")
        if not material:
            raise ValueError("Материал не может быть пустым")
        self.color = color
        self.material = material

    @abstractmethod
    def area(self) -> float:
        """
        Расчет площади фигуры.
        :return: площадь в квадратных единицах.
        """
        ...

    @abstractmethod
    def perimeter(self) -> float:
        """
        Расчет периметра фигуры.
        :return: периметр.
        """
        ...

    def move(self, dx: float, dy: float) -> None:
        """
        Перемещение фигуры по координатам.

        :param dx: смещение по оси X.
        :param dy: смещение по оси Y.

        Примеры:
        >>> fig = Figure("blue", "wood")
        >>> fig.move(5, -3)
        """
        # Здесь мог бы быть код перемещения
        ...


class Transport(ABC):
    """
    Абстрактный класс, описывающий транспортное средство.

    Атрибуты:
    - max_speed (float): максимальная скорость.
    - weight (float): вес транспорта.
    """

    def __init__(self, max_speed: float, weight: float) -> None:
        """
        Инициализация транспортного средства.

        :param max_speed: максимальная скорость, должна быть положительным числом.
        :param weight: вес транспортного средства, дробное число.
        :raises ValueError: если speed или weight некорректны.

        Примеры:
        >>> t = Transport(120.5, 1500)
        """
        if not isinstance(max_speed, (int, float)):
            raise TypeError("max_speed должен быть числом")
        if max_speed <= 0:
            raise ValueError("max_speed должен быть положительным числом")
        if not isinstance(weight, (int, float)):
            raise TypeError("weight должен быть числом")
        self.max_speed = max_speed
        self.weight = weight

    @abstractmethod
    def start(self) -> None:
        """
        Запуск транспортного средства.
        """
        ...

    @abstractmethod
    def stop(self) -> None:
        """
        Остановка транспортного средства.
        """
        ...

    def fuel_consumption(self) -> float:
        """
        Расчет расхода топлива.

        :return: объем топлива.
        """
        # Заглушка
        return 0.0


class ElectronicDevice(ABC):
    """
    Абстрактный класс для электронной техники.

    Атрибуты:
    - brand (str): бренд устройства.
    - power (float): потребляемая мощность в ваттах.
    """

    def __init__(self, brand: str, power: float) -> None:
        """
        Инициализация устройства.

        :param brand: бренд.
        :param power: мощность в ваттах.
        :raises ValueError: если power отрицательное.

        Примеры:
        >>> device = ElectronicDevice("Samsung", 85.0)
        """
        if not isinstance(brand, str):
            raise TypeError("Бренд должен быть строкой")
        if not isinstance(power, (int, float)):
            raise TypeError("power должен быть числом")
        if power < 0:
            raise ValueError("Мощность не может быть отрицательной")
        self.brand = brand
        self.power = power

    def turn_on(self) -> None:
        """
        Включение устройства.
        """
        ...

    def turn_off(self) -> None:
        """
        Выключение устройства.
        """
        ...

    def get_power_usage(self, hours: float) -> float:
        """
        Расчет затрат энергии за указанное время.

        :param hours: количество часов.
        :return: сумма энергии в ватт-часах.
        :raises ValueError: если hours отрицательно.

        >>> device = ElectronicDevice("Apple", 10)
        >>> device.get_power_usage(5)
        """
        if not isinstance(hours, (int, float)):
            raise TypeError("hours должно быть числом")
        if hours < 0:
            raise ValueError("hours не может быть отрицательным")
        return self.power * hours


if __name__ == "__main__":
    doctest.testmod()