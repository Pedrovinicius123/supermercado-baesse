from dataclasses import dataclass
from products import Product


@dataclass
class Cart:
    items: list
    tot_price: float

    def add_item(self, item:Product):
        self.items.append(item)
        self.tot_price += items.price

    def remove_item(self, item_name):
        items_list = list(map(self.items, lambda x:x.product_name))
        
        if item_name not in items_list:
            return False

        self.tot_price -= self.items[items_list.index(item_name)].price
        self.items.pop(items_list.index(item_name))
        return True

