import time
import argparse


def main() -> None:
    seconds = get_time_to_wait()
    wait_for(seconds=seconds)


def get_time_to_wait() -> int:
    parser = argparse.ArgumentParser(
        prog='etimer',
        description='Консольный таймер',
        epilog='Время не ждёт',    
    )
    parser.add_argument('seconds', type=int, help='Количество секунд')
    arguments = parser.parse_args()
    return arguments.seconds


def wait_for(seconds: int) -> None:
    print(f'Засекаю {seconds} сек.')
    print('...')
    time.sleep(seconds)
    print('Время вышло!')


if __name__ == '__main__':
    main()

