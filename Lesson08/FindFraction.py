def find_fraction(summ):
    znam = summ//2 + 1
    chys = summ - znam
    if summ < 3:
        return False
    elif chys % 2 == 0 and znam % 2 == 0:
        znam = znam + 1
        chys = summ - znam

    return (chys, znam)
