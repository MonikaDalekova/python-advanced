def cookbook(*args):
    book = {}
    for case in args:
        name, cuisine, ingredients = case
        if cuisine not in book.keys():
            book[cuisine] = []
        book[cuisine].append([name, ingredients])
    sorted_book = sorted(book.items(), key=lambda x: (-len(x[1]), x[0]))

    final_result = ''
    for cuisine, recepies in sorted_book:
        sorted_recepies = sorted(recepies, key=lambda x: x[0])
        final_result += f'{cuisine} cuisine contains {len(sorted_recepies)} recipes:\n'
        for name, ingredients in sorted_recepies:
            final_result += f"  * {name} -> Ingredients: {', '.join(ingredients)}\n"
    return final_result


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))