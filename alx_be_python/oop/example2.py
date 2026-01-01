class product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_stock_value(self):
        total_value = self.price * self.quantity
        return total_value
laptop = product("laptop", 1200, 3)
mouse_pad = product("mouse_pad", 30, 2)

laptop_value = laptop.calculate_stock_value()
print(f"product: {laptop.name}")
print(f"stock_quantity: {laptop.quantity}")
print(f"stock_value: {laptop_value}")
mouse_pad_value = mouse_pad.calculate_stock_value()
print(f"product: {mouse_pad.name}")
print(f"stock_quantity: {mouse_pad.quantity}")
print(f"stock_value: {mouse_pad_value}")