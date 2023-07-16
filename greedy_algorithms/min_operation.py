def min_operations(target):
    number_steps = 0
    while target != 0:
        if target % 2 == 0:
            target //= 2
        else:
            target -= 1
        number_steps += 1
    return number_steps


def test_function(test_case):
    target = test_case[0]
    solution = test_case[1]
    output = min_operations(target)

    if output == solution:
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    target = 18
    solution = 6
    test_case = [target, solution]
    test_function(test_case)

    target = 69
    solution = 9
    test_case = [target, solution]
    test_function(test_case)
