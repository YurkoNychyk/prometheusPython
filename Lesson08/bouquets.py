def bouquets(narcissus_price, tulip_price, rose_price, summ):

    narcissus_price *= 100
    tulip_price *= 100
    rose_price *= 100
    summ *= 100

    n_price = int(narcissus_price)
    t_price = int(tulip_price)
    r_price = int(rose_price)
    summ = int(summ)

    result = 0
    n = 0
    for x in range(0, summ+1, n_price):
        for y in range(0, summ+1, t_price):
            for z in range(0, summ+1, r_price):
                if x + y + z > summ:
                    break
                else:
                    n += 1
                    if (x / n_price + y / t_price + z / r_price) % 2 != 0 and x + y + z <= summ:
                        result += 1
    return result
