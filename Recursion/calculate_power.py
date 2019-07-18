import sys


def cal_power(base, power):
    if power == 0 :
        return 1
    temp = cal_power(base, int(power / 2))
    if power % 2 == 0:
        return temp * temp
    else:
        if power > 0:
            return base * temp * temp
        else:
            return (temp*temp)/base


if __name__ == "__main__":
    print(cal_power(2, -102))
