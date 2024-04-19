stack_list = []
text = input()

for index in range(len(text)):
    if text[index] == "(":
        stack_list.append(index)
    elif text[index] == ")":
        start_position = stack_list.pop()
        end_position = index
        print(text[start_position:end_position+1])