while True: 
    A, B, C = map(int, input().split())

    if A == 0 and B == 0 and C == 0:
        break

    sides = sorted([A, B, C])
    
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        print("right")
    else:
        print("wrong")