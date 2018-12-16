from guessing import generate_random_data, check_your_guessing
import itertools

t_all = 0


def auto(n):
    target = generate_random_data(n)  # 目标数字
    possibility_collection = list(itertools.permutations(range(10), n))  # 所有可能性列表
    t = 1
    guess_data = list(range(1, n + 1))  # 第一步都猜 123...n
    success_res = "{0}A{0}B".format(n)
    while True:
        check_res = check_your_guessing(target, guess_data)
        print(t, guess_data, check_res, len(possibility_collection))  # 单个题已猜的次数，显示结果 ，可能性集合的size
        if check_res == success_res:
            print("CONGRATULATION!")
            global t_all
            t_all += t
            break
        guess_collection = list(
            filter(lambda x: check_your_guessing(guess_data, x) == check_res, possibility_collection))
        guess_data = guess_collection.pop()
        possibility_collection = guess_collection
        t += 1


if __name__ == '__main__':
    for i in range(10):
        auto(8)
    print(t_all)
