SPEEDS = {0: {'name': '0cc', 'torque': 36, 'speed': 57, 'reverse': 21},
          50: {'name': '50cc', 'torque': 40, 'speed': 72, 'reverse': 25},
          100: {'name': '100cc', 'torque': 46, 'speed': 87, 'reverse': 30},
          150: {'name': '150cc', 'torque': 54, 'speed': 102, 'reverse': 36}}


def equation_torque(cc):
    torque = (0.0004 * cc * cc) + (0.06 * cc) + 36
    return torque


def recursive_torque(cc):
    cc_50 = cc - 50
    cc_100 = cc - 100
    if cc <= 150:
        cc_t = SPEEDS[cc]['torque']
    else:
        cc_50_t = recursive_torque(cc_50)
        cc_100_t = recursive_torque(cc_100)
        cc_t = cc_50_t + (cc_50_t - cc_100_t + 2)
    torque = cc_t
    return torque


def equation_speed(cc):
    speed = (0.3 * cc) + 57
    return speed


def recursive_speed(cc):
    cc_50 = cc - 50
    if cc <= 150:
        cc_s = SPEEDS[cc]['speed']
    else:
        cc_50_s = recursive_speed(cc_50)
        cc_s = cc_50_s + 15
    speed = cc_s
    return speed


def equation_reverse(cc):
    reverse = (0.0002 * cc * cc) + (0.07 * cc) + 21
    return reverse


def recursive_reverse(cc):
    cc_50 = cc - 50
    cc_100 = cc - 100
    if cc <= 150:
        cc_r = SPEEDS[cc]['reverse']
    else:
        cc_50_r = recursive_reverse(cc_50)
        cc_100_r = recursive_reverse(cc_100)
        cc_r = cc_50_r + (cc_50_r - cc_100_r + 1)
    reverse = cc_r
    return reverse


def equation_relative_speed(base_speed, new_speed):
    return base_speed / SPEEDS[150]['speed'] * new_speed


def find_custom_stats_equation(cc):
    new_torque = equation_torque(cc)
    new_speed = equation_speed(cc)
    new_reverse = equation_reverse(cc)
    new_air_speed = equation_relative_speed(70, new_speed)
    new_surface2_speed = equation_relative_speed(44, new_speed)
    new_surface3_speed = equation_relative_speed(30, new_speed)
    return {int(cc): {'name': f'{cc}cc', 'torque': new_torque, 'speed': new_speed, 'reverse': new_reverse,
                      'air_speed': new_air_speed, 'surface2': new_surface2_speed, 'surface3': new_surface3_speed}}


def find_custom_stats_recursive(cc):
    new_torque = recursive_torque(cc)
    new_speed = recursive_speed(cc)
    new_reverse = recursive_reverse(cc)
    return {int(cc): {'name': f'{cc}cc', 'torque': new_torque, 'speed': new_speed, 'reverse': new_reverse}}


def custom_round(x, base=50):
    return base * round(x / base)


def main():
    target_cc = input('Find stats for what CC? ')
    cc = int(target_cc)
    stats = find_custom_stats_equation(cc)
    out = f'{stats[cc]["name"]}\nTorque: {stats[cc]["torque"]}\nSpeed: {stats[cc]["speed"]}\nReverse: {stats[cc]["reverse"]}\nAir Speed: {stats[cc]["air_speed"]}\nSurface 2: {stats[cc]["surface2"]}\nSurface 3: {stats[cc]["surface3"]}'
    print(out)

    # cc_round = custom_round(cc)
    # stats = find_custom_stats_recursive(cc_round)
    # out = f'Recursive {stats[cc_round]["name"]}\nTorque: {stats[cc_round]["torque"]}\nSpeed: {stats[cc_round]["speed"]}\nReverse: {stats[cc_round]["reverse"]}'
    # print('')
    # print(out)


if __name__ == '__main__':
    main()
