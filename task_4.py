if __name__ == "__main__":
    # Write your solution here
    pass
from typing import Dict, Any
class SocialNetwork:
    """
    Базовый класс для социальных сетей.
    """
    def __init__(self, name: str, user_count: int) -> None:
        """
        Инициализация социальная сети.
        :param name: Название сети.
        :param user_count: Количество зарегистрированных пользователей.
        """
        self._name = name  # Защищённый атрибут — название соцсети
        self._user_count = user_count  # Защищённый атрибут — число пользователей

    def __str__(self) -> str:
        """
        Возвращает краткое описание объекта.
        """
        return f"Социальная сеть: {self._name}, Пользователей: {self._user_count}"

    def __repr__(self) -> str:
        """
        Возвращает строку, которая может быть использована для воспроизведения объекта.
        """
        return f"SocialNetwork(name='{self._name}', user_count={self._user_count})"

    def get_user_info(self, user_id: int) -> Dict[str, Any]:
        """
        Получение информации о пользователе по ID.
        :param user_id: ID пользователя.
        :return: словарь с информацией о пользователе.
        """
        # В реальности бы сюда подключился API соцсети.
        return {"user_id": user_id, "name": "Иван", "status": "активен"}


class VK(SocialNetwork):
    """
    Класс reprezent' отношения VK, наследника SocialNetwork.
    """

    def __init__(self, user_count: int, vk_group_id: str) -> None:
        """
        Инициализация VK с расширенными атрибутами.
        :param user_count: Количество пользователей.
        :param vk_group_id: ID группы VK.
        """
        super().__init__(name="VK", user_count=user_count)
        self.__vk_group_id = vk_group_id  # приватный атрибут для ID группы VK

    def __str__(self) -> str:
        """
        Возвращает описание VK, расширяя базовый метод __str__.
        """
        base_desc = super().__str__()
        return f"{base_desc}, Группа VK ID: {self.__vk_group_id}"

    def __repr__(self) -> str:
        """
        Возвращает строку воспроизведения объекта VK.
        """
        return f"VK(user_count={self._user_count}, vk_group_id='{self.__vk_group_id}')"

    def get_user_info(self, user_id: int) -> Dict[str, Any]:
        """
        Получение информации о пользователе в VK.
        Этот метод расширяет базовый, добавляя конкретные детали VK.
        :param user_id: ID пользователя.
        :return: словарь с подробной информацией.
        """
        # В реальности API VK для получения информации пользователя
        user_info = super().get_user_info(user_id)
        user_info.update({"VK_specific": "Информация о VK"})
        return user_info

    def set_vk_group_id(self, new_id: str) -> None:
        """
        Метод для обновления ID группы VK.
        :param new_id: Новый идентификатор группы.
        """
        self.__vk_group_id = new_id


class Facebook(SocialNetwork):
    """
    Класс представляющий Facebook и наследующий от SocialNetwork.
    """

    def __init__(self, user_count: int, page_name: str) -> None:
        """
        Инициализация Facebook-страницы.
        :param user_count: Количество пользователей.
        :param page_name: Название страницы.
        """
        super().__init__(name="Facebook", user_count=user_count)
        self._page_name = page_name  # защищённый атрибут

    def __str__(self) -> str:
        """
        Расширенный метод __str__, показывающий название страницы.
        """
        base_desc = super().__str__()
        return f"{base_desc}, Страница: {self._page_name}"

    def __repr__(self) -> str:
        """
        Воспроизводимый формат объекта.
        """
        return f"Facebook(user_count={self._user_count}, page_name='{self._page_name}')"

    def get_user_info(self, user_id: int) -> Dict[str, Any]:
        """
        Получение информации о пользователе в Facebook.
        Расширение базового метода.
        :param user_id: ID пользователя.
        :return: словарь.
        """
        user_info = super().get_user_info(user_id)
        user_info.update({"Facebook_specific": "Информация о Facebook"})
        return user_info

    def update_page_name(self, new_name: str) -> None:
        """
        Метод обновления названия страницы.
        :param new_name: новое название.
        """
        self._page_name = new_name


if __name__ == "__main__":
    # Создаем объекты соцсетей
    vk_network = VK(user_count=1500000, vk_group_id="group_12345")
    fb_network = Facebook(user_count=300000, page_name="MyPage")

    # Вывод информации о них
    print(vk_network)
    print(repr(vk_network))
    print(fb_network)
    print(repr(fb_network))

    # Используем расширенные методы get_user_info
    print(vk_network.get_user_info(42))
    print(fb_network.get_user_info(42))

    # Обновляем внутренние состояния
    vk_network.set_vk_group_id("new_group_id")
    fb_network.update_page_name("NewPageName")

    # Еще раз выводим для проверки изменений
    print(vk_network)
    print(fb_network)