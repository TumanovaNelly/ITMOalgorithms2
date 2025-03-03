from utils import tested_time_memory


@tested_time_memory
def palindrome_task(word: str, k: int) -> int:
    cnt = 1

    for i in range(1, len(word)):
        badness_index = 0
        left = right = i
        while left >= 0 and right < len(word):
            if word[left] != word[right]: badness_index += 1
            if badness_index > k: break
            cnt += 1
            left -= 1
            right += 1

        badness_index = 0
        left = i - 1
        right = i
        while left >= 0 and right < len(word):
            if word[left] != word[right]: badness_index += 1
            if badness_index > k: break
            cnt += 1
            left -= 1
            right += 1

    return cnt


if __name__ == '__main__':
    word = input("Введите слово: ")
    k = int(input("K = "))
    print('Количество "почти палиндромов" = ', palindrome_task(word, k))
