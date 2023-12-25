
print(12/2)
# %為整除=0
print(12%2)
# %整除完餘數
print(12%5)
# i為臨時變量、(20)=0~19
for i in range(20):
    print(i)
#若(20)整除2後不為0，則為奇數
for i in range(20):
    if i % 2 != 0 : #奇數
        print(i)

#次方計算
print(2**10)
print(5**3)
print(2**10,5**6)

#整除，不留小數
print(9/2)
print(9//2)

#Ture和False判斷
a = 9
b = 6
c = 3
print(a == b)
print(a != c)

#賦值運算
a = a+1
print(a)
a += 1
print(a)
a -= 1
print(a)
a *= c
a //= 4
print(a)
a %= 2
print(a)

#邏輯運算 and、or、not
print(a,b,c)
print( a < b and a < c )
d = 1
print( a >= d and c > d )
print( a >= d and c > d or b <= a or a != d)
print( a >= d and c > d and (b <= a or a != d))
print( a >= d and c > d and (b <= a or a <= d) and a == d)

print(not a > b)
customer_list = 'Redd', 'Eddy', 'Song', 'Benson', 'Lee', 'Dexter', 'Joker'
print(customer_list)
print("Lee" not in customer_list)
print("Dexter" in customer_list)
