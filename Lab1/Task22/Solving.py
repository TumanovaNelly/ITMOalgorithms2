from utils import tested_time_memory


def dp_check(line_num1: int, line_num2: int, lines_len: int) -> bool:
    num1_shift = line_num1 >> 1
    num2_shift = line_num2 >> 1
    combined0 = line_num1 | num1_shift | line_num2 | num2_shift
    # Если последние (lines_len - 1) битов числа combined0 равны 1, плохих квадратов из нулей нет
    combined1 = line_num1 & num1_shift & line_num2 & num2_shift
    # Если последние (lines_len - 1) битов числа combined1 равны 0, плохих квадратов из единиц нет
    mask = (1 << (lines_len - 1)) - 1  # нули и (lines_len - 1) единиц в конце
    return (combined0 & mask == mask) and (combined1 & mask == 0)


@tested_time_memory
def tiles_task(m: int, n: int) -> int:
    if n > m: n, m = m, n
    lst_line_variants_num = (1 << n) # то же, что 2^n
    dp = [[1] * lst_line_variants_num, [0] * lst_line_variants_num]
    for k in range(1, m):
        old_index = ~k & 1  # то же, что old_index = (k % 2 == 0)
        new_index = k & 1  # то же, что new_index = (k % 2 == 1)
        for line_num_i in range(lst_line_variants_num):
            for line_num_j in range(lst_line_variants_num):
                if dp_check(line_num_i, line_num_j, n):
                    dp[new_index][line_num_j] += dp[old_index][line_num_i]

        for i in range(lst_line_variants_num): dp[old_index][i] = 0

    return sum(dp[~m & 1])


if __name__ == '__main__':
    variants_num = tiles_task(*map(int, input("Введите размеры двора: ").split()))
    print(f"Всего {variants_num} вариантов")
