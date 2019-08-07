
import random


cnt = 10000;
playerWin = 0
bankerWin = 0
while cnt:
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    sum = a + b
    if sum == 7 or sum == 11:
        playerWin += 1
    elif sum == 2 or sum == 3 or sum == 12:
        bankerWin += 1
    else:
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        sum2 = x + y
        if sum2 == sum:
            playerWin += 1
        if sum2 == 7:
            bankerWin += 1

    cnt -= 1

print("player win ", playerWin)
print("banker win ", bankerWin)

