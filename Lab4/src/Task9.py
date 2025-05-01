from Lab4.src.Task7 import HashedString
from utils import tested_time_memory


@tested_time_memory
def compress_string(string: str) -> str:
    hashed_string = HashedString(string)

    dp = [float('inf')] * (len(string) + 1)
    dp[0] = 0

    last_repeated_substring = [(0, 0)] * (len(string) + 1)
    repeat = [0] * (len(string) + 1)

    for end in range(1, len(string) + 1):
        for start in range(end):
            hash_repeated_string = hashed_string.get_hash(start, end)
            length_repeated_string = end - start

            multiplier = 1
            cur_start = start - length_repeated_string
            cur_end = start

            while cur_start >= 0 and hashed_string.get_hash(cur_start, cur_end) == hash_repeated_string:
                multiplier += 1
                cur_start -= length_repeated_string
                cur_end -= length_repeated_string

            cur_res = (dp[cur_end] + (1 if cur_end > 0 else 0) + length_repeated_string +
                       (len(str(multiplier)) + 1 if multiplier > 1 else 0))

            if dp[end] > cur_res:
                dp[end] = cur_res
                last_repeated_substring[end] = (start, end)
                repeat[end] = multiplier

    i = len(string)
    result = []
    while i > 0:
        result += [string[last_repeated_substring[i][0]: last_repeated_substring[i][1]] +
                   (f"*{repeat[i]}" if repeat[i] > 1 else "")]
        i -= (last_repeated_substring[i][1] - last_repeated_substring[i][0]) * repeat[i]

    return "+".join(reversed(result))


if __name__ == '__main__':
    print(compress_string(input("Введите строку: ")))
