import random

TRACKS = {
    1: {'environment': 2, 'cup': 1, 'thing': 'Catz in the', 'location': 'Hood'},
    2: {'environment': 4, 'cup': 1, 'thing': 'Crazy', 'location': 'Dunes'},
    3: {'environment': 3, 'cup': 1, 'thing': 'Palerock', 'location': 'Lake'},
    4: {'environment': 1, 'cup': 1, 'thing': 'City', 'location': 'Slickers'},
    5: {'environment': 3, 'cup': 2, 'thing': 'Country', 'location': 'Bumpkin'},
    6: {'environment': 2, 'cup': 2, 'thing': 'Spooky', 'location': 'Manor'},
    7: {'environment': 1, 'cup': 2, 'thing': 'Mally', 'location': 'Market'},
    8: {'environment': 4, 'cup': 2, 'thing': 'Valley of the', 'location': 'Kings'},
    9: {'environment': 1, 'cup': 3, 'thing': 'Play Misty For', 'location': 'Me'},
    10: {'environment': 3, 'cup': 3, 'thing': 'Sneak-A', 'location': 'Peak'},
    11: {'environment': 4, 'cup': 3, 'thing': 'Blazing', 'location': 'Oasis'},
    12: {'environment': 2, 'cup': 3, 'thing': 'Pastacosi', 'location': 'Factory'},
    13: {'environment': 4, 'cup': 4, 'thing': 'Mysterious', 'location': 'Temple'},
    14: {'environment': 1, 'cup': 4, 'thing': 'Prohibited', 'location': 'Site'},
    15: {'environment': 2, 'cup': 4, 'thing': 'Caskou', 'location': 'Park'},
    16: {'environment': 3, 'cup': 4, 'thing': 'Loopy', 'location': 'Lagoon'}
}


def list_all_tracks():
    for i in TRACKS:
        for j in TRACKS:
            code = f'E{TRACKS[i]["environment"]}C{TRACKS[j]["cup"]}: '
            joiner = ' '
            if '-' in TRACKS[i]['thing']:
                joiner = '-'
            track = joiner.join([TRACKS[i]['thing'], TRACKS[j]['location']])
            print(f'{code}{track}')


def build_trackname(seed=None):
    random.seed(seed)
    i1 = random.choice(list(TRACKS))
    i2 = random.choice(list(TRACKS))
    code = f'E{TRACKS[i1]["environment"]}C{TRACKS[i2]["cup"]}: '
    joiner = ' '
    if '-' in TRACKS[i1]['thing']:
        joiner = '-'
    track = joiner.join([TRACKS[i1]['thing'], TRACKS[i2]['location']])
    return f'{code}{track}'


def main():
    list_all_tracks()
    # trackname = build_trackname()
    # print(trackname)


if __name__ == "__main__":
    main()
