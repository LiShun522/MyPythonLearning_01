#作業1:
#猜年齡遊戲，寫程序實現以下效果，程序啟動後讓用戶猜腳色年齡。

while True:
    print("猜猜寶寶的年齡?")
    age = int(input())
    if age > 18:
        print("想被打?")
    if age < 18:
        print("喜歡羅莉控? 死宅男")
    if age == 18:
        break
print("對~你終於講句人話")
print("完成！亂按離開")
input()