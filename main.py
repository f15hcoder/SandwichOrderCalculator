total_cost = 0.00 
sugar_tax = 0.50 
print("Sandwich or Wrap?") 
bread_type = input().upper() 
print("Meat, Vegetarian or Vegan?") 
filling_type = input().upper() 
print("Chilli sauce, Tomato sauce or None?")
sauce = input().upper()
print("Would you like extra salad?")
salad = input().upper()
print("Cookie, Crisps, Fruit or None") 
pudding = input().upper() 
print("Fizzy drink, Water, Juice or None") 
drink = input().upper()
if bread_type != "SANDWICH": 
  total_cost = 2.00 
else: 
  total_cost = 3.00 
if filling_type == "VEGETARIAN" or filling_type == "VEGAN": 
  total_cost = total_cost + 1.00 
else: 
  total_cost = total_cost + 1.50 
if sauce == "CHILLI SAUCE" or sauce == "TOMATO SAUCE":
  total_cost = total_cost + 0.50
if sauce == "NONE":
  total_cost = total_cost - 0.50
if salad != "NO":
  total_cost = total_cost + 0.50
if salad != "NO" and sauce != "NONE":
  total_cost = total_cost + 1.00
if pudding == "COOKIE" and drink == "FIZZY DRINK": 
  total_cost = total_cost + sugar_tax 
if pudding == "NONE" and drink == "NONE": 
  total_cost = total_cost - sugar_tax
print(f"Your total cost is: £{total_cost}") 