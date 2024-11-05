import time
import argparse


def etimer(seconds: int) -> None:
    wait_for(seconds=seconds)


def wait_for(seconds: int) -> None:
    print(f'Засекаю {seconds} сек.')
    print('...')
    time.sleep(seconds)
    print('Время вышло!')

