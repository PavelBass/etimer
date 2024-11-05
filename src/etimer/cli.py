import argparse

from etimer import etimer


def get_parser() -> int:
    parser = argparse.ArgumentParser(
        prog='etimer',
        description='Консольный таймер',
        epilog='Время не ждёт',    
    )
    parser.add_argument('seconds', type=int, help='Количество секунд')
    return parser


def main() -> None:
    parser = get_parser()
    arguments = parser.parse_args()
    etimer(seconds=seconds)

