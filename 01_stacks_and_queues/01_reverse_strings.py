def stack_list(a):
    my_stack = list(a)
    while my_stack:
        removed_item = my_stack.pop()
        print(removed_item, end='')


string = input()
stack_list(string)