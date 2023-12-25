#使用 a = input("XXX:")代表，你要輸入一個變量，他會帶入在:之後要你輸入，值出來後便可以用{}加入到表格變量
name = input("Your Name:")
age = int(input("Your Age:"))
#若強制只要數字可在input()前面加上int(input())

hobbie = input("Your Hobbie:")
job = input("Your Job:")
sport = input("Your Favorite Sport:")

#若想要輸入非數字時，顯示錯誤
lucky = input("Your Lucky number:")
if lucky.isdigit():
    age = int(age)
else:
    print("需輸入數字")
    exit()

#加上f可以在段落中用{}表示變量，不然的話要用%，每個都要寫
msg = f"""
---------{name}-----------
Name:{name}
Age:{age},Great,still powerful,in {50-age} years you will be 50 year old.
Hobbie:{hobbie}
Job:{job}
Favorite Sport:{sport}
Lucky Number:{lucky}
----------END------------
"""
print(msg)



