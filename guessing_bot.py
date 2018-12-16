from guessing import generate_random_data ,check_your_guessing
import itertools



def auto(N):

    TARGET = generate_random_data(N)

    possibility_collection = list(itertools.permutations(range(1, 10), N))

    t =0
    guess_data = list(range(1, N + 1))

    while True:

        check_res = check_your_guessing(TARGET,guess_data)
        print(t, guess_data, check_res ,len(possibility_collection))
        if check_res == "Y"*N:
            print("CONGRATULATION!")
            break
        guess_collection = list(filter(lambda x : check_your_guessing(guess_data, x) == check_res, possibility_collection))
        guess_data = guess_collection.pop()
        print("---------------",guess_data)
        possibility_collection =guess_collection
        t += 1
        if t >10:
            break




if __name__ == '__main__':
    auto(6)