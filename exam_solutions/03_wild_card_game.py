def draw_cards(*args, **kwargs):
    monster_cards = []
    spell_cards = []
    result = ''

    for card_name, card_type in (list(args) + list(kwargs.items())): # мога да събера двата листа, защото прави низ от тюпъли
        if card_type == "monster":
            monster_cards.append(f"  ***{card_name}")
        elif card_type == "spell":
            spell_cards.append(f"  $$${card_name}")

    if monster_cards:
        result = "Monster cards:\n" + "\n".join(sorted(monster_cards, reverse=True))
    if spell_cards:
        result += "\nSpell cards:\n" + "\n".join(sorted(spell_cards))

    return result


print(draw_cards(("celtic guardian", "monster"), ("earthquake", "spell"), ("fireball", "spell"), raigeki="spell",
                     destroy="spell", ))

