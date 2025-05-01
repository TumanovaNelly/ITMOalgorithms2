from typing import List, Tuple

from utils import tested_time_memory


class HashedString:
    __prev_hashes: List[int]
    __parameter: int = 31

    @property
    def MOD(self) -> int:
        return 1000000007

    def __init__(self, string: str):
        self.__prev_hashes = self.__polynomial_prev_hashes(string)

    def __polynomial_prev_hashes(self, string: str) -> List[int]:
        offset = ord('a') - 1
        hashes = [0] * (len(string) + 1)

        for i in range(len(string)):
            hashes[i + 1] = (hashes[i] * self.__parameter + ord(string[i]) - offset) % self.MOD

        return hashes

    def get_hash(self, start: int, end: int) -> int:
        return (self.__prev_hashes[end] - self.__prev_hashes[start] * self.__parameter ** (end - start)) % self.MOD


@tested_time_memory
def longest_common_substring(string1: str, string2: str):
    hashed_string1 = HashedString(string1)
    hashed_string2 = HashedString(string2)

    left = 0
    right = min(len(string1), len(string2)) + 1

    past: Tuple[int, int] = (0, 0)

    while left < right:
        mid = (left + right) // 2

        hashes_set = {hashed_string1.get_hash(st, st + mid) for st in range(len(string1) - mid + 1)}

        coincidences = False
        for start in range(len(string2) - mid + 1):
            cur_hash2 = hashed_string2.get_hash(start, start + mid)
            if cur_hash2 in hashes_set:
                past = (start, mid)
                coincidences = True
                break

        if coincidences:
            left = mid + 1
        else:
            right = mid

    return past


if __name__ == '__main__':
    s, t = input("Введите первую строку: "), input("Введите вторую строку: ")

    start, length = longest_common_substring(t, s)
    print(f"Начало в {start} индексе первой строки, длина {length}")
