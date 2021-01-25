import random

r = random.randint(1, 100)
count = 0
while True:
    count += 1 #count = count + 1
    guess = input("請輸入猜的整數，範圍為0-100:")
    guess = int(guess)
    if guess == r:
	    print("終於猜對啦!")
	    print("這是你猜的第", count, "次")
	    break
    elif guess >= r:
	    print("猜錯啦!答案比你猜的數字再小一點")
    elif guess <= r:
        print("猜錯啦!答案比你猜的數字再大一點")
    print("這是你猜的第", count, "次")
    pass
