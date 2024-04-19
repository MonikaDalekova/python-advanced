# 1
my_stack = []
n = int(input())

for _ in range(n):
    my_query = input().split()
    action = my_query[0]
    if action == "1":
        my_stack.append(int(my_query[1]))
    elif my_stack:
        if action == "2":
            my_stack.pop()
        elif action == "3":
            max_number = max(my_stack)
            print(f"{max_number}")
        elif action == "4":
            min_number = min(my_stack)
            print(f"{min_number}")
print_list = []
while my_stack:
    print_list.append(my_stack.pop())
print(f"{', '.join(str(x) for x in print_list)}")

#2
# my_stack = []
#
#
# def sum(a, b):
#     return a + b
#
#
# map_functions = {
#     "1": lambda x: my_stack.append(x[1]),
#     "2": lambda x: my_stack.pop() if my_stack else None,
#     "3": lambda x: print(max(my_stack)) if my_stack else None,
#     "4": lambda x: print(min(my_stack)) if my_stack else None
# }
#
# for _ in range(int(input())):
#     my_query = input().split()
#     action = my_query[0]
#     map_functions[action](my_query) #извикваме функцията, чието име е map_functions с ключ 1, 2 и т.н., като за X подаваме my_query
# my_stack.reverse()
# print(*my_stack, sep=", ")