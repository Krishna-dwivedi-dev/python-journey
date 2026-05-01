# Day 4: Bonus Q2 - Food Delivery Order Tracker

class FoodOrder:
    def __init__(self, restaurant_name, order_id):
        self.restaurant_name = restaurant_name
        self.order_id = order_id
        self.status = "Order Placed"

    def next_status(self):
        if self.status == "Order Placed":
            self.status = "Preparing"
        elif self.status == "Preparing":
            self.status = "Out for Delivery"
        elif self.status == "Out for Delivery":
            self.status = "Delivered"
        else:
            print("Order already delivered!")
            return
        print(f"Status updated: {self.status}")

    def cancel_order(self):
        if self.status == "Order Placed":
            self.status = "Cancelled"
            print(f"Order #{self.order_id} cancelled successfully!")
        else:
            print("Order already in progress, cannot cancel!")

    def display(self):
        print(f"Order #{self.order_id} | Restaurant: {self.restaurant_name} | Status: {self.status}")

# Test
order1 = FoodOrder("Starbux", 250)
order1.next_status()
order1.cancel_order()
order1.display()

order2 = FoodOrder("Sunset", 315)
order2.next_status()
order2.next_status()
order2.next_status()
order2.next_status()
order2.display()