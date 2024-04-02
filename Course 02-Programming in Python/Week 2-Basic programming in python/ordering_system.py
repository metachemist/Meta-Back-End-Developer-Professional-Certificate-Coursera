menu = {
    1: {"name": 'espresso', "price": 1.99},
    2: {"name": 'coffee', "price": 2.50},
    3: {"name": 'cake', "price": 2.79},
    4: {"name": 'soup', "price": 4.50},
    5: {"name": 'sandwich', "price": 4.99},    
}

#program starts executing from here
if __name__ == "__main__"
    main()  #this will call main function!

#01
def main():
    order = take_order()
    print_order(order)

    subtotal = calculate_subtotal(order)
    print("Subtotal for the order is:")

    tax = calculate_tax(subtotal)
    print("Tax for the order is: " + str(tax))

    items, subtotal = summarize_order(order)

#03 take order calls display menu
def display_menu():
    print(" ----- Menu ----- ")
    for selection in menu:
        print(f"{selection}. {menu[selection]['name'] : <9} | {menu[selection]['price']} : >5")
    print()

#02
def take_order():
    display_menu()
    order = []
    count = 1
    for i in range(3):
        item = input('select menu item number ' + str(count) + '(from 1 to 5):')  
        count +=1
        order.extend(menu[int(item)])
    return order

# print_order called by main function
def print_order(order):
    print("You have ordered" + str(len(order)) + "items")
    items = []
    items = [item["name"] for item in order]
    print(items)
    return order
    
def summarize_order(order):
    """ Summarizes the order """
    names = [item["name"] for item in order]
    subtotal = calculate_subtotal(order)
    tax = calculate_tax(subtotal)
    total = subtotal + tax
    return names, round(total, 2)

def calculate_tax(subtotal):  
    """ Calculates the tax of an order """
    tax = subtotal * 0.15
    return round(tax, 2)

def calculate_subtotal(order):
    """ Calculates the subtotal of an order """
    subtotal = sum(item["price"] for item in order)
    return subtotal