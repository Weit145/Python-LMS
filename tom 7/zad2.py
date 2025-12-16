class Product:
    def __init__(self, name: str, price: float, category: str):
        self.name = name
        self.price = price
        self.category = category
    
    def __str__(self):
        return f"{self.name} - {self.price} руб. ({self.category})"


class Order:
    def __init__(self, order_id: str):
        self.order_id = order_id
        self.products = []
        self.discount = 0 
        self.category_discounts = {} 
    
    def add_product(self, product: Product):
        self.products.append(product)
    
    def remove_product(self, name: str):
        for p in self.products:
            if p.name == name:
                self.products.remove(p)
                return True
        return False
    
    def set_order_discount(self, percent: float):
        self.discount = percent
    
    def set_category_discount(self, category: str, percent: float):
        self.category_discounts[category] = percent
    
    def total_price(self) -> float:
        total = 0
        for product in self.products:
            price = product.price
            if product.category in self.category_discounts:
                price *= (100 - self.category_discounts[product.category]) / 100
            price *= (100 - self.discount) / 100
            total += price
        return total
    
    def category_price(self, category: str) -> float:
        total = 0
        for product in self.products:
            if product.category == category:
                price = product.price
                if category in self.category_discounts:
                    price *= (100 - self.category_discounts[category]) / 100
                price *= (100 - self.discount) / 100
                total += price
        return total
    
    def show(self):
        print(f"\nЗаказ #{self.order_id}")
        print("Товары:")
        for product in self.products:
            print(f"  {product}")
        if self.discount > 0:
            print(f"Скидка на заказ: {self.discount}%")
        if self.category_discounts:
            print("Скидки по категориям:")
            for category, discount in self.category_discounts.items():
                print(f"  {category}: {discount}%")
        print(f"Общая стоимость: {self.total_price():.2f} руб.")


if __name__ == "__main__":
    laptop = Product("Ноутбук", 75000, "Электроника")
    book = Product("Книга", 1200, "Книги")
    shirt = Product("Футболка", 1500, "Одежда")
    order = Order("001")
    order.add_product(laptop)
    order.add_product(book)
    order.add_product(shirt)
    order.set_category_discount("Электроника", 10)
    order.set_order_discount(5)                    
    order.show()
    print(f"\nСтоимость электроники: {order.category_price('Электроника'):.2f} руб.")