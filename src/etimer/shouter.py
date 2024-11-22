from typing import Final
from etimer.printer import Printer
from etimer.timer import TimerRun


class Shouter:
    """Рупор
    Отвечает за объявления о состоянии таймера

    Attributes:
        SAY_ABOUT_PASSED_TIME_PERIOD: Период объявления о прошедшем времени
    """

    SAY_ABOUT_PASSED_TIME_PERIOD: Final[int] = 3

    def __init__(self, timer: TimerRun) -> None:
        """Инициализация класса Shouter

        Args:
            timer: Таймер
        """
        self._timer = timer
        self._printer = Printer()

    @property
    def _time_passed_after_last_say(self) -> float:
        """Количество секунд, прошедших после последнего объявления о прошедшем времени"""
        return self._timer.passed - self._last_state_said_at

    @property
    def _has_time_come_to_say_about_passed_time(self) -> bool:
        """Настало ли время объявить о прошедшем времени"""
        return self._time_passed_after_last_say >= self.SAY_ABOUT_PASSED_TIME_PERIOD

    def say_about_start(self) -> None:
        """Объявить о начале"""
        self._printer.print(f'Засекаю {self._timer.duration} сек.')
        self._printer.print('...')

    def say_about_passed_time_if_time_has_come(self) -> None:
        """Объявить о прошедшем времени"""
        if not self._has_time_come_to_say_about_passed_time:
            return
        message = f'Прошло {int(self._timer.passed)} сек.'
        self._printer.print(message, clear_previous=True, end='')
        self._last_state_said_at = self._timer.passed

    def say_time_is_over(self) -> None:
        """Объявить о завершении"""
        self._printer.print('\nВремя вышло!')

