def sum_modulo():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    total = 0
    for num in arr:
        total = (total + num) % m

    print(total)


if __name__ == "__main__":
    sum_modulo()
