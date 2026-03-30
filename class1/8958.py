T = int(input())

for _ in range(T):
    s = input()
    score = streak = 0
    for ch in s:
        streak = streak + 1 if ch == 'O' else 0
        score += streak
    print(score)

