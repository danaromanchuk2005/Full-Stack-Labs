class Shop:
    def __init__(self, shop_name, store_type):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = 0

    def set_number_of_units(self, val):
        self.number_of_units = val

    def increment_number_of_units(self, val):
        self.number_of_units += val

class Discount(Shop):
    def __init__(self, shop_name, store_type):
        super().__init__(shop_name, store_type)
        self.discount_products = ["Яблука", "Банани", "Одяг"]
