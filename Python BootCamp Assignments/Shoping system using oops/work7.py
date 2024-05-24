class Item:
    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def __str__(self):
        return f"{self.name} - ${self.price} x {self.quantity}"

    
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        
        for cart_item in self.items:
            if cart_item.name == item.name:
                cart_item.quantity += item.quantity
                return
        
        self.items.append(item)
    
    def remove_item(self, item_name, quantity=1):
        for cart_item in self.items:
            if cart_item.name == item_name:
                if cart_item.quantity > quantity:
                    cart_item.quantity -= quantity
                elif cart_item.quantity == quantity:
                    self.items.remove(cart_item)
                else:
                    print(f"Cannot remove {quantity} of {item_name}. Only {cart_item.quantity} in cart.")
                return
        print(f"{item_name} not found in the cart.")
    
    def view_cart(self):
        if not self.items:
            print("Your cart is empty.")
        else:
            print("Your cart contains:")
            for item in self.items:
                print(item)

    def calculate_total(self):
        total = sum(item.price * item.quantity for item in self.items)
        return total
    
    def checkout(self):
        if not self.items:
            print("Your cart is empty. Add items before checking out.")
            return
        total = self.calculate_total()
        print(f"Total amount: ${total:.2f}")
        print("Proceeding to checkout...")

if __name__ == "__main__":
    cart = ShoppingCart()
    item1 = Item("Laptop", 999.99, 1)
    item2 = Item("Mouse", 25.99, 2)
    item3 = Item("Keyboard", 45.99, 1)

    cart.add_item(item1)
    cart.add_item(item2)
    cart.add_item(item3)

    cart.view_cart()

    cart.remove_item("Mouse", 1)
    cart.view_cart()

    cart.remove_item("Mouse", 1)
    cart.view_cart()

    cart.remove_item("Mouse", 1)
    cart.view_cart()

    cart.checkout()