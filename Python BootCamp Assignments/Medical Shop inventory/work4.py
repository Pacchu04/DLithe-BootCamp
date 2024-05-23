class MedicalShop:
    def __init__(self):
        self.inventory={}

    def add_tablet(self,tablet_id,name,count):
        self.inventory[tablet_id]= {'name': name,'count': count}
    
    def buy_tablet(self,tablet_id,quantity):
        if tablet_id in self.inventory:
            self.inventory[tablet_id]['count'] +=quantity
            print(f"Bought {quantity} of {self.inventory[tablet_id]['name']}. New count: {self.inventory[tablet_id]['count']}")
        else:
            print(f"Tablet ID {tablet_id} not found in inventory")
    
    def sell_tablet(self,tablet_id,quantity):
        if tablet_id in self.inventory:
            if self.inventory[tablet_id]['count'] >=quantity:
                self.inventory[tablet_id]['count'] -=quantity
                print(f"Sold {quantity} of {self.inventory[tablet_id]['name']}. New count: {self.inventory[tablet_id]['count']}")
            else:
                print(f"Not enough stock to sell {quantity}")
        else:
            print(f"tablet ID {tablet_id} not found")

    def count_tablet(self,tablet_id):
        if tablet_id in self.inventory:
            return self.inventory[tablet_id]['count']
        else:
            print(f"Tablet ID {tablet_id} not found in inventory")
            return 0

shop= MedicalShop()

shop.add_tablet(1, 'Paracetamol', 100)
shop.add_tablet(2, 'Metformin', 50)

shop.buy_tablet(1, 50)
shop.sell_tablet(2, 5)
                      
print(f"Count of Paracetamol: {shop.count_tablet(1)}")
              

