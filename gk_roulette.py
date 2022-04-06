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
    hat_options.extend([GARAGE[color]['hat'] for color in list(GARAGE)])
    final_hat_options = [hat for hat in [hat_options[0]] for i in range(20)]
    final_hat_options.extend([hat for hat in [hat_options[1]] for i in range(20)])
    final_hat_options.extend([hat for hat in hat_options[2:] for i in range(10)])
    hat = random.choice(final_hat_options)

    spoiler_options = [GARAGE[color]['spoiler'] for color in list(GARAGE)]
    final_spoiler_options = [spoiler for spoiler in [spoiler_options[0]] for i in range(20)]
    final_spoiler_options.extend([spoiler for spoiler in spoiler_options[1:] for i in range(10)])
    spoiler = random.choice(final_spoiler_options)

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
        with open('C:/Users/Dan/Documents/obs dump/misc/gkr.txt', 'w', encoding='utf-8') as o:
            o.write(out)
            o.close()
        print(out)
        inp = input('Reroll? Yes/No\n')
        if 'y' not in inp.lower():
            return


if __name__ == "__main__":
    main()
