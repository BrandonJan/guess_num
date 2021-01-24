import random

r = random.randint(1, 100)

while True:
    guess = input("請輸入猜的整數，範圍為0-100:")
    guess = int(guess)
    if guess == r:
	    print("終於猜對啦!")
	    break
    elif guess >= r:
	    print("猜錯啦!答案比你猜的數字再小一點")
    elif guess <= r:
        print("猜錯啦!答案比你猜的數字再大一點")
    pass
