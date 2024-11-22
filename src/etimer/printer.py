class Printer:
    """Принтер
    Умеет печатать сообщения, перетирая предыдущее
    """
    
    def __init__(self) -> None:
        """Инициализация класса Printer"""
        self._last_message_length = 0

    def print(self, message: str, clear_previous: bool=False, end='\n') -> None:
        """Печать сообщения

        Args:
            message: Сообщение
            clear_previous: Флаг. Очистить предыдущее сообщение
            end: Конец строки
        """
        if clear_previous:
            self._clear_previous_message()
        message = message + end
        print(message, end='', flush=True)
        self._last_message_length = len(message)

    def _clear_previous_message(self) -> None:
        """Очистка предыдущего сообщения"""
        if not self._last_message_length:
            return
        self._remove_previous_message()
        self._move_caret_on_start_of_previous_message()

    def _remove_previous_message(self) -> None:
        """Удаление предыдущего сообщения"""
        self._move_caret_on_start_of_previous_message()
        print(' ' * self._last_message_length, end='')

    def _move_caret_on_start_of_previous_message(self) -> None:
        """Перемещение каретки на начало предыдущего сообщения"""
        print('\b' * self._last_message_length, end='', flush=True)

