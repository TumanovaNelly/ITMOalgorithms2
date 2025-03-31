from Lab3.src.QuickMax import quick_max
from Prima import get_mst_lens
from utils import tested_time_memory


@tested_time_memory
def task(data, cluster_number):
    return quick_max(get_mst_lens(data), cluster_number - 2) ** 0.5


if __name__ == '__main__':
    n = int(input("Введите количество вершин: "))
    print("Введите координаты вершин:")
    vertexes = [tuple(map(int, input().split()[:2])) for _ in range(n)]
    print(task(vertexes, int(input("Введите количество кластеров: "))))
