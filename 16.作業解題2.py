#作業2:
#寫一段程序，讀取用戶輸入的工資，根據工資多少，打印下面相應的文字
#你工資多少決定了你的心態

print("你的薪水有多少?")
salary = int(input())
if salary <= 20000:
    print("惡老闆去吃屎吧!!")
elif salary < 30000:
    print("只能吃飽飯而已")
elif salary < 50000:
    print("物價通膨養活自己而已")
elif salary < 80000:
    print("下班可以去喝喝酒")
elif salary < 100000:
    print("你終於給到基本薪資了")
else :
    print("天天都去大保健")
print("完成！亂按離開")
input()
