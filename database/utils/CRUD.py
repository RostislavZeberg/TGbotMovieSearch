from typing import Dict, Union


class DatabaseFacade:
    """
    Класс описывающий действия с базой данных
    """
    def __init__(self, model) -> None:
        self.model = model

    def add(self, **kwargs) -> Dict:
        """Создает новую запись."""
        return self.model.create(**kwargs)

    def get_all(self) -> Dict:
        """Возвращает все записи."""
        return self.model.select()

    def get_by_telegram_id(self, telegram_id) -> Union[dict, None]:
        """Возвращает запись по telegram_id."""
        try:
            return self.model.get(self.model.telegram_id == telegram_id)
        except self.model.DoesNotExist:
            return None

    def delete(self, telegram_id) -> Union[dict, None]:
        """Удаление записей по telegram_id."""
        try:
            user = self.model.get(self.model.telegram_id == telegram_id)
            user.delete_instance()
        except self.model.DoesNotExist:
            return None

