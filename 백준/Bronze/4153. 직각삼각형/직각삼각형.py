while (1):
    x, y, z = map(int, input().split())
    if x == y == z == 0:
        break

    if (x*x + y*y == z*z) or (x*x + z*z == y*y) or (y*y + z*z == x*x):
        result = "right"
    else:
        result = "wrong"

    print(result)