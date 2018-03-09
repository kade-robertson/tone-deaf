# Generic functions that might be used in multiple chords.

def tetrate(x, y):
    out = x
    while y > 1:
        out = x ** out
        y -= 1
    return out

def is_prime(x):
    if x % 2 == 0 or x < 2:
        return 0
    elif x == 2:
        return 1
    else:
        i = 3
        while i < int(x**.5)+1:
            if x % i == 0:
                return 0
            i += 2
        return 1

def prime_factors(x):
    f = []
    while x % 2 == 0:
        f += [2]
        x /= 2
    i = 3
    while x > 1:
        while x % i == 0:
            f += [i]
            x /= i
        i += 2
    return f

def tetr_mod(x, y, m):
    a = 1
    i = 0
    while i < y:
        b = pow(x, a, m)
        if a == b: break
        a = b
        i += 1
    return b

def lu_decomp_det(m):
    d = 1
    s = len(m)
    for i in range(s):
        d *= m[i,i]
        c = i+1
        for j in range(c, s):
            m[j,i] /= m[i,i]
            for k in range(c, s):
                m[j,k] -= m[j,i] * m[i,k]
    return d
