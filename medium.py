price = eval(input("Input Item Price ---> "))
qty = eval(input("Item Quantity ---> "))

cost = price * qty

if cost >= 100:
  discount = cost * 0.10
  final_cost = cost - discount 
  print("Discount price is ", final_cost)

else:
  print("No discount is applied, cost is ", cost)
