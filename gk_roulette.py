import random

GARAGE = {
    'White': {'character': 'N/A', 'kart': 'N/A', 'hat': 'No Hat', 'unique_hat': 'No Hat', 'spoiler': 'No Spoiler'},
    'Orange': {'character': 'Garfield', 'kart': 'Formula ZZZZ', 'hat': 'Beddy-Bye Cap',
               'unique_hat': 'Space-Bubble', 'spoiler': 'Bombastic Spoiler'},
    'Yellow': {'character': 'Jon', 'kart': 'Abstract-Kart', 'hat': 'Whizzy Wizard', 'unique_hat': 'Pizzaiolo Hat',
               'spoiler': 'Whacky Spoiler'},
    'Cyan': {'character': 'Liz', 'kart': 'Medi-Kart', 'hat': 'Tic-Toque', 'unique_hat': 'Bunny Band',
             'spoiler': 'Superfit Spoiler'},
    'Red': {'character': 'Odie', 'kart': 'Woof-Mobile', 'hat': 'Elasto-Hat', 'unique_hat': 'Joe Montagna',
            'spoiler': 'Cyclobone Spoiler'},
    'Pink': {'character': 'Arlene', 'kart': 'Kissy-Kart', 'hat': 'Chef\'s Special',
             'unique_hat': 'Aristo-Catic Bicorn', 'spoiler': 'Foxy Spoiler'},
    'Gray': {'character': 'Nermal', 'kart': 'Cuite-Pie Cat', 'hat': 'Cutie-Pie Crown',
             'unique_hat': 'Toutankhameow', 'spoiler': 'Shimmering Spoiler'},
    'Purple': {'character': 'Squeak', 'kart': 'Rat-Racer', 'hat': 'Viking Helmet',
               'unique_hat': 'Apprentice Sorcerer', 'spoiler': 'Holey Moley Spoiler'},
    'Green': {'character': 'Harry', 'kart': 'Muck-Madness', 'hat': 'Stink-O-Rama', 'unique_hat': 'Mule Head',
              'spoiler': 'Stained Spoiler'}}


def build_loadout(seed=None):
    random.seed(seed)
    char_color = random.choice(list(GARAGE)[1:])
    char = GARAGE[char_color]['character']
    kart = GARAGE[random.choice(list(GARAGE)[1:])]['kart']
    hat_options = [GARAGE[char_color]['unique_hat']]
    for color in list(GARAGE):
        hat_options.append(GARAGE[color]['hat'])
    hat = random.choice(hat_options)
    spoiler = GARAGE[random.choice(list(GARAGE))]['spoiler']
    loadout = {'character': char, 'kart': kart, 'hat': hat, 'spoiler': spoiler}
    return loadout


def main():
    while True:
        loadout = build_loadout()
        char = loadout['character']
        kart = loadout['kart']
        hat = loadout['hat']
        spoiler = loadout['spoiler']
        out = f'C: {char}\nK: {kart}\nH: {hat}\nS: {spoiler}'
        with open('text/gkr.txt', 'w', encoding='utf-8') as o:
            o.write(out)
            o.close()
        print(out)
        inp = input('Reroll? Yes/No\n')
        if 'y' not in inp.lower():
            return


if __name__ == "__main__":
    main()
