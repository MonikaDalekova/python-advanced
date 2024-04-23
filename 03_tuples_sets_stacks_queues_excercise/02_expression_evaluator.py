from collections import deque
from math import floor
expression = deque(input().split())
index = 0

while index < len(expression):
    element = expression[index]
    if element == "*":
        for _ in range(index-1):
            expression.appendleft(int(expression.popleft()) * int(expression.popleft()))
    elif element == "+":
        for _ in range(index-1):
            expression.appendleft(int(expression.popleft()) + int(expression.popleft()))
    elif element == "-":
        for _ in range(index-1):
            expression.appendleft(int(expression.popleft()) - int(expression.popleft()))
    elif element == "/":
        for _ in range(index-1):
            expression.appendleft(int(expression.popleft()) / int(expression.popleft()))

    if element in "*+-/":
        del expression[1]
        index = 1
    index += 1
print(floor(int(expression[0])))

#2
# from collections import deque
# from functools import reduce
# from math import floor
# 
# expression = deque(input().split())
# index = 0
# 
# functions = {
#     "*": lambda i: reduce(lambda a, b: a*b, map(int, expression[:i])),
#     "+": lambda i: reduce(lambda a, b: a+b, map(int, expression[:i])),
#     "-": lambda i: reduce(lambda a, b: a-b, map(int, expression[:i])),
#     "/": lambda i: reduce(lambda a, b: a/b, map(int, expression[:i]))
# }
# 
# while index < len(expression):
#     element = expression[index]
#     if element in "*+-/":
#         expression[0] = functions[element](index)
#         [expression.pop(1) for i in range(index)]
#         index = 1
#     index += 1
# print(floor(int(expression[0])))
