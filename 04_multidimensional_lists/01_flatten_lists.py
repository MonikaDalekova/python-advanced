#1
string = input().split("|")
result = []
for element in string[::-1]:
    for el in element.split():
        result.append(el)
print(*result, sep=' ')

#2
string = input().split("|")
result = []
for element in string[::-1]:
    result.extend(element.split())
print(*result, sep=' ')

#3
numbers = [el.split() for el in input().split("|")]
print(*[' '.join(sublist) for sublist in numbers[::-1] if sublist])