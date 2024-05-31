#1
def concatenate(*args, **kwargs):
    result = ""
    for el in args:
        result += el
    for key in kwargs.keys():
        if key in result:
            result = result.replace(key, kwargs[key])
    return result


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))

#2
def concatenate(*args, **kwargs):
    text = ''.join(args)

    for key, value in kwargs:
        text = text.replace(key, value)

    return text

