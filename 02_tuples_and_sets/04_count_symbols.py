#1
def dictionary(text):
    some_dict = {}
    counter = 1
    for el in text:
        if el not in some_dict:
            some_dict[el] = counter
        else:
            some_dict[el] += 1
    return some_dict


def sorting(some_dict):
    sorted_list = list(some_dict.keys())
    sorted_list.sort()
    sorted_dict = {i: some_dict[i] for i in sorted_list}
    return sorted_dict


text = input()
some_dict = dictionary(text)
for el, count in sorting(some_dict).items():
    print(f"{el}: {count} time/s")

#2
# occ = {}
# for letter in input():
#     occ[letter] = occ.get(letter, 0) + 1
#
# for el, count in sorted(occ.items()):
#     print(f"{el}: {count} time/s")