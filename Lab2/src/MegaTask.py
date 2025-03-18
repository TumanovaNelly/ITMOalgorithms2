from Lab2.src.Rope import Rope


def main():
    string = Rope()
    string.build(input("Введите текст: "))
    for _ in range(int(input("Введите количество запросов: "))):
        start_cut, end_cut, to_index = map(int, input().split())
        string.cut_n_paste((start_cut, end_cut), to_index)
    print(string)


if __name__ == '__main__':
    main()
