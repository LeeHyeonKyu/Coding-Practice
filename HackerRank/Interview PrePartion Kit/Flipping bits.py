def flippingBits(n):
    bin_n = '{:0>32}'.format(bin(n)[2:])
    rev_n = '0b'
    for bit in bin_n :
        if bit == '1' :
            rev_n += '0'
        else :
            rev_n += '1'
    return int(rev_n, 2)
