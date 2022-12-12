from collections import Counter, deque
from copy import deepcopy
from functools import reduce
from operator import add, mul, sub, truediv, floordiv
from cProfile import run

from modnum import ModNum


cur_monkey = []
cur_test = []
monkeys_start = []
test_divs = []

op_strs = {
    "+": add,
    "-": sub,
    "/": truediv,
    "*": mul,
}

with open("11.txt") as f:
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
                    op = pow
                    val = 2
                cur_monkey.append((op,val))
            case 3:
                line = line.replace("Test: divisible by ", "")
                test_div = int(line)
                test_divs.append(test_div)
                cur_test.append(test_div)
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

for i, monkey in enumerate(monkeys_start):
    monkey[0] = deque(ModNum(item,test_divs) for item in monkey[0])

def get_activity(rounds,relief):
    monkeys = deepcopy(monkeys_start)
    activity = Counter()
    for round in range(rounds):
        for monkey_i, (items, (op, val), (test_div, true_monkey, false_monkey)) in enumerate(monkeys):
            for item in items:
                activity[monkey_i] += 1
                item = item.do_op(op,val)
                if relief:
                    item = item.do_op(floordiv, 3)
                if item % test_div == 0:
                    target_monkey = true_monkey
                else:
                    target_monkey = false_monkey
                monkeys[target_monkey][0].append(item)
            items.clear()
    
    return reduce(mul, (times for monkey, times in activity.most_common(2)))

print(get_activity(20,True))
print(get_activity(10000, False))