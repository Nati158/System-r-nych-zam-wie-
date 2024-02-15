class Order:
    def __init__(self, order_id, customer_name, total_amount):
        self.order_id = order_id
        self.customer_name = customer_name
        self.total_amount = total_amount
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def display_order_details(self):
        print("Order ID:", self.order_id)
        print("Customer Name:", self.customer_name)
        print("Total Amount:", self.total_amount)
        print("Items:")
        for item in self.items:
            print("- ", item)

class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"{self.quantity} x {self.name} (${self.price})"

if __name__ == "__main__":
    order = Order(1, "John Doe", 100)
    order.add_item(Item("Product 1", 2, 25))
    order.add_item(Item("Product 2", 1, 50))
    order.display_order_details()
