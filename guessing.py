import random


def generate_random_data(n=4):
    """
    1-9 中 随机生成n个不重复数字
    :param n: 数字的个数
    """
    data_set = list(range(10))
    return random.sample(data_set, n)


def check_your_guessing(target, guessing):
    """

    :param target: list, 目标数字列表
    :param guessing: list, 猜测的数字列表  
    :return: 显示猜测结果，B 代表数字和位置都正确的个数 ，A代表数字正确的个数
    """
    target_length = len(target)
    guessing_length = len(guessing)
    if target_length != guessing_length:
        return target_length * "0"
    guess_set = set(guessing)
    target_set = set(target)

    data_correct_num = len(guess_set) + len(target_set) - len(set.union(guess_set, target_set))
    order_correct_num = [guessing[i] == target[i] for i in range(len(guess_set))].count(True)

    return "{}A{}B".format(data_correct_num, order_correct_num)


def guessing_game(n=4):
    target = generate_random_data(n)
    success_res = "{0}A{0}B".format(n)
    i = 1
    while True:
        guessing = input("\033[;36mplease input your answer!\n\033[0m")
        checking = check_your_guessing(target, [int(i) for i in guessing])
        print(checking)
        if checking == success_res:
            print("Congratulation!")
            break
        elif i >= 9:
            print("\033[;36m The answer :{} \n\033[0m".format(target))
            break
        else:
            i += 1


if __name__ == '__main__':
    guessing_game(2)
