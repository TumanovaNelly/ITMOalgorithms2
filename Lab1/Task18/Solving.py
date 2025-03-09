from typing import List, Tuple

from utils import tested_time_memory


@tested_time_memory
def cafe_task(day_prices: List[int], coupon_price: int = 100) -> Tuple[int, Tuple[int, int], List[int]]:
    # Построение динамической таблицы
    dp: List[List] = [[0]]
    for price in day_prices:
        dp.append([float("inf")] * len(dp[-1]))
        will_coupon_add = False
        if price > coupon_price:
            dp[-1].append(float("inf"))
            will_coupon_add = True

        dp[-1][will_coupon_add] = dp[-2][0] + price
        for i in range(1, len(dp[-2])):
            dp[-1][i - 1] = min(dp[-1][i - 1], dp[-2][i])
            dp[-1][i + will_coupon_add] = min(dp[-1][i + will_coupon_add], dp[-2][i] + price)

    # print(*dp, sep="\n")

    # Поиск лучшего пути
    min_cost = dp[-1][0]
    min_cost_col = 0
    for i in range(1, len(dp[-1])):
        if min_cost >= dp[-1][i]:
            min_cost = dp[-1][i]
            min_cost_col = i

    # Восстановление пути
    way_point_cur_index = min_cost_col
    free_days = []
    for line in range(len(dp) - 1, 0, -1):
        was_coupon_add = day_prices[line - 1] > coupon_price
        if way_point_cur_index + 1 < len(dp[line - 1]) and \
                dp[line - 1][way_point_cur_index + 1] == dp[line][way_point_cur_index]:
            free_days.append(line)
            way_point_cur_index += 1
        else:
            way_point_cur_index -= was_coupon_add

    return min_cost, (min_cost_col, len(free_days)), free_days


if __name__ == '__main__':
    data = list(map(int, input("Введите стоимость обедов: ").split()))
    cost_data, (extra_coupons, spent_coupons), days_data = cafe_task(data)
    print(f"Минимальная сумма на обеды: {cost_data}")
    print(f"Останется {extra_coupons} купонов. Всего будет потрачено {spent_coupons} купонов")
    print("Дни, когда нужно использовать купоны:")
    print(*reversed(days_data), sep="\n")
