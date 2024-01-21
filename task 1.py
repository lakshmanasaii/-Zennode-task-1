A = 20
B = 40
C = 50

print(
    """A = $20
B = $40
C = $50"""
)

cart = 0
quantity_count = 0
quantity_count_A = 0
quantity_count_B = 0
quantity_count_C = 0

# entering the details

while True:
    product = input("Enter the product u want to buy [1 product at a time (A, B, C) ]:") # THE CUSTUMER MUST ENTER ONE PRODUCT LETTER IN ONE SELECTIOM
    quantity = int(input("Enter the product of quantity [1 to 100]:")) # YOU CAN ENTER AS MUCH AS NEEDED
    if product.upper() == "A":
        cart += 20 * quantity
        quantity_count += quantity
        quantity_count_A = quantity
    elif product.upper() == "B":
        cart += 40 * quantity
        quantity_count += quantity
        quantity_count_B = quantity
    elif product.upper() == "C":
        cart += 50 * quantity
        quantity_count += quantity
        quantity_count_C = quantity
    else:
        print(
            """Error Enter the product and quantity clearly [A = $20 : B = $40 : C = $50]"""
        )
        pass
    out = input("Do u wish to countinue [yes or no]:")
    if out.lower() != "yes":
        break

# DISCOUNTS SECTION

if cart > 200:
    cart -= 10
    print(f"after the 10% discount: {cart}")
elif quantity_count_A > 10:
    cart -= 5
    print(f"after the 5% discount:-{cart}")
elif quantity_count_B > 10:
    cart -= 5
    print(f"after the 5% discount:-{cart}")
elif quantity_count_C > 10:
    cart -= 5
    print(f"after the 5% discount:-{cart}")

# 50% DISCOUNT SECTION

cart1 = 0
if quantity_count >= 30:
    if quantity_count_A >= 15:
        cart1 = (((quantity_count_B * B) * 0.5) + ((quantity_count_C * C) * 0.5)) + (
            quantity_count_A * A
        )
    if quantity_count_B >= 15:
        cart1 = (((quantity_count_A * A) * 0.5) + ((quantity_count_C * C) * 0.5)) + (
            quantity_count_B * B
        )
    if quantity_count_C >= 15:
        cart1 = (((quantity_count_B * B) * 0.5) + ((quantity_count_A * A) * 0.5)) + (
            quantity_count_C * C
        )
    print(f"after the 50%: {cart1}")


# Gift wrap fee: $1 per unit.

gift_wrap = quantity_count * 1
print(f"gift wrap fee: ${gift_wrap}")

# Shipping fee: 10 units can be packed in one package, and the shipping fee for each package is $5.

shipping_fee = (quantity_count / 10) * 5
print(f"shipping fee: ${shipping_fee}")

# Total

print(f"Total quantify of products: {quantity_count}")
print(f" Product A Toatl Quantity :{quantity_count_A}")
print(f" Product B Toatl Quantity :{quantity_count_B}")
print(f" Product C Toatl Quantity :{quantity_count_C}")

# THE FINAL WILL BE SELETED BY USING A MIN FUNCTION ITS SHOWS THE LESS VALUE B/W TO NUMBERS 

final = min(cart, cart1)
if final != 0:
    print(f"final amount {final + gift_wrap + shipping_fee}")
else:
    print(f"final amount {cart + gift_wrap + shipping_fee}")
