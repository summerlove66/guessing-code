import random


def generate_random_data(n=4):
    """
  
    :param n: the  length of  the genearated data
    """
    data_set = list(range(1, 10))
    return random.sample(data_set, n)


def check_your_guessing(target, guessing):
    """
    
    :param target: list, target data 
    :param guessing: list, the data of player  guessing  
    :return: give some hint to player ,, how may many Numers are correct and how many Number  in correct order .
    """
    target_length = len(target)
    guessing_length = len(guessing)
    if target_length != guessing_length:
        return target_length * "0"
    guess_set = set(guessing)
    target_set = set(target)

    data_correct_num = len(guess_set) + len(target_set) - len(set.union(guess_set, target_set))
    order_correct_num = [guessing[i] == target[i] for i in range(len(guess_set))].count(True)
    return order_correct_num * "Y" + (data_correct_num - order_correct_num) * "X" + (
                                                                                target_length - data_correct_num) * "0"


def guessing_game(n=4):
    target = generate_random_data(n)

    i =1
    while True:
        guessing = input("\033[;36mplease input your answer!\n\033[0m")
        checking = check_your_guessing(target, [int(i) for i in guessing])
        print(checking)
        if checking == "Y" * len(target):
            print("Congratulation!")
            break
        elif i >= 9:
            print("\033[;36m The answer :{} \n\033[0m".format(target))
            break
        else:
            i += 1
if __name__ == '__main__':
    guessing_game(4)
