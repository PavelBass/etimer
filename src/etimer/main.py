import time
import argparse

SLEEP_TIME = 0.1  # seconds
SAY_SPENT_TIME_PERIOD = 3  # seconds


def etimer(seconds: int) -> None:
    wait_for(seconds=seconds)


def wait_for(seconds: int) -> None:
    print(f'Засекаю {seconds} сек.')
    print('...')
    started_at = time.time()
    last_state_said_at = 0
    last_message_length = 0
    while (time_passed := time.time() - started_at) < seconds:
        if time_passed - last_state_said_at > SAY_SPENT_TIME_PERIOD:
            if last_message_length:
                print('\b' * last_message_length, end='')
                print(' ' * last_message_length, end='')
                print('\b' * last_message_length, end='', flush=True)
            message = f'Прошло {int(time.time() - started_at)} сек.'
            print(message, end='', flush=True)
            last_state_said_at = time_passed
            last_message_length = len(message)
        time.sleep(SLEEP_TIME)
    print('\nВремя вышло!')
