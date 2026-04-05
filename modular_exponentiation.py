def mod_exp(a, m, p):
    result = 1
    a = a % p

    while m > 0:
        if m % 2 == 1:
            result = (result * a) % p
        a = (a * a) % p
        m //= 2

    return result


if __name__ == "__main__":
    a, m, p = map(int, input().split())
    print(mod_exp(a, m, p))
