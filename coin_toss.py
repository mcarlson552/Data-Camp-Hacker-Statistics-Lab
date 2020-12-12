import numpy as np

coin = np.random.randint(0,2) # randomly generate 0 or 1
counter = 0

coin_toss = []

for toss in range(0,6):
    if counter < 5:
        counter += 1
        if coin == 0:
            coin_toss.append("heads")
        else:
            coin_toss.append("tails")
    else:
        print("You have tossed all your coins")

print(coin_toss)
print(counter)

#range makes counter meaningless - need to fix counter