from backend.products import Product


class Cart:
    def __init__(self, tot_price:float = 0):
        self.items = []
        self.tot_price = tot_price

    def add_item(self, item:Product):
        self.items.append(item)
        self.tot_price += item.price

    def remove_item(self, item_name):
        items_list = list(map(self.items, lambda x:x.product_name))
        
        if item_name not in items_list:
            return False

        self.tot_price -= self.items[items_list.index(item_name)].price
        self.items.pop(items_list.index(item_name))
        return True

