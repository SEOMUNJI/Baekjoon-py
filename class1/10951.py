while True:
    try:
        A, B = map(int, input().split())
        print(A + B)
    except:
        break

# 방법 2
#import sys

#for line in sys.stdin:
#    A, B = map(int, line.split())
#    print(A + B)