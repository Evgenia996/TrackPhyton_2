class Book:
    """ Базовый класс книги с неизменными name и author.
    """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook:
    """
    Бумажная книга с количеством страниц.
    """

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages  # вызовет setter с проверкой

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("pages должен быть целым числом")
        if value <= 0:
            raise ValueError("pages должен быть положительным числом")
        self._pages = value

    def __str__(self) -> str:
        base_str = super().__str__()
        return f"{base_str}, страниц: {self.pages}"


class AudioBook(Book):
    """
    Аудиокнига с продолжительностью.
    """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration  # вызовет setter с проверкой

        @property
        def duration(self) -> float:
            return self._duration

        @duration.setter
        def duration(self, value: float) -> None:
            if not isinstance(value, (float, int)):
                raise TypeError("duration должен быть числом")
            if value <= 0:
                raise ValueError("duration должен быть положительным числом")
            self._duration = float(value)

        def __str__(self) -> str:
            base_str = super().__str__()
            return f"{base_str}, длительность: {self.duration} часа(ов)"


# Проверка:
if__name__=="__main__":
# Создадим обьекты для теста
pb = PaperBook("Сто лет одиночества","Габриэль Гарсия Маркес",368)
print(repr(pb))
print(pb)
# Попытка задать неверное значение pages
try:
    pb.pages = -10
except Exception as e:
    print("Ошибка при присвоении pages:", e)

ab = AudioBook("Мастер и Маргарита", "Михаил Булгаков", 12.5)
    print(repr(ab))
    print(ab)
# Попытка задать неверное значение duration
    try:
        ab.duration = "двадцать"
    except Exception as e:
        print("Ошибка при присвоении duration:", e)

