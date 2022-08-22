def bouquets(narcissus_price, tulip_price, rose_price, summ):
    result = 0
    n = 0
    for x in range(0, summ+1, narcissus_price):
        for y in range(0, summ+1, tulip_price):
            for z in range(0, summ+1, rose_price):
                if x + y + z > summ:
                    break
                else:
                    n += 1
                    if (x/narcissus_price + y/tulip_price + z/rose_price) % 2 != 0 and x + y + z <= summ:
                        result += 1
    print n
    return result
