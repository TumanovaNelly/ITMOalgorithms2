from Lab2.src.Rope import Rope
from utils import tested_time_memory


@tested_time_memory
def task(word, requests) -> str:
    string = Rope()
    string.build(word)
    for *from_borders, to_border in requests:
        string.cut_n_paste(from_borders, to_border)
    return str(string)


if __name__ == '__main__':
    word = input("Введите текст: ")
    requests = []
    for _ in range(int(input("Введите количество запросов: "))):
        requests.append(tuple(map(int, input().split())))

    print(task(word, requests))
