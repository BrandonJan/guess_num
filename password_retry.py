password = input("請輸入密碼，最多輸入3次")
if password == "a123456" :
    print("登入成功!")
else:
    x = 2
    while x > 0 :
        print("密碼錯誤!還有", x, "次機會")
        password = input("請再次輸入密碼")
        if password == "a123456" :
        	print("登入成功!")
        	break
        x = x-1
    pass
if x == 0:
    print("帳號已上鎖")
    
        

