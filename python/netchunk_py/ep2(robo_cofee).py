# Let's start a coffee shop together!! We're going to build a coffee shop using some new python programming concepts!!

#let's build robot wasikaran!!!

print("Hello, welcome to furi coffee!!!!!!!!!!!!!")
name=(input("What is your name?\n:"))
print(f"Hello {name}, Thank you so much for coming in today.\n")

menu="Americano, Espresso, Latte, Cappucino"

print(f"{name}, What whould you like from our menu today? Here is what we are serving.\n {menu}")

order=input(":")

price=60

quantity=int(input("How manny coffees would you like\n:"))
total=price*quantity
print(f"Thank you, Your total is Rupee :{total}.\n")
print(f"Sounds good {name}, We'll have your {quantity} {order} ready for you in a moment.")
