import random

number=random.randint(1,100)
guess=0
guess_count = 0

print("猜一个1-100之间的数字")
while guess !=number:
           
    guess =int(input("你的猜测"))
    guess_count += 1
    if guess < number :
        print("太小了")
    elif guess>number: 
        print("太大了")
    else:
        print(f"恭喜，答对了！你总共猜了{guess_count}次")