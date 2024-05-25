class Shop:
    def __init__(self,name):
        self.name=name
        self.items={}
    
    def add_item(self,item,quantity,cost_price):
        if item in self.items:
            self.items[item]["quantity"] +=quantity
        else:
            self.items[item]={"quantity":quantity, "cost_price": cost_price}

class Inventory(Shop):
    def __init__(self, name):
        super().__init__(name)
        self.low_stock_threshold=2
    
    def check_inventory(self):
        low_stock_items=[]
        for item, details in self.items.items():
            if details["quantity"] <=self.low_stock_threshold:
                low_stock_items.append(item)
        return low_stock_items

class Sales(Shop):
    def __init__(self, name):
        super().__init__(name)
        self.daily_sales=0
    
    def record_sale(self,item,quantity,selling_price):
        if item in self.items:
            self.items[item]["quantity"] -=quantity
            self.daily_sales += quantity * selling_price
        else:
            print(f"Item {item} not found in inventory")

class ShopManagement(Inventory,Sales):
    def __init__(self, name):
        super().__init__(name)
    
    def calculate_profit(self):
        total_cost=0
        total_revenue = self.daily_sales
        for item,details in self.items.items():
            total_cost += details["quantity"] * details["cost_price"]
        return total_revenue - total_cost

shop = ShopManagement("My Shop")


shop.add_item("Shirt", 100, 20000)
shop.add_item("Pants", 50, 10000)
shop.add_item("Hat", 20, 2000)

shop.record_sale("Shirt", 100, 700)
shop.record_sale("Pants", 50, 700)
shop.record_sale("Hat",20,200)


low_stock_items = shop.check_inventory()
print("Low stock items:", low_stock_items)


profit = shop.calculate_profit()
print("Todays Profit: ",shop.daily_sales)
print("Total profit:", profit)
