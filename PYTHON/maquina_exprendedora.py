
class VendingMachine:
    def __init__(self):
        self.products = {
            1: {"name": "Soda", "price": 125},
            2: {"name": "Chips", "price": 100},
            3: {"name": "Candy", "price": 75},
            4: {"name": "Juice", "price": 150}
        }
        self.valid_coins = [5, 10, 50, 100, 200]
    
    def calculate_change(self, change):
        change_coins = []
        for coin in sorted(self.valid_coins, reverse=True):
            while change >= coin:
                change_coins.append(coin)
                change -= coin
        return change_coins
    
    def vend(self, coins, product_number):
        # Check for valid coins
        if not all(coin in self.valid_coins for coin in coins):
            return "Invalid coins provided.", coins
        
        # Check if product exists
        if product_number not in self.products:
            return "Product does not exist.", coins
        
        # Calculate total money provided
        total_money = sum(coins)
        product_price = self.products[product_number]["price"]
        
        if total_money < product_price:
            return "Insufficient funds.", coins
        
        # Calculate change
        change = total_money - product_price
        change_coins = self.calculate_change(change)
        
        return self.products[product_number]["name"], change_coins

# Ejemplo de uso
machine = VendingMachine()

# Caso 1: Monedas válidas, dinero suficiente, producto existente
print(machine.vend([100, 50, 50], 1))  