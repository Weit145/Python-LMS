class Tableware:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"{self.name} ({self.price} руб.)"

class Table:
    def __init__(self, max_items: int = 5):
        self.max_items = max_items
        self.items = []
    
    def put_item(self, item: Tableware):
        if len(self.items) < self.max_items:
            self.items.append(item)
            return True
        return False
    
    def remove_item(self, name: str):
        for item in self.items:
            if item.name == name:
                self.items.remove(item)
                return item
        return None
    
    def find_by_name(self, name: str):
        return [item for item in self.items if name.lower() in item.name.lower()]
    
    def find_by_price(self, max_price: float):
        return [item for item in self.items if item.price <= max_price]
    
    def total_cost(self):
        return sum(item.price for item in self.items)
    
    def show(self):
        print(f"Стол (мест: {len(self.items)}/{self.max_items}):")
        for item in self.items:
            print(f"  - {item.name}: {item.price} руб.")
        print(f"Общая стоимость: {self.total_cost()} руб.")

if __name__ == "__main__":
    fork = Tableware("Вилка", 150)
    spoon = Tableware("Ложка", 120)
    knife = Tableware("Нож", 180)
    table = Table(max_items=3)
    table.put_item(fork)
    table.put_item(spoon)
    table.put_item(knife)
    table.show()
    print("\nПоиск 'ложка':")
    found = table.find_by_name("ложка")
    
    for item in found:
        print(f"  Найден: {item.name}")
        
    print(f"\nОбщая стоимость: {table.total_cost()} руб.")
    print("\nУбираем нож:")
    table.remove_item("Нож")
    table.show()