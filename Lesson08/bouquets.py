def bouquets(narcissus_price, tulip_price, rose_price, summ):
    result = set()

    for x in range(summ, -1, 0 - narcissus_price):
        print "x " + str(x)
        for y in range (summ - x*narcissus_price, -1, 0 - tulip_price):
            print "y " + str(y)
            for z in range(summ - x*narcissus_price - y*tulip_price, -1, 0 - rose_price):
                print "z " + str(z)

                if (x + y + z) % 2 != 0 and x*narcissus_price + y*tulip_price + z*rose_price <= summ:
                    print "X:%2d, Y:%2d, Z:%2d" % (x, y, z)
                    result.add((x, y, z))
    return len(result)
