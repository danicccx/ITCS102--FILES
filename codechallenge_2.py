amount = eval(input("Enter amount to deposit ---> "))

print("Here is a breakdown of the deposit amount:"))
print(amount // 1000, "- 1000")
amount = amount % 1000
print(amount // 500, "- 500")
amount = amount % 500
print(amount // 200, "- 200")
amount = amount % 200
print(amount // 100, "- 100")
amount = amount % 100
print(amount // 50, "- 50")
amount = amount % 50
print(amount // 20, "- 20")
amount = amount % 20
print(amount // 10, "- 10")
amount = amount % 10
print(amount // 5, "- 5")
amount = amount % 5
print(amount // 1, "- 1")
amount = amount % 1

