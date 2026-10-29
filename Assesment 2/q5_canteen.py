def add_item_buggy(item, order=[]):
    order.append(item)
    return order


def add_item(item, order=None):
    if order is None:
        order = []

    order.append(item)
    return order


# Buggy function
print(add_item_buggy("Tea"), add_item_buggy("Vada"))

# Correct function
print(add_item("Tea"), add_item("Vada"))

# Show the default value
print("Default value:", add_item_buggy.__defaults__)


# Returning multiple values
def calculate_bill(amount):
    gst = amount * 0.05
    total = amount + gst
    return total, gst


total, gst = calculate_bill(100)
print("Total:", total)
print("GST:", gst)


# Local and global scope
x = 10

def show_scope():
    x = 20
    print("Local x:", x)


show_scope()
print("Global x:", x)


# Nonlocal scope
def outer():
    value = 5

    def inner():
        nonlocal value
        value = 10

    inner()
    print("Nonlocal value:", value)


outer()