from collections import Counter, deque
from copy import deepcopy
from functools import reduce
from operator import add, mul, sub, truediv
from cProfile import run


cur_monkey = []
cur_test = []
monkeys_start = []

op_strs = {
    "+": add,
    "-": sub,
    "/": truediv,
    "*": mul,
}

with open("11-test.txt") as f:
    for monkey_i, line in enumerate(f):
        line = line.strip()
        match monkey_i%7:
            case 1:
                line = line.replace("Starting items: ", "")
                items = deque(int(x) for x in line.split(", "))
                cur_monkey.append(items)
            case 2:
                line = line.replace("Operation: new = old ", "")
                op, val = line.split(" ")
                op = op_strs[op]
                try:
                    val = int(val)
                except ValueError:
                    op = mul
                    val = None
                cur_monkey.append((op,val))
            case 3:
                line = line.replace("Test: divisible by ", "")
                cur_test.append(int(line))
            case 4:
                line = line.replace("If true: throw to monkey ", "")
                cur_test.append(int(line))
            case 5:
                line = line.replace("If false: throw to monkey ", "")
                cur_test.append(int(line))
                cur_monkey.append(cur_test)
                cur_test = []
                monkeys_start.append(cur_monkey)
                cur_monkey = []


def get_activity(rounds,relief):
    monkeys = deepcopy(monkeys_start)
    activity = Counter()
    for round in range(rounds):
        if round % 100 == 0:
            print(round)
        for monkey_i, (items, (op, val), (test_div, true_monkey, false_monkey)) in enumerate(monkeys):
            for item in items:
                activity[monkey_i] += 1
                if val is None:
                    val = item
                item = op(item,val)
                if relief:
                    item //= 3
                if item % test_div == 0:
                    target_monkey = true_monkey
                else:
                    target_monkey = false_monkey
                monkeys[target_monkey][0].append(item)
            items.clear()
    
    return reduce(mul, (times for monkey, times in activity.most_common(2)))

print(get_activity(20,True))
run('get_activity(800,False)')