import operator
import random


# Define possible math operations
operators = ['+', '-', '*']

# Map operation string to operator interface
ops = {'+': operator.add, '-': operator.sub, '*': operator.mul}


# Takes three numbers and operations b/n them. Returns result from the operations
# Does not consider higher math precedence. There is no multiplication b/n num2 and num3 (see above)
def calc_result(num1, num2, num3, operation1, operation2):
    result_a_b = ops[operation1](num1, num2)
    result_a_b_c = ops[operation2](result_a_b, num3)

    return result_a_b_c


# Tries to convert to int. If it fail returns -1
def convert_int(s):
    try:
        result = int(s)
    except ValueError:
        result = -1
    return result


# The list indexes are used as follows
#  A        [0]     B       [1]     C

# [6]               [8]             [10]

#  D        [2]     E       [3]     F

# [7]               [9]             [11]

#  G        [4]     H       [5]     I
def generate_operators():
    my_operators = []
    for x in range(12):
        my_operation = random.choice(operators)
        my_operators.append(my_operation)

    # Avoid double multiplication. Second '*' sign is replaced with '+' or '-' on random
    for i in range(0, 12, 2):
        if my_operators[i] == '*' and my_operators[i + 1] == '*':
            my_operators[i + 1] = random.choice(['+', '-'])

    return my_operators
