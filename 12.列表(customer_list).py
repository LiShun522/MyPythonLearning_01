name1 = "Sam"
name2 = "Eddy"
name3 = "Song"
name4 = "Benson"

print(name1,name2,name3,name4)

customer_list = []
type(customer_list)

customer_list = ["Sam","Eddy","Song","Benson"]
print(customer_list)

print(customer_list[0])

customer_list[0]="Redd"
print(customer_list)

for name in customer_list:
    print(f"My dear frined,{name},happy new year.")

customer_list.append("Dexter")

print(customer_list)

customer_list.insert(2,"Manrou")

print(customer_list)

print(customer_list[2])
print(customer_list[2])

customer_list[2]="Manrou Hong"

print(customer_list)

print(customer_list.index("Manrou Hong"))

print(customer_list[2])

sale_index = customer_list.index("Dexter")

print(customer_list[sale_index])

del customer_list[2]

customer_list.remove("Dexter")

print(customer_list)

customer_list.append("Lee")
customer_list.append("Dexter")
customer_list.append("Joker")
print(customer_list)

print(customer_list[0:5])

print(customer_list[-3:-1])
print(customer_list[-3:])

print(customer_list[0:5:2])
print(customer_list[-6::2])

print(customer_list)
customer_list.append(["寶寶",158,48,35])
print(customer_list)
print(customer_list[-1])
print(customer_list[-1][3])
customer_list[-1][3]=18
print(customer_list[-1])

print(customer_list)