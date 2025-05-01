from typing import List


def z_function(s: str) -> List[int]:
    n = len(s)
    z = [0] * n
    left, right = 0, 0

    for i in range(1, n):
        if i <= right:
            z[i] = min(right - i + 1, z[i - left])

        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1

        if i + z[i] - 1 > right:
            left, right = i, i + z[i] - 1

    return z


if __name__ == '__main__':
    z = z_function(input('Введите строку: '))
    print("Z-функция строки:")
    print(*z)