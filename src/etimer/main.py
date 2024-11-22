import time
from typing import Final

from etimer.shouter import Shouter
from etimer.timer import TimerRun


class ETimer:
    """Приложение Etimer

    Attributes:
        SLEEP_TIME: Время между проверками на то, что время вышло, в секундах
    """

    SLEEP_TIME: Final[float] = 0.1 


    def __init__(self, seconds: int) -> None:
        """Инициализация класса ETimer

        Args:
            seconds: Количество секунд
        """
        self._timer = TimerRun(seconds)
        self._shouter = Shouter(self._timer)

    def run(self) -> None:
        """Запуск"""
        self._shouter.say_about_start()
        while not self._timer.is_finished:
            self._shouter.say_about_passed_time_if_time_has_come()
            time.sleep(self.SLEEP_TIME)
        self._shouter.say_time_is_over()

