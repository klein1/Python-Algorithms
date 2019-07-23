x = 2
epsilon = 0.0001
step = epsilon/10
numGuesses = 0
ans = 1

while abs(ans**2 - x) >= epsilon and ans <= x:
    ans += step
    numGuesses += 1

print('numGuesses =', numGuesses)
print('ans =', ans)