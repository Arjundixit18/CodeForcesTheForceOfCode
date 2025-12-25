def is_right(points):

    x1, y1, x2, y2, x3, y3 = points
    a = (x1 - x2)**2 + (y1 - y2)**2
    b = (x2 - x3)**2 + (y2 - y3)**2
    c = (x1 - x3)**2 + (y1 - y3)**2

    sides = sorted([a, b, c])
    return sides[0] > 0 and sides[0] + sides[1] == sides[2]


points = list(map(int, input().split()))


if is_right(points):
    print("RIGHT")
else:
    found = False

    for i in range(6):
        points[i] += 1
        if is_right(points):
            print("ALMOST")
            found = True
            break

        points[i] -= 2
        if is_right(points):
            print("ALMOST")
            found = True
            break

        points[i] += 1  

    if not found:
        print("NEITHER")
