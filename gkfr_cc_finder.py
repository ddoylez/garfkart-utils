SPEEDS = {50: {'name': '50cc', 'torque': 40, 'speed': 72, 'reverse': 25},
          100: {'name': '100cc', 'torque': 46, 'speed': 87, 'reverse': 30},
          150: {'name': '150cc', 'torque': 54, 'speed': 102, 'reverse': 36}}


def custom_torque(cc):
    cc_50 = cc - 50
    cc_100 = cc - 100
    if cc <= 150:
        cc_t = SPEEDS[cc]['torque']
    else:
        cc_50_t = custom_torque(cc_50)
        cc_100_t = custom_torque(cc_100)
        cc_t = cc_50_t + (cc_50_t - cc_100_t + 2)
    torque = cc_t
    return torque


def custom_speed(cc):
    cc_50 = cc - 50
    if cc <= 150:
        cc_s = SPEEDS[cc]['speed']
    else:
        cc_50_s = custom_speed(cc_50)
        cc_s = cc_50_s + 15
    speed = cc_s
    return speed


def custom_reverse(cc):
    cc_50 = cc - 50
    cc_100 = cc - 100
    if cc <= 150:
        cc_r = SPEEDS[cc]['reverse']
    else:
        cc_50_r = custom_reverse(cc_50)
        cc_100_r = custom_reverse(cc_100)
        cc_r = cc_50_r + (cc_50_r - cc_100_r + 1)
    reverse = cc_r
    return reverse


def find_custom_stats(cc):
    new_torque = custom_torque(cc)
    new_speed = custom_speed(cc)
    new_reverse = custom_reverse(cc)
    return {int(cc): {'name': f'{cc}cc', 'torque': new_torque, 'speed': new_speed, 'reverse': new_reverse}}


def custom_round(x, base=50):
    return base * round(x / base)


def main():
    target_cc = input('Find stats for what CC? ')
    cc = custom_round(int(target_cc))
    stats = find_custom_stats(cc)
    out = f'{stats[cc]["name"]}\nTorque: {stats[cc]["torque"]}\nSpeed: {stats[cc]["speed"]}\nReverse: {stats[cc]["reverse"]}'
    print(out)


if __name__ == '__main__':
    main()
