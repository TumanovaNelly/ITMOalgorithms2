import tracemalloc
from time import time

RESET = '\033[0m'  # Сброс цвета
RED = '\033[31m'  # Красный
GREEN = '\033[32m'  # Зеленый
YELLOW = '\033[33m'  # Желтый
BLUE = '\033[34m'  # Синий
MAGENTA = '\033[35m'  # Фиолетовый
CYAN = '\033[36m'  # Голубой
GREY = '\033[37m'  # Серый


def tested_time_memory(func):
    def wrapper(*args, **kwargs):
        tracemalloc.start()

        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        elapsed_time = end_time - start_time

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        print(f"{MAGENTA}Время выполнения функции:{RESET} {elapsed_time:.6f} {MAGENTA}сек.{RESET}")
        print(f"{MAGENTA}Пиковое использование памяти:{RESET} {peak / 1024:.2f} {MAGENTA}KB{RESET}")
        print(f"{MAGENTA}————————————————————————————————————{RESET}")

        return result

    return wrapper
