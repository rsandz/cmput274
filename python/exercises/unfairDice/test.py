import unfairDice

args = [
    [[1/12, 1/4, 1/3, 1/12, 1/12, 1/6], 2**32-1, 20],
    [[1/4, 1/6, 1/12, 1/12, 1/4, 1/6], 42, 200],
    [[1/3, 1/3, 1/3], 2**32-1, 1000],
]

widths = [50, 10, 10, 1]


for index, arg in enumerate(args):
    # print("Index = {}".format(index))
    rolls = unfairDice.biased_rolls(*arg)
    unfairDice.draw_histogram(len(arg[0]), rolls, widths[index])

