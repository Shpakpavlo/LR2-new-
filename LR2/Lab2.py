# Ймовірності попиту
demand_probabilities = [15/100, 30/100, 30/100, 25/100]

# Ціни
purchase_price = 50
normal_selling_price = 60
discounted_selling_price = 30

# Знайдемо оптимальний обсяг закупки
max_profit = float('-inf')
min_profit = float('inf')
optimal_purchase_quantity = 0
optimal_demand = 0

for purchase_quantity in range(1, 101):
    for demand in range(1, 101):
        revenue = 0
        if purchase_quantity >= demand:
            revenue += demand * normal_selling_price
        else:
            revenue += purchase_quantity * normal_selling_price
        costs = purchase_quantity * purchase_price
        profit = (revenue - costs) * demand_probabilities[demand - 1]
        if profit > max_profit:
            max_profit = profit
            optimal_purchase_quantity = purchase_quantity
            optimal_demand = demand
        if profit < min_profit:
            min_profit = profit

# Виведемо результат
print(f"Максимальний прибуток: {max_profit} грн")
print(f"Мінімальний прибуток: {min_profit} грн")
print(f"Оптимальний обсяг закупки: {optimal_purchase_quantity} одиниць")
print(f"Оптимальний попит: {optimal_demand} одиниць")
