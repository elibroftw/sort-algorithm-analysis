from sorts import *
from time import time
import random

# func_list = [selection_sort, bubble_sort, comb_sort, counting_sort, heap_sort, insertion_sort, merge_sort, quick_sort,
#              shell_sort]
func_list = [comb_sort, counting_sort, heap_sort, merge_sort, quick_sort, shell_sort]


def test_sorts(length):
    random_arrays = []
    trials = {}
    for func in func_list:
        trials[func.__name__] = []
    for i in range(5):
        random_array = [random.randrange(100000) for _ in range(length)]  # positive integers only!!!
        random_arrays.append(random_array)
        # master_sorted_array = sorted(random_array)  # was used to check if sort was implemented properly
        for func in func_list:
            for j in range(5):
                test_array = random_array.copy()
                before = time()
                func(test_array)
                after = time()
                trials[func.__name__].append(after - before)
            print('done', func.__name__)
        print('done a round')
    with open(f'array list of length {length}.txt', 'w') as f:
        for l in random_arrays:
            for i, number in enumerate(l):
                if i > 0: f.write(', ')
                f.write(f'{number}')
            f.write('\n')

    for key in trials:
        with open(f'{key} - {length}.txt', 'w') as f:
            for i, value in enumerate(trials[key]):
                if i > 0: f.write(', ')
                f.write(str(value))
                if (i + 1) % 5 == 0: f.write('\n')


def start_test():
    # before = time()
    # test_sorts(100)
    # print('test 1:', time() - before)
    #
    # before = time()
    # test_sorts(1000)
    # print('test 2:', time() - before)
    #
    # before = time()
    # test_sorts(10000)
    # print('test 3:', time() - before)

    before = time()
    test_sorts(100000)
    print('test 4:', time() - before)

    before = time()
    test_sorts(1000000)
    print('test 5:', time() - before)


def calculate_averages():
    lengths = [100, 1000, 10000, 100000, 1000000]
    hs = {}
    for func in func_list:
        averages = []
        for length in lengths:
            with open(f'{func.__name__} - {length}.txt') as f:
                values = [float(value.replace('\n', '')) for value in f.read().split(', ')]
                averages.append(sum(values) / len(values))
                hs[func.__name__] = sum(values) / len(values)
        with open(f'{func.__name__} averages.txt', 'w') as f:
            length = 100
            for average in averages:
                f.write(str(length) + ': ' + str(average) + ' seconds \n')
                length *= 10
    # ranking_score = []
    # ranking_name = []
    # for key in hs:
    #     temp = hs[key]
    #     i = 0
    #     if len(ranking_score) == 0:
    #         ranking_score.append(temp)
    #         ranking_name.append(key)
    #     for x in ranking_score:
    #         if temp < x: break
    #         i += 1
    #     ranking_score.insert(i, temp)
    #     ranking_name.insert(i, key)
    # print(ranking_name)
    # print(ranking_score)


start_test()
calculate_averages()
