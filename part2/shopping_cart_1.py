# Create a separate function for asking the user for prices.
def price():
    price_list = []  # create empty list
    while True:  # infinite loop
        user = input("input a price one at a time:")

        if user == "no":
            break  # stops the loop
        else:
            price_list.append(user)  # appends input to list
    return (price_list)

prices = price()

# pass the output of the price function through the shopping cart function

def sum_cart(prices):
    total = 0
    for item in prices:
        total += int(item)
    return total

print("The sum of the prices in the shopping cart is ${}".format(sum_cart(prices)))


# In that function, only ask for one price at a time.
# Use a while loop, to continue to ask for prices until the user enters "no".
# Pass the list to the sum_cart() function.
# Why two for loops. Refactor to one.