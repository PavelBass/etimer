import time


class TimerRun:
    """Таймер"""

    def __init__(self, duration: int) -> None:
        """Инициализация класса TimerRun

        Args:
            duration: Длительность таймера в секундах
        """
        self.duration = duration
        self._started_at = None

    @property
    def started_at(self) -> float | None:
        """Время запуска таймера"""
        return self._started_at

    @property
    def passed(self) -> float:
        """Прошедшее время"""
        if not self.is_started:
            return 0
        if self.is_finished:
            return self.duration
        return time.time() - self.started_at

    def start(self) -> None:
        """Запуск"""
        self._started_at = time.time()

    @property
    def is_started(self) -> bool:
        """Запущен ли таймер"""
        return self.started_at is not None

    @property
    def is_finished(self) -> bool:
        """Завершён ли таймер"""
        return self.is_started and time.time() - self.started_at >= self.duration

